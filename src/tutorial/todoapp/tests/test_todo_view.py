# -*- coding: utf-8 -*-
"""Test @@todo BrowserView."""

from DateTime import DateTime
from plone import api
from tutorial.todoapp.testing import IntegrationTestCase

import unittest2 as unittest


class TestView(IntegrationTestCase):
    """Test the @@todo BrowserView."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.folder = self.portal.folder

        # Set @@todo as default display view for folder
        self.folder.setLayout("todo")

        # get the view
        self.view = api.content.get_view(
            name='todo',
            context=self.folder,
            request=self.request
        )

    def test_no_todo_items(self):
        """Test HTML output when there are no Todo Items."""
        output = self.view()
        self.assertIn('No Todo Items added yet, add some!', output)
        self.assertNotIn('<table class="listing"', output)

    def test_listing_table(self):
        """Test HTML listing table output."""

        # create a todo item
        api.content.create(
            container=self.folder,
            type="todo_item",
            title=u"Try Brulé!",
        )

        # set the modification date to a known value so we can test its
        # presence in the view output
        date = DateTime('2012/08/20')
        self.folder['try-brule'].setModificationDate(date)
        self.folder['try-brule'].reindexObject(idxs=['modified'])

        # get view output
        output = self.view()

        # check that the 'no items found' msg is not shown
        self.assertNotIn('No Todo Items added yet, add some!', output)

        # clickable title
        self.assertIn('href="http://nohost/plone/folder/try-brule"', output)
        self.assertIn(u'>Try Brulé!</a>', output)

        # workflow state
        self.assertIn('<td class="todo-visual-status open">', output)

        # modification date
        self.assertIn('todo-modified">Aug 20, 2012 12:00 AM</td>', output)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
