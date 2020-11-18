Edit Sessions
=============
An ``EditSession`` handles the configuration for getting and placing blocks, entities, and biomes. It sets up the
chain of extents to place blocks properly. It also handles turning on and off reorder mode, fast mode, and buffering.
Every operation targeting a world will use an ``EditSession`` at some point to ensure that block placement is done properly and quickly.

The easiest way to make a simple ``EditSession`` is using the helper methods on the ``WorldEdit`` class,
``newEditSession(World)`` or ``newEditSession(Actor & Locatable)``. These are shorthands for using the full builder,
available from ``newEditSessionBuilder()``. The builder has all of the options that used to be available from the
``EditSessionFactory``'s various methods, but in a easier-to-read form. If you use the builder, don't forget to call
``build()`` at the end to get an actual ``EditSession``.

.. code-block:: java

    // Getting an edit session for a WorldEdit World
    WorldEdit.getInstance().newEditSession(world)

    // Getting an edit session for a WorldEdit World with a maximum block count
    WorldEdit.getInstance().newEditSessionBuilder().world(world).maxBlocks(1000).build()

Edit sessions must be closed once all operations are complete, to ensure that block queues are flushed.
They are not re-usable, and must be re-created for each individual operation.

A clean way to close a ``EditSession`` is to use the ``try-with-resources`` statement:

.. code-block:: java

   try (EditSession editSession = WorldEdit.getInstance().newEditSession(world)) {
       // use the edit session here ...
   } // it is automatically closed/flushed when the code exits the block

For more information, see `The try-with-resources Statement`_ page from the Java Tutorials.

The Extent Stack
~~~~~~~~~~~~~~~~

The "extent stack" is a term used to describe the many extents that are composed to create an ``EditSession``.
At the very bottom of the stack is the ``World`` that the changes will be committed to. That extent is wrapped in
other extents that all apply various fixes for oddities with Minecraft, and then the first event is posted with a stage
of ``Stage.BEFORE_CHANGE``. The resulting extent is used for ``EditSession.rawSetBlock()``. Then, that extent
is wrapped in some reordering / batching extents, and another event is posted with a stage of ``Stage.BEFORE_REORDER``.
The resulting extent is used for ``EditSession.smartSetBlock()``. Then, that extent is wrapped in change set, masking,
and limiting extents, and a final event is posted with a stage of ``Stage.BEFORE_HISTORY``. The resulting extent is
used for the normal ``EditSession.setBlock()``.

.. _edit-session-event:

Edit Session Event
~~~~~~~~~~~~~~~~~~

The ``EditSessionEvent`` is the way to hook into WorldEdit's changes in an efficient manner. It is fired as a part of
``EditSession`` creation, and allows hooking into the extent stack at various steps as described above. You can
subscribe to this event by registering with WorldEdit's event bus:

.. code-block:: java

    WorldEdit.getInstance().getEventBus().register(new Object() /* [1] */ {
        // Make sure you import WorldEdit's @Subscribe!
        @Subscribe
        public void onEditSessionEvent(EditSessionEvent event) {
            if (event.getStage() == /* the stage you're interested in */) {
                event.setExtent(new MyCustomExtent(event.getExtent()));
            }
        }
    });

    // [1]: You don't need to use an anonymous class, you can also store your method in its own separate class
    //      and construct it here instead.

When creating your own extent class, consider extending ``AbstractDelegateExtent``, which allows you to only override
the methods you're interested in. Don't forget to call the appropriate ``super`` method to actually perform the changes!

.. _The try-with-resources Statement: https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html
