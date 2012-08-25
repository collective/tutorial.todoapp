# -*- coding: utf-8 -*-
"""Test Todo Item content type."""

from tutorial.todoapp.tests.base import IntegrationTestCase
from plone import api
import json

import unittest2 as unittest


class TestWorkflowServices(IntegrationTestCase):
    """Test the Todo Item content type."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.folder = self.portal.folder
        self.request = self.layer['request']
        self.todo = api.content.create(
            container=self.folder,
            type="todo_item",
            title=u"Try Brulé!",
        )

    def test_complete_todo_item(self):
        self.request.form['transition'] = 'complete'
        view = api.content.get_view(
            name='update_workflow',
            context=self.todo,
            request=self.request
        )
        results = json.loads(view())
        self.assertEqual(results['success'], True)
        self.assertEqual(results['results']['state'], 'completed')
        self.assertEqual(results['results']['transitions'], ['reopen'])

    def test_reopen_todo_item_workflow(self):
        api.content.transition(self.todo, transition='complete')

        self.request.form['transition'] = 'reopen'
        view = api.content.get_view(
            name='update_workflow',
            context=self.todo,
            request=self.request
        )
        results = json.loads(view())
        self.assertEqual(results['success'], True)
        self.assertEqual(results['results']['state'], 'open')
        self.assertEqual(results['results']['transitions'], ['complete'])

    def test_nonexistant_workflow(self):
        self.request.form['transition'] = 'foobar'
        view = api.content.get_view(
            name='update_workflow',
            context=self.todo,
            request=self.request
        )
        results = json.loads(view())
        self.assertEqual(results['success'], False)
        self.assertEqual(results['results']['state'], 'open')
        self.assertEqual(results['results']['transitions'], ['complete'])


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
