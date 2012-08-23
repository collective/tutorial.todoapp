# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from plone import api
from tutorial.todoapp.testing import IntegrationTestCase

import unittest2 as unittest


class TestInstall(IntegrationTestCase):
    """Test installation of tutorial.todoapp into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_product_installed(self):
        """Test if tutorial.todoapp is installed in portal_quickinstaller."""
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('tutorial.todoapp'))

    def test_uninstall(self):
        """Test if tutorial.todoapp is cleanly uninstalled."""
        installer = api.portal.get_tool('portal_quickinstaller')
        installer.uninstallProducts(['tutorial.todoapp'])
        self.assertFalse(installer.isProductInstalled('tutorial.todoapp'))

    # metadata.xml
    def test_dependencies_installed(self):
        """Test that all product dependencies are installed.

        These are add-on that would otherwise need to be installed through
        the Plone Control Panel. Since they are listed in metadata.xml they
        will be installed automatically when this product is installed.
        """
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('plone.app.dexterity'))

    # types/todo_item.xml
    def test_todo_item_installed(self):
        """Test that Todo Item content type is listed in portal_types."""
        types = api.portal.get_tool('portal_types')
        self.assertIn('todo_item', types.objectIds())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
