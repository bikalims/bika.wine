# -*- coding: utf-8 -*-

import collections

from bika.lims import api
from bika.lims import senaiteMessageFactory as _
from bika.lims.utils import get_link_for
from senaite.core.i18n import translate
from senaite.core.permissions import AddAnalysisCategory
from senaite.app.listing import ListingView


class VintagesView(ListingView):

    def __init__(self, context, request):
        super(VintagesView, self).__init__(context, request)

        self.catalog = 'senaite_catalog_setup'

        self.contentFilter = {
            "portal_type": "Vintage",
            "sort_on": "sortable_title",
            "sort_order": "ascending",
            "path": {
                "query": api.get_path(self.context),
                "depth": 1,
            },
        }

        self.context_actions = {
            _("listing_vintages_action_add", default="Add"): {
                "url": "++add++Vintage",
                "permission": AddAnalysisCategory,
                "icon": "senaite_theme/icon/plus"
            }
        }

        self.title = translate(_(
            "listing_vintages_title",
            default="Vintages")
        )
        self.icon = api.get_icon("Vintages", html_tag=False)
        self.show_select_column = True

        self.columns = collections.OrderedDict((
            ("Title", {
                "title": _(
                    u"listing_vintages_column_title",
                    default=u"Vintage",
                ),
                "index": "sortable_title"}),
        ))

        self.review_states = [
            {
                "id": "default",
                "title": _(
                    u"listing_vintages_state_active",
                    default=u"Active",
                ),
                "contentFilter": {"is_active": True},
                "columns": self.columns.keys(),
            }, {
                "id": "inactive",
                "title": _(
                    u"listing_vintages_state_inactive",
                    default=u"Inactive",
                ),
                "contentFilter": {'is_active': False},
                "columns": self.columns.keys(),
            }, {
                "id": "all",
                "title": _(
                    u"listing_vintages_state_all",
                    default=u"All",
                ),
                "contentFilter": {},
                "columns": self.columns.keys(),
            },
        ]

    def folderitem(self, obj, item, index):
        obj = api.get_object(obj)
        item["replace"]["Title"] = get_link_for(obj)
        return item
