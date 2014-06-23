.. line-block::

    WARNING: If you are reading this on GitHub, DON'T! Read it on ReadTheDocs:
    http://tutorialtodoapp.readthedocs.org/en/latest/chapter_1.html so you
    have working references and proper formatting.


.. index::
   single: Getting Started with Content Types

==========================
Chapter 1: Through-The-Web
==========================

Getting Started with Content Types
==================================

If you don't know what a content type is, don't worry! Sit back, relax, and do
the tutorial! I'll save the mumbo jumbo definitions for another day. In this
first part, we will make a Todo list without touching any code. It won't be
fancy, but it will give you a good idea of how things work in Plone.

The way Plone handles content is a little different than your average
relational database driven framework, so if you don't understand something
right away, sit back, relax, and finish the tutorial.

Generally speaking, content-types are just that: types of content. By default,
in Plone you get the News Item content-type, the Event content-type and so on.
So if you add a content item that is of Event type, you are using the Event
content-type. In our case, we will create a new content-type that will
represent a Todo Item.


Create a New Content Type
-------------------------

First we need to create a new content type to represent an item on our Todo
list. This will be a type with one field, that which needs to be done.

#. Navigate to `site setup` as shown below, or just enter
   ``http://localhost:8080/Plone/@@overview-controlpanel`` in your browser.
   This is where you can configure Plone for happy fun time.

   .. image:: images/site_setup.jpg
      :width: 400px

#. Now comes the fun part. We want to create our own type `Through-The-Web`
   aka. `TTW`. This type will be a Todo Item. Let’s click `Dexterity Content
   Types` (or go directly to
   ``http://localhost:8080/Plone/@@dexterity-types``).

   .. image:: images/plone_configuration_panel.jpg
      :width: 400px

#. Create a Todo List Item by clicking ``Add New Content Type``.

   .. image:: images/add_content_type.jpg
      :width: 400px

#. Fill in the fields as seen below and then click ``Add``.

   .. image:: images/add_todo_content_type.jpg
      :width: 400px

#. Now you will see that there is a new type to play with. There are two
   important things we need to do here: we need to adjust some `behaviors`,
   and add some `fields`. Let’s look at behaviors first.

   .. image:: images/todo_item_behaviors.jpg
      :width: 400px

#. By default, all Plone content-types have `Dublin Core
   <http://en.wikipedia.org/wiki/Dublin_Core>`_ metadata enabled (you may know
   it as ``title`` and ``description``. We don’t need this for our über simple
   Todo list item. Uncheck ``Dublin Core metadata`` and then click ``Save``.

   .. image:: images/behaviors_config.jpg
      :width: 400px

#. Next we need to add some fields. Because this type is so simple, we will
   add just one field, but feel free to go CRAZY. Start by going back to the
   ``Fields`` tab and clicking ``Add new field...``.

   .. image:: images/add_new_field.jpg
      :width: 400px

#. Add a field called ``Todo``, or anything else you want. But! Note that it's
   very important that the `Short Name` field value is ``title``. By using
   this key short name, we make sure that all Todo Items are searchable from
   smart search. Update the field as seen below and click ``Add``.

   .. image:: images/add_todo_field.jpg
      :width: 400px

#. You will see that a new field has been added to your content type. If you
   are feeling adventuresome, click on the settings tab next to the field to
   set other properties, or just see what’s available.

   .. image:: images/final_todo_fields_config.jpg
      :width: 400px


Trying out the Todo Item content-type
-------------------------------------

Now it's time to reap the rewards of all of your effort. Let's put all of our
Todo Items in one particular folder so that we can have collections of items
throughout the site. For this tutorial, we will be putting everything in the
root of the site so it's easy to debug.

#. From the root, add a new folder called ``TODO list``.

   .. image:: images/add_folder_menu.jpg
      :width: 400px

   .. image:: images/save_todo_folder.jpg
      :width: 400px

#. Add a new `Todo Item` to the new `Todo` folder.

   .. image:: images/add_todo_item.jpg
      :width: 400px

   .. image:: images/save_todo_item.jpg
      :width: 400px

#. Celebrate!

   .. image:: images/todo_item.jpg
      :width: 400px

   You may be wondering about earlier, when we asked you to make sure that the
   `short name` for the Todo Item was called ``title``. The time has come to
   let you in on a little secret. Calling the short name either ``title`` or
   ``description`` will automatically add that text to the livesearch menu.
   WHAT?!? I know! When life gives you lemonade, spike it with vodka and enjoy
   liberally! You can now search for your Todo Items in Live Search.

   .. image:: images/live_search_title.jpg
      :width: 400px

But wait a minute... This todo item is marked ``private``, and that doesn't
really make sense. It's a good thing Plone has an easy solution for that. In
the next section, we will go over the basics of that magical, mystical word:
`workflow`.


Getting Started with Workflows
==============================

So what is a workflow? It is a mechanism to control the flow of a
content item through various states in time. Most commonly, and by default in Plone,
you deal with a `publication` workflow. For example: A writer writes up a News
Item and submits it for review. Then the in-house reviewing team goes through
the text and publishes the News Item so it is public for the entire world to
see.

The Todo Item we added in the last section is marked as ``private`` because by
default all new Plone content items are assigned a workflow
called ``simple_publication_workflow``. I know what you are thinking:
simple publication whodie whatie grble gobble??!?! Just like before, let's
bypass trying to explain what that means and just fix it. Relax, enjoy, and
finish the tutorial!

Todo Items really have 2 states that we are interested in: `open` and
`complete`. Let's make that happen.

#. Head over to the ZMI at ``http://localhost:8080/Plone/manage_main``.
#. In the ZMI, open the ``portal_workflow`` tool.

   .. image:: images/manage_portal_workflow.jpg
      :width: 400px

   On this page, we see all content-types in our portal `mapped` to a workflow.
   Our new type, Todo Item, is mapped to ``(Default)``. You can see right below
   that the default is ``Simple Publication Workflow``. This is just too
   complex for our little Todo Item.

   .. image:: images/default_workflow.jpg
      :width: 400px

#. So let's create a new one that suites our needs perfectly! Click the
   ``contents`` tab at the top of the page to get a listing of all the
   available workflows.

   .. image:: images/portal_workflow_contents.jpg
      :width: 400px

   You can poke around here all you like, but the details of each one of these
   workflows are better left to another tutorial. When in doubt, you can always
   come back to these workflows to see examples of how things can be done.
   Onwards and upwards!

#. Let's create a new workflow for our Todo Items and call it
   ``todo_item_workflow``. We will make a new workflow by copying and
   customising one of the workflows that are already there. Duplicate the
   ``one_state_workflow``.

   .. image:: images/copy_workflow.jpg
      :width: 400px

#. Rename the copied workflow to ``todo_item_workflow``.

   .. image:: images/rename_workflow.jpg
      :width: 400px

   .. image:: images/save_rename_workflow.jpg
      :width: 400px

#. You will be spit back out to the workflow contents page. Click the workflow
   to start editing.

   .. image:: images/edit_todo_workflow.jpg
      :width: 400px

#. Let's update the name of the workflow so we don't double take later on.

   .. image:: images/retitle_workflow.jpg
      :width: 400px


#. Workflow is something that takes time to get used to if you have never
   encountered the concept. The best analogy in our case is to a car. The car
   engine has two simple states: `on` and `off`. To transition from on to off
   and vice versa, it needs some action from the driver. The same for our TODO
   items. They have two states: `open` and `completed`. In order to get them
   from `open` to `completed`, the user needs to click something. Don't
   understand yet? Relax, sit back, and finish the tutorial.

   Lets start by adding our base states. We will call them `open` and
   `complete`. From the edit workflow screen, click on the ``States`` tab.

   .. image:: images/workflow_base_view.jpg
      :width: 400px

#. Delete the currently listed state.

   .. image:: images/cleanup_states.jpg
      :width: 400px


#. Add two states with the ids ``open`` and ``completed``.

   .. image:: images/add_open.jpg
      :width: 200px

   .. image:: images/add_completed.jpg
      :width: 400px

#. Next lets add `transitions`. They will take the TODO item from
   `open` to `completed` and vice versa (in case a user wants to revert an item
   back to `open`). Click on the ``Transitions`` tab.

   .. image:: images/transitions_tab.jpg
      :width: 400px

#. Add two transitions: `complete` and `reopen`. When a user `completes` a
   task, it will move into the `completed` state. When a user `reopens` a task,
   it will go back to the `open` state.

   .. image:: images/add_transitions.jpg
      :width: 400px

#. Let's add a few details to these new transitions. Let's start with
   `complete`. Click on ``complete`` to edit the transition.

   .. image:: images/edit_complete.jpg
      :width: 400px

#. First add a title so you remember later what this does. Description is
   optional but adding one will help you keep your thoughts clear and remind
   the `future you` what the `today you` is thinking. The destination state
   should be set to ``completed``. We also want to make sure that only people
   with mega permissions, or the creator of the todo item itself, can change
   the state so we add ``Modify portal content`` to the ``Permissions`` box.

   All this means nothing if we don't give the user a chance to change the
   state. Next to ``Display in actions box``, we can set the title for what
   will be displayed in the workflow drop down box of the item (where
   `Pending`, `Reject`, etc. where earlier). Let's call it ``Complete``. Last
   but not least, we need to add the URL that the action points to. I could
   make this tutorial 100 years long and explain why you have to do this, but
   accept that it has to be done, relax, and follow this formula:

   .. code-block:: bash

       URL = %(content_url)s/content_status_modify?workflow_action=X

   where `X` is the id of the transition. So for this case, in the URL box, you
   will add

   .. code-block:: bash

       %(content_url)s/content_status_modify?workflow_action=complete

   .. image:: images/complete_details.jpg
      :width: 400px

   Double check everything and click ``Save``.

#. If your brain isn't hurting yet it will be soon. Go back to the transitions
   listing.

   .. image:: images/youre_welcome.jpg
      :width: 400px

   .. image:: images/edit_reopen.jpg
      :width: 400px


#. Let's update the `reopen` transition and update in a similar manner. This
   time, the destination state is ``open``, and following the formula above,
   the URL is ``%(content_url)s/content_status_modify?workflow_action=reopen``.

   .. image:: images/save_reopen.jpg
      :width: 400px

#. Now we have 2 states and 2 transitions, but they aren't 100% linked
   together ... yet. Go back to the workflow listing, click the ``States`` tab
   and then click on ``completed`` to edit the state.

   .. image:: images/back_to_workflow.jpg
      :width: 400px

   .. image:: images/edit_completed.jpg
      :width: 400px

#. Add a title, since this is what users see in the top right corner of the
   TODO items, and then check ``reopen`` as a possible transition. This means
   that when a TODO item is completed, it will only allow the user to reopen it
   (and not re-complete it, for example). In the same respect, open the
   ``open`` transition, add a title, and mark ``complete`` as a possible
   transition.

   .. image:: images/save_completed.jpg
      :width: 400px

   .. image:: images/save_open.jpg
      :width: 400px

#. When we create a new TODO item, we need to tell Plone what the first state
   is. Go back to the workflow states listing, and make ``open`` the initial
   state.

   .. image:: images/initial_state.jpg
      :width: 400px

#. And that's it! Almost... Last but not least, we need to assign our new
   workflow to our TODO item type. Go back to the main workflow screen.

   .. image:: images/home_base.jpg
      :width: 400px

#. Instead of mapping to the ``(Default)`` workflow, we are going to map to the
   id of our new workflow, ``todo_item_workflow``, and then click ``Change``.

   If you already have TODO items in your site, you MUST click ``Update
   Security Settings`` to update the workflow for the items. Instead of going
   into gross detail about why this is the case, just sit back, relax, finish
   the tutorial, and remember to click this button any time you make changes
   (yes! you can continue to change and update your workflows!).

   .. image:: images/map_to_workflow.jpg
      :width: 400px

#. Could the time have arrived? Time to try it out? YES! Go to your ``Todo``
   folder and add a new TODO Item. Validate that the workflow works as
   expected. By toggling between the states.

   .. image:: images/works.jpg
      :width: 400px

Congrats! You have now passed `Plone Workflow 101`. Next we will transition
from developing through the web (TTW) to developing on the filesystem.
