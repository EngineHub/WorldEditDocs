Navigation
==========

You may often find yourself in need of getting to places in order to do your work better. The following commands deal with that issue.

.. contents::
    :local:
    :backlinks: none

The Navigation Wand
~~~~~~~~~~~~~~~~~~~

WorldEdit gives you access to a navigation wand, a :doc:`tool <tools/tools>` that is by default bound to the compass (though you can :doc:`configure <../config>` this).

At any time, you can left click while holding a compass to jump to the block you are looking at (as with the jumpto command, described below). You can also right click with the compass to pass through walls (as with the thru command, described below).

Freeing yourself
~~~~~~~~~~~~~~~~

    ::

        /unstuck
        /!

This will get you out of a block if you somehow got embedded inside. It moves you to the top-most free position, choosing to do nothing if you were not stuck to begin with. The short alias (``/!``) can often be useful if you aren't in creative mode and find yourself suffocating after pasting or generating something on top of yourself.

Jumping to the block in sight
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    /jumpto

This command sends you to the top of the block that you are looking at. If that block is a vertical wall, you will be placed on top of the cliff at the very edge. 

Passing through walls
~~~~~~~~~~~~~~~~~~~~~

::

    /thru

This command sends you through a wall in the direction you are looking. Just look into a wall and use the command. Make sure that you do not look downwards into a wall because it will attempt to go through the ground. This command limits the thickness of the wall to a reasonable amount. 

Ascending and descending
~~~~~~~~~~~~~~~~~~~~~~~~

::

    /ascend [levels]
    /descend [levels]

These two commands allow you to pass through the ceiling above or floor below you. For example, if you were inside a home, you would move to the roof of the building if you used /ascend. You can also optionally provide a number of levels to ascend or descend. For example, if you were in a skyscraper on the bottom floor, and used ``/ascend 2``, you'd be on the 3rd floor.

Ascending to the ceiling
~~~~~~~~~~~~~~~~~~~~~~~~

::

    /ceil [clearance]

This command brings you up to the ceiling of the current room that you are in. If you provide no clearance parameter to use, you will be right up to the ceiling. If you do specify a clearance, the space above your head will be larger. A glass block is placed under your feet in order to support you. You must remove the block manually.

Ascending up an arbitrary distance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    /up <distance>

This will move you up a certain number of blocks. You cannot pass through walls with this command and a glass block will be placed at your feet to support you. The glass block has to be removed manually after you are done. 
