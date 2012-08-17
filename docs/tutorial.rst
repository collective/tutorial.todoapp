===============
Plone TODO List
===============
It's a fact - Plone has a lot of complicated features. That doesn't mean Plone is hard for everything! This is a simple tutorial that anyone can follow to get a simple TODO list running inside of a Plone application. Would you want to deploy this hearty appication server for just a TODO list? Probably not. You can however learn several simple, fast concepts that will get you most of the way there. Feeling like you don't understand something completely or the terminology is getting to you? Sit back, relax, and finish the tutorial. If in the end things still aren't clear, please give feedback and we'll look at what we could do better.

In this tutorial you will:
* Learn how to create content types using Dexterity 
* Create and apply basic workflows
* Convert customizations to your plone portal which can be consistenly recreated across multiple sites
* Learn about plone.api
* Learn how to create custom listings of your new content types

Assumptions:
* You have Plone running on port 8080 succesfully.
* That's it!

Getting Started with Content Types
------------------------------
If you don't know what a content type is, don't worry! Sit back, relax, and do the tutorial! I'll save the mumbo jumbo definitions for another day. In this first part, we will make a TODO list without touching any code. It won't be fancy, but it will give you a good idea of how things work in Plone. The way that Plone handles content is a little different than your average relational database driven framework, so if you don't understand right away, sit back, relax, and finish the tutorial.

Create a New Plone Site
^^^^^^^^^^^^^^^^^^^^^^^
If you already have a plone site you want to work with, you can skip this part!

To set up a Plone site
#. Log in as a zope administrator, and head over to the ZMI at  http://localhost:8080/manage_main. Click “Add Plone Site”
.. figure:: https://raw.github.com/zupo/collective.todoapp/master/docs/images/create_plone_site.jpg
#. Change the name and id if you wish, but for this tutorial we will assume the name of the site is “Plone” and is located at http://localhost:8080/Plone
#. Under “Add-ons”, make sure to check “Dexterity Content Types” and then click “Create Plone Site"
#. Sit back, relax, and finish the tutorial

TODO: add folder for TODOs

Next we need to create a new content type, which will be our TODO.

#. Navigate to site setup as shown below, or just enter http://localhost:8080/Plone/@@overview-controlpanel . This is where you can configure Plone for happy fun time.
#. Now comes the fun part. We want to create our own type through-the-web (TTW). This type will be a todo item. Let’s click manage our Dexterity Content Types (or go directly to http://localhost:8080/Plone/@@dexterity-types).
#. Create a Todo List Item by clicking “Add New Content Type”
#. Fill in the fields as seen below and then click “Add” 
#. Now you will see that there is a new type to play with. Let’s adjust a few things. Click the name of the new type to edit. There are two important things we need to do here: we need to adjust some behaviors, and add some fields. Let’s look at the behaviors first.By default, all plone types have dublin core metadata enabled (you may know it as “title” and “description”. We don’t need this for our uber simple TODO list item. (Additionally, there is something really weird to start since title and description aren’t displayed but they are actually there...). Uncheck “Dublin Core metadata” and then click save.
#. Next we need to add some fields. Because this type is so simple, we will just add one field but feel free to go CRAZY. Start by clicking “Add new field...”
#. Add a field called TODO (or anything you want). Most important is that the short id is “title”. By using this key short name, we make sure that all todos are searchable from smart search. Update the field as seen below and click add.
#. You will see that a new field has been added to your content type. If you are feeling adventuresome, click on the settings tab next to the field to set other properties, or just see what’s available.
#. Guess what? You are done! Well, with this part anyways. Test our adding your new content type from the home page.

Part 2: Updating the Workflow
=============================
Switch to 1 step, then move on to complicated schtuff

Part 3: Redistributing Your Work
================================
