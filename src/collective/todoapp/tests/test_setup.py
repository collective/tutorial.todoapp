# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.todoapp.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName

import unittest2 as unittest


class TestInstall(IntegrationTestCase):
    """Test installation of collective.todoapp into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.todoapp is installed with portal_quickinstaller."""
        self.failUnless(self.installer.isProductInstalled('collective.todoapp'))

    def test_uninstall(self):
        """Test if collective.todoapp is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.todoapp'])
        self.failIf(self.installer.isProductInstalled('collective.todoapp'))

    # properties.xml
    def test_portal_title(self):
        """Test if portal title was correctly updated."""
        title = self.portal.getProperty('title')
        self.assertEquals("Todo App Tutorial", title)

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ITodoAppLayer is registered."""
        from collective.todoapp.interfaces import ITodoAppLayer
        from plone.browserlayer import utils
        self.failUnless(ITodoAppLayer in utils.registered_layers())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
