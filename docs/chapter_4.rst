.. line-block::

    WARNING: If you are reading this on GitHub, DON'T! Read it on ReadTheDocs:
    http://tutorialtodoapp.readthedocs.org/en/latest/chapter_3.html so you
    have working references and proper formatting.


======================
Chapter 4: Bling-bling
======================

As a reward for making it all the way to the end, we will help you add some fancy features 
to your project, otherwise known as bling. Unfortunately, bling means having to write JavaScript. Plone comes with jQuery so we can easily integrate. 

The final part of this tutorial will allow users to check and un-check items on their todo list 
without having to load a new page request. Note that by developing the functionality in this 
order, 100% of the functionality of the application remains when javascript is disabled. Win!


AJAX view
=========

Before we add front-end bling, we need some code that can handle the requests coming in. We create
a simple view that will update the object in context to a new state. You can see that we actually
already have a view to handle this is ``src/tutorial/todoapp/browser/todo.py`` called 
WorkflowTransition. Take a look at this class and the comments around the code. There are a 
couple of things to point out specific to this setup:

.. code-block:: python

    grok.context(Item)

Tells us that this view should be called in the context of a Dexterity item. So if you try to go
to this view from the portal root or anywhere in the site out that is not a Dexterity item, it 
will return a 404.

.. code-block:: python

    def render(self):

``render`` is a special function that must be used. It is where all of the code must go when used
with grok directives. This is the main block of code that will be executed.

.. code-block:: python

    transition = self.request.form.get('transition', '')

``self.request`` is set by the base class, and in anything based on BrowserView will have access 
to this variable. All of the GET/POST parameters will be stored in self.request.form.

.. code-block:: python

        self.request.response.setHeader('Content-Type',
                                        'application/json; charset=utf-8')
        return json.dumps(results)

When working with JSON, it's not *required* to set the header content type, but when used with 
certain jQuery calls it is expected to have the header set correctly. If you don't set this, it 
will sometimes work and sometimes not. Get used to it!

Additionally, we return the result serialized as json by default. For making and testing JSON
web service calls, keep in mind that they should do exactly one thing and no more. This makes
it easy to integrate with Javascript and VERY easy to test. For example, look at 
tests/todo_workflow.py to see how easy we can test this view. 

Furthermore, before taking the plunge to wire up JavaScript, go directly to the url and test 
the change. For example, if you have an item at http://localhost:8080/Plone/todo-list/go-to-the-bathroom, 
you can test the view by adding the view name and GET variables to the end of the url.

.. code-block:: bash

    http://localhost:8080/Plone/todo-list/go-to-the-bathroom  + update_workflow?transition=complete =

    http://localhost:8080/Plone/todo-list/go-to-the-bathroom/update_workflow?transition=complete


.. image:: images/ajax_call.jpg
      :width: 800px


For extra clarity: if you are not an expert in python, plone, AND javascript, I highly
recommend integrating bling bling in the following order:
    #. Write base view and [passing] test cases
    #. Test views in browser
    #. Make ajax interactive

Starting with bling will only bring you pain.

Custom JavaScript
=================

Now that we know the view is working, let's add some AJAX handling on the top of it.
Checkout the Javascript file and a JavaScript registry file into your working directory:

.. code-block:: bash

    git checkout master git src/tutorial/todoapp/browser/static/todoapp.js
    git checkout master git src/tutorial/todoapp/profiles/default/jsregistry.xml

``jsregistry.xml`` contains all of the configuration needed to tell Plone how it should register
the Javascript. It has a lot of options that are pretty self explanatory if you think 
like a machine.

.. literalinclude:: ../src/tutorial/todoapp/profiles/default/jsregistry.xml
    :linenos:

Testing
=======
Holy moley you made it! Reinstall the product, Do a hard reload in the web browser and check out
your todo list. The todo items will toggle complete and incomplete.


TODO: switch code to css and show how to register css. This section needs a bit of love still I know
