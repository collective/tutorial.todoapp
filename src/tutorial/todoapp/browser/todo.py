# -*- coding: utf-8 -*-
"""A Folder view that lists Todo Items."""

from five import grok
from Products.ATContentTypes.interface import IATFolder
from plone.dexterity.content import Item
import json
from plone import api
from Products.CMFCore.WorkflowCore import WorkflowException


# Search for templates in the current directory.
# Hopefully this line won't be needed in the future as I hope that we can tell
# grok to look in the current dir by default.
grok.templatedir('.')


class Todo(grok.View):
    """A BrowserView to display the Todo listing on a Folder."""

    grok.context(IATFolder)  # type of object on which this View is available
    grok.require('zope2.View')  # what permission is needed for access


class WorkflowTransition(grok.View):
    """
    Change the state of an item. The context is implied by the url.
    Returns state of the object after the transition, and possible
    transitions in that state
    """

    grok.context(Item)
    grok.require('zope2.View')
    grok.name('update_workflow')

    def render(self):
        # the submitted form variables are stored in the request object
        transition = self.request.form.get('transition', '')
        results = {'results': None,
                   'success': False,
                   'message': ''
                   }

        if transition:
            try:
                # set the new state by running a transition
                api.content.transition(self.context, transition=transition)
                results['success'] = True
            except WorkflowException, e:
                # apprently workflow exceptions don't take kindly to
                # being serialized as json...
                results['message'] = "%s" % e

            results['results'] = {
                'state': api.content.get_state(self.context),
                'transitions': self.get_possible_transitions(self.context),
            }

        # set the right header for sending a JSON response
        self.request.response.setHeader('Content-Type',
                                        'application/json; charset=utf-8')
        return json.dumps(results)

    def get_possible_transitions(self, item):
        """
        Return the posible transitions for an item. This should
        eventually get out of this tutorial, since its NASTY.
        """
        from Products.CMFCore.utils import getToolByName
        workflow_tool = getToolByName(self.context, "portal_workflow")
        items = workflow_tool.getTransitionsFor(item)
        return [item['id'] for item in items]
