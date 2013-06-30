# -*- coding: utf-8 -*-
"""Test Todo Item content type."""

from plone import api
from tutorial.todoapp.testing import IntegrationTestCase
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
        """Test completing a todo item."""

        # prepare the request
        self.request.form['transition'] = 'complete'

        # call the @@update_workflow view
        view = api.content.get_view(
            name='update_workflow',
            context=self.todo,
            request=self.request
        )
        response = json.loads(view())

        # assert view response & todo item state
        self.assertEqual(response['success'], True)
        self.assertEqual(response['results']['state'], 'completed')
        self.assertEqual(response['results']['transitions'], ['reopen'])
        self.assertEqual(api.content.get_state(self.todo), 'completed')

    def test_reopen_todo_item_workflow(self):
        """Test reopening a todo item."""

        # programmatically transition the todo item into the Completed state
        api.content.transition(self.todo, transition='complete')

        # prepare the request
        self.request.form['transition'] = 'reopen'

        # call the @@update_workflow view
        view = api.content.get_view(
            name='update_workflow',
            context=self.todo,
            request=self.request
        )
        response = json.loads(view())

        # assert view response & todo item state
        self.assertEqual(response['success'], True)
        self.assertEqual(response['results']['state'], 'open')
        self.assertEqual(response['results']['transitions'], ['complete'])
        self.assertEqual(api.content.get_state(self.todo), 'open')

    def test_invalid_transition(self):
        """Test view response when dealing with a bad workflow transition."""

        # set request to use an invalid transition
        self.request.form['transition'] = 'foobar'

        # call the @@update_workflow view
        view = api.content.get_view(
            name='update_workflow',
            context=self.todo,
            request=self.request
        )
        results = json.loads(view())

        #  view response & todo item state
        self.assertEqual(results['success'], False)
        self.assertEqual(results['results']['state'], 'open')
        self.assertEqual(results['results']['transitions'], ['complete'])
        self.assertEqual(api.content.get_state(self.todo), 'open')


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
