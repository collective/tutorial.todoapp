# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from plone import api
from collective.todoapp.tests.base import IntegrationTestCase

import unittest2 as unittest


class TestInstall(IntegrationTestCase):
    """Test installation of collective.todoapp into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_product_installed(self):
        """Test if collective.todoapp is installed in portal_quickinstaller."""
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('collective.todoapp'))

    def test_uninstall(self):
        """Test if collective.todoapp is cleanly uninstalled."""
        installer = api.portal.get_tool('portal_quickinstaller')
        installer.uninstallProducts(['collective.todoapp'])
        self.assertFalse(installer.isProductInstalled('collective.todoapp'))

    # properties.xml
    def test_portal_title(self):
        """Test if portal title was correctly updated."""
        title = self.portal.getProperty('title')
        self.assertEquals("Todo App Tutorial", title)

    # Folder.xml
    def test_folder_available_layouts(self):
        """Test that our custom display layout (@@todo) is available on folders
        and that the default ones are also still there.
        """
        layouts = self.portal.folder.getAvailableLayouts()
        layout_ids = [id for id, title in layouts]

        # default layouts
        self.assertIn('folder_listing', layout_ids)
        self.assertIn('folder_summary_view', layout_ids)
        self.assertIn('folder_tabular_view', layout_ids)
        self.assertIn('atct_album_view', layout_ids)
        self.assertIn('folder_full_view', layout_ids)

        # our custom one
        self.assertIn('todo', layout_ids)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
