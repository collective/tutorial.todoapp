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

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_folder_menu.jpg
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

   You may be wondering about earlier, when we asked you to make sure that the "short name" for the todo item was called "title". The time has come to let you in on a little secret. Calling the short name either "title" or "description" will automatically add that text to the livesearch menu. WHAT?!? I know! When life gives you lemonade, spike it with whisky and enjoy liberally! You can now search for your TODO items in Live Search

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/live_search_title.jpg
      :width: 400px

But wait a minute... This todo item is marked "Private", and that doesn't really make sense. It's a good thing Plone has an easy solution for that. In the next section, we will go over the basics of that magical, mystical word: workflow. 

Part 2: Updating the Workflow
=============================
The TODO Item we added in the last section is marked as private because by default all new Plone content types are assigned a complex publication workflow. I know what you are thinking; Publication whodie whatie grble gobble??!?! Just like before, let's bypass trying to explain what that means and just fix it. Relax, enjoy, and finish the tutorial!

If you aren't interested in workflow, or already know all about this stuff, skip straight to Part 3!

TODO items really have 2 states that we are interested in: incomplete and complete. Let's make that happen.

#. Head over to the ZMI at http://localhost:8080/Plone/manage_main
#. In the ZMI, open the portal_workflow tool

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/manage_portal_workflow.jpg
      :width: 400px

#. On this page, we see all of the types in our portal "mapped" to a workflow. Our new type, "TODO Item", is mapped to "(Default)". You can see right below that the default is "Simple Publication Workflow". This is just too complex for our little TODO Item.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/default_workflow.jpg
      :width: 400px

#. So let's create a new one that suites our needs perfectly! Click the "contents" tab at the top of the page to get a listing of all the available workflows

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/portal_workflow_contents.jpg
      :width: 400px

   You can poke around here all you like, but the details of each one of these workflows is better left to another tutorial. When in doubt, you can always ome back to these workflows to see examples of how things can be done. Onwards and upwards!

#. Let's create a new workflow for our TODO Items and call it "todo_item_workflow" 

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/save_workflow.jpg
      :width: 400px

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_too_workflow.jpg
      :width: 400px

#. You will be spit back out and the workflow contents page. Click the workflow to start editing

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/edit_todo_workflow.jpg
      :width: 400px



#. Workflow is something that takes time to get used to if you have never encoutered the concept. The best analogy in our case is to a car. The car engine has two simple states: on and off. To transition from on to off and vice versa, it needs some action from the driver. The same for our TODO items. They have to states: incomplete and complete. In order to get them from Incomplete to Complete, the user needs to click something. Don't understand yet? Relax, sit back, and finish the tutorial.

   Lets start by adding out base states. We will call them "open" and "complete". From the edit workflow screen, click on the "States" tab.


   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/workflow_base_view.jpg
      :width: 400px

#. Add two states with the ids "open" and "completed".

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_open.jpg
      :width: 200px

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_completed.jpg
      :width: 400px

#. Next lets add the transitions. The transitions will take the TODO item from open to completed and vice versa (in case a user accidentally marks an item as complete. Click on the transitions tab.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/transitions_tab.jpg
      :width: 400px

#. Add two transitions: complete, and reopen. When a user "complete"s a task, it will move into the "completed" state. When a user "reopens" a task, it will go back to the "open" state. 

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/add_transitions.jpg
      :width: 400px

#. Let's add a few details to these new transitions. Let's start with complete. Click on "complete" to edit the transition.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/edit_complete.jpg
      :width: 400px

#. First add a title so you remember later what this does. Description is optional but adding one will help you keep your thoughts clear and remind future you what now you is thinking. The destination state should be set to "completed". We also want to make sure that only people with mega permissions, or the owner itself, can change the state so we add "Modify portal content" to the Permissions box. 

   All this means nothing if we don't give the user a chance to change the state. Next to "Display in actions box", we can set the title for  what will be displayed in the workflow drop down box of the item (where "Pending", "Reject" et al where earlier). Let's call it "Complete". Last but not least, we need to add the url that the action points to. I could make this tutorial 100 years long and explain why you have to do this, but accept that it has to be done, relax, and follow this formula::

   URL = %(content_url)s/content_status_modify?workflow_action=X

   such that X is the id of the transition. Got it? Good.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/complete_details.jpg
      :width: 400px

   Double check everything and click "Save".

#. ZOMG if your brain isn't hurting yet it will be soon. Go back to the transitions listing.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/youre_welcome.jpg
      :width: 400px

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/edit_reopen.jpg
      :width: 400px


#. Let's update the reopen transition and update in a similar manner. This time, the destination state is "open", and following the formula above, the URL is "%(content_url)s/content_status_modify?workflow_action=reopen".

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/save_reopen.jpg
      :width: 400px

#. Now we have 2 states and 2 transitions, but they aren't 100% linked together... yet. Go back to the workflow listing, click the states tab and then and click on "completed" to edit the state.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/back_to_workflow.jpg
      :width: 400px

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/edit_completed.jpg
      :width: 400px

#. Add a title, since this is what users see in the top right corner of the TODO items, and then check "reopen" as a possible transition. This means that when a TODO item is completed, it will only allow the user to reopen it (and not re-complete it, for example). In the same respect, open the open transition, add a title, and mark "complete" as a possible transition.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/save_completed.jpg
      :width: 400px

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/save_open.jpg
      :width: 400px

#. When we create a new TODO item, we need to tell Plone what the first state is. Go back to the workflow states listing, and make "open" the initial state.

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/initial_state.jpg
      :width: 400px

#. And that's it! Almost... Last but not least, we need to assign our new workflow to our TODO item type. Go back to the main workflow screen. 

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/home_base.jpg
      :width: 400px

#. Instead of mapping to the "(Default)" workflow, we are going to map to the id of our new workflow, todo_item_workflow, and then click "Change".

   If you already have TODO items in your site, you MUST click "Update Security Settings" to update the workflow for the items. Instead of going into gross detail about why this is the case, just sit back, relax, finish the tutorial, and remember to click this button any time you make changes (yes! you can continue to change and update your workflows!).

   .. image:: https://raw.github.com/collective/collective.todoapp/master/docs/images/map_to_workflow.jpg
      :width: 400px

#. Could the time have arrived? Time to test? YES! Go to your TODO Items folder and add a new TODO Item. Validate that the workflow works::: XXX: addd screenshot HERE!


Part 3: Redistributing Your Work
================================
