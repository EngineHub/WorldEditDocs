Edit Sessions
=============
An ``EditSession`` handles the configuration for getting and placing blocks, entities, and biomes. It sets up the
chain of extents to place blocks properly. It also handles turning on and off reorder mode, fast mode, and buffering.
Every operation targeting a world will use an ``EditSession`` at some point to ensure that block placement is done properly and quickly.

Edit sessions must be closed once all operations are complete, to ensure that block queues are flushed.
They are not re-usable, and must be re-created for each individual operation.

A clean way to close a ``EditSession`` is to use the ``try-with-resources`` statement:

.. code-block:: java

   try (EditSession editSession = WorldEdit.getInstance().getEditSessionFactory().getEditSession(world, -1)) {
       // use the edit session here ...
   } // it is automatically closed/flushed when the code exits the block

For more information, see `The try-with-resources Statement`_ page from the Java Tutorials.

.. _The try-with-resources Statement: https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html
