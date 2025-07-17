# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from AccessControl import ClassSecurityInfo
from plone.dexterity.content import Item
# from plone.namedfile import field as namedfile
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
# from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer

from bika.lims.interfaces import IDeactivable
from bika.wine.interfaces import ICultivar
from bika.lims import api
from senaite.core.catalog import SETUP_CATALOG


from bika.wine.config import _


class ICultivarSchema(model.Schema):
    """ Marker interface and Dexterity Python Schema for Cultivar
    """
    code = schema.TextLine(
        title=_(
            u"title_cultivar_code",
            default=u"Code"
        ),
        description=_(
            u"description_cultivar_code",
            default=u"Code of the cultivar"
        ),
        required=False,
    )


@implementer(ICultivar, ICultivarSchema, IDeactivable)
class Cultivar(Item):
    """
    """
    _catalogs = [SETUP_CATALOG]

    security = ClassSecurityInfo()

    @security.private
    def accessor(self, fieldname):
        """Return the field accessor for the fieldname"""
        schema = api.get_schema(self)
        if fieldname not in schema:
            return None
        return schema[fieldname].get

    @security.private
    def mutator(self, fieldname):
        """Return the field mutator for the fieldname"""
        schema = api.get_schema(self)
        if fieldname not in schema:
            return None
        result = schema[fieldname].set
        self.reindexObject()
        return result
