# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from bika.lims import api
from bika.lims.utils import get_link
from bika.extras import is_installed
from bika.extras.config import _
from senaite.app.listing.interfaces import IListingView
from senaite.app.listing.interfaces import IListingViewAdapter


class SamplesListingViewAdapter(object):
    adapts(IListingView)
    implements(IListingViewAdapter)

    def __init__(self, listing, context):
        self.listing = listing
        self.context = context

    def before_render(self):
        if not is_installed():
            return

        cultivar = [("Cultivar", {"toggle": True, "title": _("Cultivar")})]
        self.listing.columns.update(cultivar)
        vintage = [("Vintage", {"toggle": True, "title": _("Vintage")})]
        self.listing.columns.update(vintage)
        for i in range(len(self.listing.review_states)):
            self.listing.review_states[i]["columns"].append("Cultivar")
            self.listing.review_states[i]["columns"].append("Vintage")

    def folder_item(self, obj, item, index):
        if not is_installed():
            return item

        full_object = api.get_object(obj)
        cultivar = full_object.Schema().getField("Cultivar")
        if cultivar:
            cultivar = cultivar.get(full_object)
            cultivar_title = cultivar.Title()
            cultivar_url = cultivar.absolute_url()
            cultivar_link = get_link(cultivar_url, cultivar_title)
            item["Cultivar"] = cultivar_title
            item["replace"]["Cultivar"] = cultivar_link

        vintage = full_object.Schema().getField("Vintage")
        if vintage:
            vintage = vintage.get(full_object)
            vintage_title = vintage.Title()
            vintage_url = vintage.absolute_url()
            vintage_link = get_link(vintage_url, vintage_title)
            item["Vintage"] = vintage_title
            item["replace"]["Vintage"] = vintage_link

        return item
