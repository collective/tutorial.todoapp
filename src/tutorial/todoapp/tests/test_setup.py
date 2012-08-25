# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from tutorial.todoapp.tests.base import IntegrationTestCase
from plone import api

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
        """Test that all dependencies are installed."""
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('plone.app.dexterity'))

    # types/Folder.xml
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

    # types/todo_item.xml
    def test_todo_item_installed(self):
        """Test that Todo Item content type is listed in portal_types."""
        types = api.portal.get_tool('portal_types')
        self.assertIn('todo_item', types.objectIds())

    # workflows/todo_item_workflow/definition.xml
    def test_todo_item_workflow_installed(self):
        """"Test that todo_item_workflow is listed in portal_workflow."""
        workflow = api.portal.get_tool('portal_workflow')
        self.assertIn('todo_item_workflow', workflow.objectIds())

    # workflows.xml
    def test_todo_item_workflow(self):
        """Test if todo_item is present and mapped to Todo Item content type."""
        workflow = api.portal.get_tool('portal_workflow')
        for portal_type, chain in workflow.listChainOverrides():
            if portal_type in ('todo_item', ):
                self.assertEquals(('todo_item_workflow',), chain)

    # jsregistry.xml
    def test_js_registered(self):
        """Test if todoapp.js JavaScript file is registered in
        portal_javascript.
        """
        resources = self.portal.portal_javascripts.getResources()
        ids = [r.getId() for r in resources]

        self.assertIn('++resource++tutorial.todoapp/todoapp.js', ids)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
