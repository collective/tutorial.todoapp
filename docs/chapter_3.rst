.. line-block::

    WARNING: If you are reading this on GitHub, DON'T! Read it on ReadTheDocs:
    http://tutorialtodoapp.readthedocs.org/en/latest/chapter_3.html so you
    have working references and proper formatting.


======================
Chapter 3: Custom View
======================

In this chapter you will learn how to add a custom view -- in our case a listing
of Todo Items.

View class
==========

Let's start by adding the view class. Go to `tutorial.todoapp repo on
GitHub <https://github.com/collective/tutorial.todoapp/>`_ and copy over code
from ``src/tutorial/todoapp/browser/todo.py`` to your local computer.

We also need to tell Plone to display this view in the `display` drop-down menu
for Folders so we will later be able to set our view as a default display view
for our Todo folder. Do that by adding the ``Folder.xml`` file to
``src/tutorial/todoapp/profiles/default/types`` folder (get contents of the file
on GitHub in the same path).

View template
=============

Now that we have a class we can also add the template. Go to `tutorial.todoapp
repo on GitHub <https://github.com/collective/tutorial.todoapp/>`_ and copy over
code from ``src/tutorial/todoapp/browser/todo.pt`` to your local computer.

The template uses ZPT syntax, `read more about it here
<http://wiki.zope.org/ZPT/TutorialPart1>`_.

Static resources
================

The template displays different icons for different workflow states of your
Todo Items. We need to add these icons to your package:

    #. Download ``open.png`` and ``completed.png`` from GitHub (they are in
       ``src/tutorial/todoapp/browser/static``) into a new folder on your local
       computer: ``src/tutorial/todoapp/browser/static``.
    #. Tell Zope that this ``static`` folder contains static resources (icons,
       CCS files, JavaScript files, etc.) by adding the following lines to
       ``src/tutorial/todoapp/browser/configure.zcml``:

       .. code-block:: xml

           <!-- Publish static files -->
           <browser:resourceDirectory
               name="tutorial.todoapp"
               directory="static" />

After restarting your Zope server, files in your ``static`` folder will be
available on a standard URL:
``http://localhost:8080/Plone/++resource++tutorial.todoapp/<filename>``


Try it out
==========

TODO: screenshots here!
#. reinstall the product (because XML changed)
#. go to the folder with todo items
#. select 'todo' as default view
#. celebrate!


Tests
=====

Cool, so you have verified that your code works through the browser and it's
time to add tests to make sure your code keeps on working in the future.

This chapter comes with only one test file: ``test_todo_view.py``. Get it from
GitHub, put it in your ``tests`` folder and run tests. Then fiddle around with
it to see what it does.
