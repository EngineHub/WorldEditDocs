Edit Sessions
=============
An ``EditSession`` handles the configuration for getting and placing blocks, entities, and biomes. It sets up the
chain of extents to place blocks properly. It also handles turning on and off reorder mode, fast mode, and buffering.
Every operation will use an ``EditSession`` at some point to ensure that block placement is done properly and quickly.

Edit sessions must be closed once all operations are complete, to ensure that block queues are flushed.
They are not re-usable, and must be re-created for each individually operation.
