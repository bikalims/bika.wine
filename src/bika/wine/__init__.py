# -*- coding: utf-8 -*-
"""Init and utils."""
from bika.lims.api import get_request
from bika.wine.interfaces import IBikaWineLayer


def is_installed():
    """Returns whether the product is installed or not"""
    request = get_request()
    return IBikaWineLayer.providedBy(request)
