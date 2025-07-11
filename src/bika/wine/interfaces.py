# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBikaWineLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ICultivars(Interface):
    """Marker interface for cultivars setup folder
    """


class ICultivar(Interface):
    """Marker interface for cultivar
    """
