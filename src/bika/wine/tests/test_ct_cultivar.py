# -*- coding: utf-8 -*-
from bika.wine.content.cultivar import ICultivar  # NOQA E501
from bika.wine.testing import BIKA_WINE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class CultivarIntegrationTest(unittest.TestCase):

    layer = BIKA_WINE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Cultivars',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_cultivar_schema(self):
        fti = queryUtility(IDexterityFTI, name='Cultivar')
        schema = fti.lookupSchema()
        self.assertEqual(ICultivar, schema)

    def test_ct_cultivar_fti(self):
        fti = queryUtility(IDexterityFTI, name='Cultivar')
        self.assertTrue(fti)

    def test_ct_cultivar_factory(self):
        fti = queryUtility(IDexterityFTI, name='Cultivar')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICultivar.providedBy(obj),
            u'ICultivar not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_cultivar_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Cultivar',
            id='cultivar',
        )

        self.assertTrue(
            ICultivar.providedBy(obj),
            u'ICultivar not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('cultivar', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('cultivar', parent.objectIds())

    def test_ct_cultivar_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Cultivar')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
