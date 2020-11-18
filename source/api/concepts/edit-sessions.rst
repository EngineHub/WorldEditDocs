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

.. _The try-with-resources Statement: https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html
