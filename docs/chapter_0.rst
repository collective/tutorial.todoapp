.. line-block::

    WARNING: If you are reading this on GitHub, DON'T! Read it on ReadTheDocs:
    http://tutorialtodoapp.readthedocs.org/en/latest/prelude.html so you have
    working references and proper formatting.


.. index::
   single: Tutorial setup

===========
Assumptions
===========

* You have a Plone site running on port 8080 succesfully. If you do not have a Plone site running already, please see ``http://collective-docs.plone.org/en/latest/getstarted/installation.html``. Also see ``http://collective-docs.plone.org/en/latest/getstarted/index.html`` for more information on getting started with Plone development
* You have git  properly installed and vaguely know how to use it
* You are working with Python 2.6 or 2.7, and have already installed setuptools and virtualenv
* Sorry windows users, but you'll have to translate as usual from n*x to Windows-ese
* For Ubuntu/Debian users it may be worthwhile to install build-essential (sudo aptitude install build-essential) to make sure you have necesary build tools

==============
Tutorial Setup
==============

Since this is a tutorial on how to be a develop, there will always be a little bit of setup. There are many ways that this could be done and integrated with the Unified installer, but it is not covered here. It is possible to use this tutorial in the context of the unified installer by just installing the source skeleton. If you feel comfortable completing this tutorial in the context of your own buildout, please feel free to do so.

#. Using git, checkout the base buildout and code for this tutorial. Run bootstrap .py with Python 2.6 or higher, and then run buildout. There are usually problems on mac and linux with the pre-installed versions of python. If you run into issues, please see ``http://collective-docs.plone.org/en/latest/getstarted/installation.html``::

    > git clone git://github.com/collective/tutorial.todoapp.git
    > ./bin/virtualenv --no-site-packages tutorial.todoapp
    > cd tutorial.todoapp
    > git checkout chapter1
    > ./bin/python bootstrap.py --distribute
    > ./bin/buildout

#. Next up, start the plone instance::

    > ./bin/instance fg

#. Open up your browser and navigate to ``http://localhost:8080``
#. Click 'Create a New Plone Site'. The default username and password for this buildout is admin/admin

#. Change the `name` and `id` if you wish, but keep in mind that for this
   tutorial we will assume the name of the site is ``Plone`` and is located at
   ``http://localhost:8080/Plone``.

   .. image:: images/dexterity_extension.jpg
      :width: 400px

#. Under `Add-ons`, make sure to check ``Dexterity Content Types`` and ``tutorial.todoapp``
   then click ``Create Plone Site``.

   .. image:: images/install_todo.jpg
      :width: 400px

#. There, your Plone site is created and you can continue with the tutorial.

   .. image:: images/welcome_to_plone.jpg
      :width: 400px

Woot! Let's go.
