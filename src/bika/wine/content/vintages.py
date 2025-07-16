# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer

from bika.wine.interfaces import IVintages
from senaite.core.interfaces import IHideActionsMenu


class IVintangesSchema(model.Schema):
    """Schema interface
    """


@implementer(IVintages, IVintangesSchema, IHideActionsMenu)
class Vintages(Container):
    """A folder/container for material types
    """
