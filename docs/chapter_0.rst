.. line-block::

    WARNING: If you are reading this on GitHub, DON'T! Read it on ReadTheDocs:
    http://tutorialtodoapp.readthedocs.org/en/latest/prelude.html so you have
    working references and proper formatting.


.. index::
   single: Tutorial setup

=============
Prerequisites
=============

* You have Git installed and vaguely know how to use it.
* You are working with Python 2.6 or 2.7
* You have already installed (listed names are for Ubuntu/Debian, should be
  similar for your distribution): `python-setuptools`, `python-virtualenv`,
  `zlib1g-dev`, `libxslt1-dev` and `libxml2-dev`.
* For Ubuntu/Debian users it may be worthwhile to install build-essential
  (sudo apt-get install build-essential) to make sure you have necessary
  build tools.
* Sorry Windows users, but you'll have to translate as usual from n*x to
  Windows-ese.

==============
Tutorial Setup
==============

Since this is a tutorial on how to be a develop, there will always be a little
bit of setup. There are many ways that this could be done and integrated with
the Unified Installer, but it is not covered here. It is possible to use this
tutorial in the context of the Unified Installer by just installing the source
skeleton.

#. Using Git, checkout the base Buildout and code for this tutorial. Run
   `bootstrap.py` with Python 2.6 or 2.7, and then run Buildout. There are
   sometimes problems on Mac and Linux with pre-installed versions of Python.
   If you run into issues, please see
   ``http://collective-docs.plone.org/en/latest/getstarted/installation.html``::

    > git clone git://github.com/collective/tutorial.todoapp.git
    > virtualenv --no-site-packages tutorial.todoapp
    > cd tutorial.todoapp
    > git checkout chapter1
    > ./bin/python bootstrap.py --distribute
    > ./bin/buildout

#. Next up, start the Plone instance::

    > ./bin/instance fg

#. Open up your browser and navigate to ``http://localhost:8080/``
#. Click 'Create a New Plone Site'. The default username and password for this
   Buildout is ``admin:admin``.

#. Change the `name` and `id` if you wish, but keep in mind that for this
   tutorial we will assume the name of the site is ``Plone`` and is located at
   ``http://localhost:8080/Plone``.

   .. image:: images/dexterity_extension.jpg
      :width: 400px

#. Under `Add-ons`, make sure to check ``Dexterity Content Types`` and
   ``tutorial.todoapp`` then click ``Create Plone Site``.

   .. image:: images/install_todo.jpg
      :width: 400px

#. There, your Plone site is created and you can continue with the tutorial.

   .. image:: images/welcome_to_plone.jpg
      :width: 400px

Woot! Let's go.


===============
Troubleshooting
===============

Sometimes setting up development environment gives you lemons. There are various
ways to go around that.

In case you don't have correct Python version or your system Python environment
is broken (yes, I'm looking to you OSX), `buildout.python` gives you get out of
jail free card. To install it, see
`https://github.com/collective/buildout.python/blob/master/docs/INSTALL.txt`_.
Then use `buildout.python/python-2.7/bin/python bootstrap.py --distribute` step as
in `Tutorial Setup` section and so on.

If everything fails, it's time to use a virtual machine. See instructions
at `https://github.com/plone/coredev.vagrant#installation`_ to prepare and try
again with `Tutorial Setup` section.
