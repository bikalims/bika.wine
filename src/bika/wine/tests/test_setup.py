# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from bika.wine.testing import BIKA_WINE_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that bika.wine is properly installed."""

    layer = BIKA_WINE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if bika.wine is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'bika.wine'))

    def test_browserlayer(self):
        """Test that IBikaWineLayer is registered."""
        from bika.wine.interfaces import (
            IBikaWineLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IBikaWineLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = BIKA_WINE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['bika.wine'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if bika.wine is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'bika.wine'))

    def test_browserlayer_removed(self):
        """Test that IBikaWineLayer is removed."""
        from bika.wine.interfaces import \
            IBikaWineLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IBikaWineLayer,
            utils.registered_layers())
