# -*- coding: utf-8 -*-

from plone.dexterity.content import Container
from plone.supermodel import model
from zope.interface import implementer

from bika.wine.interfaces import ICultivars
from senaite.core.interfaces import IHideActionsMenu


class ICultivarsSchema(model.Schema):
    """Schema interface
    """


@implementer(ICultivars, ICultivarsSchema, IHideActionsMenu)
class Cultivars(Container):
    """A folder/container for material types
    """
