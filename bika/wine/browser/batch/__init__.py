from bika.lims.browser import BrowserView
from bika.lims.permissions import *
from operator import itemgetter

import json
import plone
import plone.protect


class getAnalysisContainers(BrowserView):

    """ Vocabulary source for jquery combo dropdown box
    Returns AnalysisRequst and Batch objects currently
    available to be inherited into this Batch.
    """

    def __call__(self):
        plone.protect.CheckAuthenticator(self.request)
        searchTerm = self.request['searchTerm'].lower()
        page = self.request['page']
        nr_rows = self.request['rows']
        sord = self.request['sord']
        sidx = self.request['sidx']

        rows = []

        ars = []
        for x in [a.getObject() for a in
                  self.bika_catalog(
                    portal_type='AnalysisRequest',
                    cancellation_state='active',
                    sort_on="created",
                    sort_order="desc")]:
            if searchTerm in x.Title().lower():
                ars.append(x)

        batches = []
        for x in [a.getObject() for a in
                  self.bika_catalog(
                    portal_type='Batch',
                    cancellation_state='active',
                    sort_on="created",
                    sort_order="desc")]:
            if searchTerm in x.Title().lower() \
            or searchTerm in x.Schema()['BatchID'].get(x).lower() \
            or searchTerm in x.Schema()['WorksOrderID'].get(x).lower() \
            or searchTerm in x.Schema()['ClientBatchID'].get(x).lower():
                batches.append(x)

        _rows = []
        for item in batches:
            _rows.append({
                'Title': item.Title(),
                'ObjectID': item.id,
                'Description': item.Description(),
                'UID': item.UID()
            })
            _rows = sorted(_rows, cmp=lambda x, y: cmp(x.lower(), y.lower()),
                           key=itemgetter(sidx and sidx or 'Title'))

        rows += _rows

        _rows = []
        for item in ars:
            _rows.append({
                'Title': item.Title(),
                'ObjectID': item.id,
                'Description': item.Description(),
                'UID': item.UID()
            })
            _rows = sorted(_rows, cmp=lambda x, y: cmp(x.lower(), y.lower()),
                           key=itemgetter(sidx and sidx or 'Title'))

        rows += _rows

        if sord == 'desc':
            rows.reverse()
        pages = len(rows) / int(nr_rows)
        pages += divmod(len(rows), int(nr_rows))[1] and 1 or 0
        start = (int(page) - 1) * int(nr_rows)
        end = int(page) * int(nr_rows)
        ret = {'page': page,
               'total': pages,
               'records': len(rows),
               'rows': rows[start:end]}

        return json.dumps(ret)
