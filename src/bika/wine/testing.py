# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import bika.wine


class BikaWineLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=bika.wine)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'bika.wine:default')


BIKA_WINE_FIXTURE = BikaWineLayer()


BIKA_WINE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BIKA_WINE_FIXTURE,),
    name='BikaWineLayer:IntegrationTesting',
)


BIKA_WINE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BIKA_WINE_FIXTURE,),
    name='BikaWineLayer:FunctionalTesting',
)


BIKA_WINE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        BIKA_WINE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='BikaWineLayer:AcceptanceTesting',
)
