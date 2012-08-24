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
kinda sucks, use this tutorial as your skeleton::

    .. code-block:: bash

    ~$ git clone git@github.com:collective/tutorial.todoapp.git
    ~$ cd tutorial.todoapp
    tutorial.todoapp$ git checkout chapter1

What you just did there was `clone` the tutorial.todoapp repository from GitHub
and then moved into the ``chapter1`` branch. This branch contains a bare-bones
skeleton package on top of which you can follow the instructions below.


Exporting configuration
=======================

Exporting Todo Item content-type
--------------------------------

TODO: Liz does her clickety-clickety fun timez screenshots here also!

Exporting todo_item_workflow
----------------------------

TODO: Liz does her clickety-clickety fun timez screenshots here!


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

Good, the next thing to do is to add tests.

