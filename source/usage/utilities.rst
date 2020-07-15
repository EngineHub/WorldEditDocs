Utilities
=========

WorldEdit provides a handful of utility commands. These are often conveniences for common tasks which would require multiple commands and selections otherwise. All these commands operate on your placement position. By default, this is your player position, but it can be changed to your first selection position using the ``/toggleplace`` command.

.. contents::
    :local:
    :backlinks: none

Editing nearby blocks
~~~~~~~~~~~~~~~~~~~~~

Sometimes you want to set or replace blocks in an area, but don't need a precise selection - you just want to use an area around you.

Removing blocks above and below::

    /removeabove <size> [height]
    /removebelow <size> [depth]

These two commands let you easily remove blocks above or below you. An example usage is to remove those tower blocks people create in order to get to a high point. The size parameter indicates the size of the cuboid to remove. The cuboid's width and length will be ``(size - 1) * 2 + 1``. The center of the cuboid is the block above the one that you are standing on. If you don't specify a height or depth, the commands will extend to the extents of the world.

Removing nearby blocks::

         /removenear <mask> <size>

This command removes nearby blocks of a certain type. The size parameter indicates the size of the cuboid to remove. The cuboid's width and length will be ``(size - 1) * 2 + 1``. The center of the cuboid is the block above the one that you are standing on.

Replacing nearby blocks::

    /replacenear <size> <mask> <pattern>

If you need to quickly replace nearby blocks, this command is a nice shortcut. The size parameter indicates the size of the cuboid to replace. The cuboid's width and length will be ``(size - 1) * 2 + 1``. The center of the cuboid is the block above the one that you are standing on.

Filling pits
~~~~~~~~~~~~

::

    //fill <pattern> <radius> [depth]

The fill command will start at the your placement position and work outward and downward, filling air with the given pattern. Note that it only works straight downward from the starting layer, so while it will fill a pond, it will not fill a cave (that goes "outward" as it goes down).

The fill command will never go upwards from your starting position.

.. figure:: /images/utilities/fill_pond.png

    An irregularly shaped pool filled with ``//fill``. You wouldn't have been able to replace air with water (with ``/replace``) in this situation because the area doesn't fit neatly into a cuboid.

Recursive Fill
--------------

::

    //fillr <pattern> <radius>

Unlike the fill command, the recursive fill command *will* work outwards as it moves down, meaning it can fill caves and other holes that expand into the walls.

Like the fill command, it will not travel upwards.

Draining pools
~~~~~~~~~~~~~~

::

    //drain [-w] <radius>

The drain command can empty a pool of water or lava. It only removes connected blocks from the starting position, so it will not drain non-connected pools even if they are in the radius.

Adding the ``-w`` flag will also un-waterlog blocks, leaving them dry.

.. note:: Some blocks, like kelp and seagrass, despite looking like they are waterlogged, do not actually have a "dry" state. If you're trying to drain an ocean or river with these blocks, use ``//removenear`` (explained above) to remove those blocks first.

Fixing pools
~~~~~~~~~~~~

::

    /fixwater <radius>
    /fixlava <radius>

This command will replace "flowing" versions of lava and water with "stationary" ones within the radius. This was useful for fixing water features that had been partially removed with buckets or blocks broken. Note that since Mojang changed water mechanics relatively recently, ``fixwater`` is much less useful than before.

Simulating snowfall
~~~~~~~~~~~~~~~~~~~

::

     /snow <radius>

Cover snow over the general area! This algorithm will only cover blocks with snow if they should be covered (for example, torch blocks will not be covered). If an area has something above it (like an overhang), snow will not reach it. "Snowfall" is completely vertical.

.. note:: The snow command does not yet build up layers of snow.

.. figure:: /images/utilities/snow.jpg

    Snowfall transforming a landscape

Thawing snow
~~~~~~~~~~~~

::

    /thaw <radius>

This command works exactly in the opposite way as the ``/snow`` command above, removing snow and ice from exposed areas.

Simulating grass growth
~~~~~~~~~~~~~~~~~~~~~~~

::

    /green [-f] <radius>

Cover grass over the general area! This area works horizontally outwards to convert dirt into grass.

Using the ``-f`` flag will also turn coarse dirt into grass as well as regular dirt.

Extinguishing fires
~~~~~~~~~~~~~~~~~~~

::

    /ex [radius]

This is essentially a shortcut ``/removenear fire <radius>``, to allow you to quickly put out fires.

Removing mobs
~~~~~~~~~~~~~

::

    /butcher [-pngabtfl] [radius]

This command removes nearby mobs. If you don't specify a radius, all active mobs in the entire loaded world will be removed. The mobs will not drop their loot. Be aware that even if you kill all mobs, they will come back quickly if there isn't anything else preventing spawning.

.. include:: butcherflags.rst
