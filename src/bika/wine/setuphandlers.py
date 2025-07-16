# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

from bika.lims import api
from senaite.core.setuphandlers import add_dexterity_items
from senaite.core.setuphandlers import setup_other_catalogs

from bika.wine.config import PROFILE_ID
from bika.wine.config import logger

INDEXES = []

# Tuples of (catalog, column_name)
COLUMNS = []

NAVTYPES = []

# An array of dicts. Each dict represents an ID formatting configuration
ID_FORMATTING = [
    {
        "portal_type": "Cultivar",
        "form": "CLT{seq:06d}",
        "prefix": "cultivar",
        "sequence_type": "generated",
        "counter_type": "",
        "split_length": 1,
    },
    {
        "portal_type": "Vintage",
        "form": "VTG{seq:06d}",
        "prefix": "vintage",
        "sequence_type": "generated",
        "counter_type": "",
        "split_length": 1,
    }
]


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'bika.wine:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    logger.info("BIKA.WINE post install handler [BEGIN]")
    profile_id = PROFILE_ID
    context = context._getImportContext(profile_id)
    portal = context.getSite()
    add_dexterity_setup_items(portal)
    setup_id_formatting(portal)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def add_dexterity_setup_items(portal):
    """Adds the Dexterity Container in the Setup Folder

    N.B.: We do this in code, because adding this as Generic Setup Profile in
          `profiles/default/structure` flushes the contents on every import.
    """
    # Tuples of ID, Title, FTI
    items = [
        ("cultivars", "Cultivars", "Cultivars"),
        ("vintages", "Vintages", "Vintages"),
    ]
    setup = api.get_senaite_setup()
    add_dexterity_items(setup, items)


def setup_catalogs(portal):
    """Setup catalogs"""
    setup_other_catalogs(portal, indexes=INDEXES, columns=COLUMNS)


def setup_id_formatting(portal, format_definition=None):
    """Setup default ID formatting"""
    if not format_definition:
        logger.info("Setting up ID formatting ...")
        for formatting in ID_FORMATTING:
            setup_id_formatting(portal, format_definition=formatting)
        logger.info("Setting up ID formatting [DONE]")
        return

    bs = portal.bika_setup
    p_type = format_definition.get("portal_type", None)
    if not p_type:
        return

    form = format_definition.get("form", "")
    if not form:
        logger.info("Param 'form' for portal type {} not set [SKIP")
        return

    logger.info("Applying format '{}' for {}".format(form, p_type))
    ids = list()
    for record in bs.getIDFormatting():
        if record.get("portal_type", "") == p_type:
            continue
        ids.append(record)
    ids.append(format_definition)
    bs.setIDFormatting(ids)
