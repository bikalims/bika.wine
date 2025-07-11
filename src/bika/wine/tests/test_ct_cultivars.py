# -*- coding: utf-8 -*-
from bika.wine.testing import BIKA_WINE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class CultivarsIntegrationTest(unittest.TestCase):

    layer = BIKA_WINE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'BikaSetup',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_cultivars_schema(self):
        fti = queryUtility(IDexterityFTI, name='Cultivars')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('Cultivars')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_cultivars_fti(self):
        fti = queryUtility(IDexterityFTI, name='Cultivars')
        self.assertTrue(fti)

    def test_ct_cultivars_factory(self):
        fti = queryUtility(IDexterityFTI, name='Cultivars')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_cultivars_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Cultivars',
            id='cultivars',
        )


        parent = obj.__parent__
        self.assertIn('cultivars', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('cultivars', parent.objectIds())

    def test_ct_cultivars_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Cultivars')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_cultivars_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Cultivars')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'cultivars_id',
            title='Cultivars container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
