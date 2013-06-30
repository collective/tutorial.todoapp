# -*- coding: utf-8 -*-
"""Test Todo Item content type."""

from plone import api
from tutorial.todoapp.testing import IntegrationTestCase

import unittest2 as unittest


class TestRequests(IntegrationTestCase):
    """Test the Todo Item content type."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.folder = self.portal.folder

    def test_add_todo_item(self):
        """Test that we can add a Todo Item."""
        api.content.create(
            container=self.folder,
            type="todo_item",
            title=u"Try Brulé!",
        )
        self.assertEquals(self.folder['try-brule'].title, u'Try Brulé!')


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
