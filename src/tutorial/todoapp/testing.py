# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone import api
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.testing import z2

import unittest2 as unittest


class TodoAppLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import tutorial.todoapp
        self.loadZCML(package=tutorial.todoapp)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'tutorial.todoapp:default')

        # Login and create a folder we're gonna use for testing
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        api.content.create(
            container=portal,
            type='Folder',
            id='folder',
        )

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'tutorial.todoapp')


FIXTURE = TodoAppLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="TodoAppLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="TodoAppLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests using zope.testbrowser."""

    layer = FUNCTIONAL_TESTING
