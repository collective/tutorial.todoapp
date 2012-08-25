.. line-block::

    WARNING: If you are reading this on GitHub, DON'T! Read it on ReadTheDocs:
    http://tutorialtodoapp.readthedocs.org/en/latest/chapter_2.html so you
    have working references and proper formatting.


=============================
Chapter 2: Filesystem package
=============================

Alright! In Chapter 1 you got your content-type and your workflow hooked up and
running. You're now ready for the next step: pushing your changes to a
filesystem-based package and into a version control system.

Now, why would you even want to do that? Here's a couple of reasons:


#. **Tracking of changes**

   The most obvious one: when you store the configuration of your content-type
   and your workflow in a VCS, you can track how they changed over time. It
   useful to be able to look back a few months and see how your files changed.

#. **Distribution to other developers**

   If you are working in a team you have two ways of distributing your work:
   either write up a guide on what needs to be clicked for someone to come to
   the state you are currently at (slow, manual and error-prone) OR you export
   your configuration and the other developer simply imports it (fast,
   consistent).

#. **Tests**

   Last, but the most important one, having your configuration exported to a
   filesystem package allows you to write tests for it. When your test runner
   spins up a Plone site to run tests again, it needs to have the same
   content-type and workflow that you configured TTW. And importing
   configuration is by far the easiest way to give him that.


Package skeleton
================

Let's start by creating a package skeleton. Since writing things up from scratch
kinda sucks, use this tutorial as your skeleton.


Exporting configuration
=======================

Exporting Todo Item content-type
--------------------------------

Navigate back to the dexterity content type panel or go directly to 
``http://localhost:8080/Plone/@@dexterity-types``

Check the TODO item and then click on export type profile to download the 
type. If you don't check anything, it won't do anything and there is currently
no error message so don't be surprised.

   .. image:: images/export_todo.jpg
      :width: 400px

This will start a download to you machine. Navigate to that directory and 
unzip the contents of that directory. Here is an example of what this will 
look like:
  
   .. image:: images/dexterity_export.jpg
      :width: 400px

We need to take types.xml and the types folder, and save it in our base product.
You can use your finder or explorer to drag and drop, or use the command line.
I'll use command line as an example but feel free to improvise. You want to move 
the files into your default product profile. What's a profile? Don't worry about 
it. Sit back, relax, and finish the tutorial. You will move the files into

.. code-block:: bash

    tutorial.todoapp/src/tutorial/todoapp/profiles/default

Anytime you perform some sort of configuration export from Plone to a custom
product, you will put the XML files in the profiles/default folder. Every time 
you make changes to your types, you should re-export and save into the same 
location. Now, when the next person installs the add-on, they wil have the 
type already there!

Exporting todo_item_workflow
----------------------------

Exporting a workflow is very similar to exporting a Dexterity type. It just takes
a little bit more navigating and a trip to the ZMI. To export the workflow, 
navigate to the root of the ZMI by gong to ``http://localhost:8080/Plone/manage_main``.
From there, head into the portal setup tool:

   .. image:: images/enter_portal_setup.jpg
      :width: 400px

WARNING: The following User Interface is not recommended for children under 18. 

In the portal_setup tool, click on the export tab.

   .. image:: images/setup_export.jpg
      :width: 400px

There are a LOT of things that you can export here, but that is for a different 
tutorial. For now, find export item #28 called ``Workflow Tool``, check the box 
to the left. Then scroll all the way to the bottom and ``Export selected steps``.

   .. image:: images/check_workflow.jpg
      :width: 400px

Just like the Dexterity content type, you will want to untar the downloaded 
folder, and move into your default profile folder. 

In that download you should have a file called ``workflows.xml`` and a folder
called ``workflows`` like below. You will move both of them to the default 
profile.

   .. image:: images/export_workflow_example.jpg
      :width: 400px

Place all of these files in your profile at

   .. code-block:: bash

    tutorial.todoapp/src/tutorial/todoapp/profiles/default

And you are done! Congratulations on the birth of your new product!


Tests
=====

Alright, tests! Considered a pain and a nuissance by some but loved by all
who do it. If you want your code to be solid and your site to be stable, tests
are a great way to get there.

The package you have on your filesystem is already configured to give you a
test-runner so you can immediately go and run it -- obviously you have no tests,
but at least you try if your test runner works.

.. code-block:: bash

    tutorial.todoapp$ bin/test
    Total: 0 tests, 0 failures, 0 errors in 0.000 seconds.

Note: you do *NOT* need to stop your Plone instance in order to run tests. They
will peacfully co-exist.

Good, the next thing to do is to add tests. Go to `tutorial.todoapp repo on
GitHub <https://github.com/collective/tutorial.todoapp/>`_
and copy/paste (or download) all files from the ``src/tutorial/todoapp/tests``
folder to your local ``src/tutorial/todoapp/tests`` folder. You can also get 
the tests with git:

.. code-block:: bash
   
   cd src/tutorial/todoapp
   git checkout master tests
   cd tests

In this folder there will be many new files:

- **base.py**

  This module contains code that bootstraps your test environment: start up
  Zope, add a Plone site, install your package, etc. Code in here is mostly
  boilerplate so for now just use it and mind what exactly it does underneath.

- **test_setup.py**

  This module contains tests that check if your package was successfully
  installed and configured. Tests in here are concerned with XML files you have
  in the ``profiles/default`` folder.

- **test_todo_item.py**

  And finally a module that contains tests for your custom content-type.

We will not go into details of what each test does as we believe the test code
and its comments are in themselves informative and we will rather encourage you
to go through all tests, try to understand what they do, maybe change something
and see what happens, etc.

Remember that you run tests with ``bin/test`` and you should get an output that
looks somewhat like this:

.. code-block:: bash

    tutorial.todoapp$ bin/test
    [...snip...]
    Set up tutorial.todoapp.tests.base.TodoAppLayer:Integration in 0.000 seconds.
    Running:

    Ran 11 tests with 0 failures and 0 errors in 9.782 seconds.
    Tearing down left over layers:
    Tear down tutorial.todoapp.tests.base.TodoAppLayer:Integration in 0.000 seconds.
    Tear down tutorial.todoapp.tests.base.TodoAppLayer in 0.004 seconds.
    Tear down plone.app.testing.layers.PloneFixture in 0.164 seconds.
    Tear down plone.testing.z2.Startup in 0.012 seconds.
    Tear down plone.testing.zca.LayerCleanup in 0.004 seconds.
