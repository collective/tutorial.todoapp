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

To set up a Plone site:

#. Log in as a zope administrator, and head over to the ZMI at  http://localhost:8080/manage_main. Click “Add Plone Site”

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_plone_site.jpg
      :width: 400px

#. Change the name and id if you wish, but for this tutorial we will assume the name of the site is “Plone” and is located at http://localhost:8080/Plone

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/dexterity_extension.jpg
      :width: 400px

#. Under “Add-ons”, make sure to check “Dexterity Content Types” and then click “Create Plone Site"

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/create_plone_site.jpg
      :width: 400px

#. Sit back, relax, and finish the tutorial

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/welcome_to_plone.jpg
      :width: 400px

TODO: add folder for TODOs


Create a New Content Type
^^^^^^^^^^^^^^^^^^^^^^^^^
Next we need to create a new content type, which will be our TODO.

#. Navigate to site setup as shown below, or just enter http://localhost:8080/Plone/@@overview-controlpanel . This is where you can configure Plone for happy fun time.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/site_setup.jpg
      :width: 400px

#. Now comes the fun part. We want to create our own type "through-the-web", aka TTW. This type will be a todo item. Let’s click manage our Dexterity Content Types (or go directly to http://localhost:8080/Plone/@@dexterity-types).

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/plone_configuration_panel.jpg
      :width: 400px

#. Create a Todo List Item by clicking “Add New Content Type”

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_content_type.jpg
      :width: 400px

#. Fill in the fields as seen below and then click “Add” 

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_todo_content_type.jpg
      :width: 400px

#. Now you will see that there is a new type to play with. Let’s adjust a few things. Click the name of the new type to edit. 

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/edit_todo_item.jpg
      :width: 400px

#. There are two important things we need to do here: we need to adjust some behaviors, and add some fields. Let’s look at the behaviors first.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/todo_item_behaviors.jpg
      :width: 400px

#. By default, all plone types have dublin core metadata enabled (you may know it as “title” and “description”. We don’t need this for our uber simple TODO list item. (Additionally, there is something really weird to start since title and description aren’t displayed but they are actually there...). Uncheck “Dublin Core metadata” and then click save.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/behaviors_config.jpg
      :width: 400px

#. Next we need to add some fields. Because this type is so simple, we will just add one field but feel free to go CRAZY. Start by clicking “Add new field...”

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_new_field.jpg
      :width: 400px

#. Add a field called TODO (or anything you want). Most important is that the short id is “title”. By using this key short name, we make sure that all todos are searchable from smart search. Update the field as seen below and click add.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_todo_field.jpg
      :width: 400px

#. You will see that a new field has been added to your content type. If you are feeling adventuresome, click on the settings tab next to the field to set other properties, or just see what’s available.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/final_todo_fields_config.jpg
      :width: 400px

Testing and INtegrating the TODO Item Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Now it's time to reap the rewards of all of your effort. Let's put all of our TODO items in one particular folder so that we can have collections of items throughout the site. For this tutorial, we will be putting everything in the root of the site so it's easy to debug.

#. From the root, add a new folder called TODO.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_forlder_menu.jpg
      :width: 400px

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/save_todo_folder.jpg
      :width: 400px

#. Add a new todo item to the new TODO list folder

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_todo_item.jpg
      :width: 400px

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/save_todo_item.jpg
      :width: 400px

#. Celebrate! 
      
   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/todo_item.jpg
      :width: 400px

But wait a minute... This todo item is marked "Private", and that doesn't really make sense. It's a good thing Plone has an easy solution for that. In the next section, we will go over the basics of that magical, mystical word: workflow. 

Part 2: Updating the Workflow
=============================


Switch to 1 step, then move on to complicated schtuff

Part 3: Redistributing Your Work
================================
