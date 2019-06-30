Patterns
========

You may have noticed (or if you haven't yet, you soon will) that many WorldEdit :doc:`commands <../../../commands>` take a "pattern" as a parameter. Patterns range from very simple (such as a single block - ``stone``) to very complex. Patterns determine what blocks get set into the world as a command, tool, etc operates.

.. contents::
    :local:
    :backlinks: none


Available Patterns
~~~~~~~~~~~~~~~~~~

.. note:: This list may be incomplete as patterns are added to WorldEdit. In addition, our API allows other plugins to register new patterns, which will not be listed here.

.. tip:: Here's a video detailing some of these patterns which were added in WorldEdit 7: https://www.youtube.com/watch?v=S5wCVMf3SvM

Single Block Pattern
--------------------

The most basic pattern of just a single block. A block is identified by two parts: the `block type <https://minecraft.gamepedia.com/Java_Edition_data_values#IDs>`_, and additional `block states <https://minecraft.gamepedia.com/Block_states>`_. These two links to the Minecraft Wiki, along with WorldEdit's in-built tab-completion for commands, should guide you in specifying the block you want. Additional states are always appended to the type using the syntax ``block_type[state1=value,state2=value,...]``. Note that when states are not specified, or if some are left out, the default values will be used for those states.

.. topic:: Example: Single block patterns

    Setting a selection to stone::

        //set stone

    Setting a selection to a note block with a specific instrument and pitch::

        //set note_block[instrument=chime,note=18]


Random Pattern
--------------

This pattern allows setting random blocks from any number of other patterns. The basic form is as simple as a comma-separated list of patterns, which will be chosen from evenly. You can also specify weights for each pattern with ``<x>%<pattern>``.

.. topic:: Example:: Random Patterns

    Setting a selection to different types of stone, equally distributed::

        //set stone,diorite,andesite,granite

    Setting a selection to mostly red wool, with a small amount of glass (5:1 ratio, see note below)::

        //set 50%red_wool,10%red_stained_glass

.. note::  Despite the percentage sign, weights need not add up to 100. They are cumulative and will be divided by the total. That is, ``5%dirt`` actually means 100% of the blocks will be dirt, while ``5%dirt,15%stone`` means 25% of blocks will be dirt, and 75% will be stone. In other words, weights are relative to each other, not to 100.

.. tip:: You can use any other pattern as one of the choices, not just the single block pattern. Keep reading to see more patterns...

Random State Pattern
--------------------

Prefixing any block type with an asterisk (``*``) will randomly choose between all states for that block for each position.

.. topic:: Example: Random State Pattern

    Setting oak logs facing in random directions::

        //set *oak_log

Clipboard Pattern
-----------------

The ``#clipboard`` pattern will take blocks from your :doc:`clipboard <../clipboard>` in the same arrangement. This makes it easy to build one part of a repeating complicated pattern by hand, and then repeat it over and over. You can also offset the pattern by adding ``@[x,y,z]``.

.. topic:: Example: Using the clipboard pattern

    Replacing :doc:`all existing blocks <masks>` to your clipboard::

        //replace #existing #clipboard

    .. centered::
        Using the clipboard in the first image to replace a hill. Note the repeating layers.    

    |clipboard_pattern|  |clipboard_replace|

    Using an offset to align the clipboard::

        //set #clipboard@[2,0,1]

.. |clipboard_pattern| image:: /images/patterns/clipboard.png
    :width: 30%

.. |clipboard_replace| image:: /images/patterns/clipboard_replace.png
    :width: 45%

Type or State Applying Pattern
------------------------------

This pattern, prefixed by ``^``, lets you set the type or states of a block without modifying everything else. This pattern will, for example, allow you to change a spiral staircase from oak to acacia without having to worry about the stairs facing in different directions and so on. You can either specify a block type (to change block type but not states, where applicable), or any number of states (to only change those states, where applicable).

.. topic:: Example: Type/State Applying Patterns

    Replacing all oak stairs to acacia stairs, while maintaining orientation, etc::

        //replace oak_stairs ^acacia_stairs

    Removing the water from all waterloggable blocks::

        //set ^[waterlogged=false]

    Doubling up all slabs::

         //replace ##slabs ^[type=double]

Block Category Pattern
----------------------

This pattern allows setting random blocks within a block category, often referred to as a "`tag <https://minecraft.gamepedia.com/Tag>`_". Tags allow grouping blocks together under a single name. Minecraft comes with many tags inbuilt (see the link) and also allows creating and modifying tags via data packs. You may already have noticed these tags being used as a :doc:`mask <masks>` in the example above (``##slabs``).

The syntax for this pattern is ``##<tag name>``, which will randomly choose between the default state of all blocks in the category. You can also mix this with the random state pattern (``##*<tag name>``) to use all states, not just the defaults.

.. topic:: Example: Block Category Pattern Usage

    Replacing all existing blocks with rainbow wool::

        //replace #existing ##wool

    Setting the selection to random types of slabs, both top/bottom/double, and waterlogged at random::

        //set ##*slabs

Special Block Data Syntax
~~~~~~~~~~~~~~~~~~~~~~~~~

Some blocks have additional syntax for setting extra information.

Sign Text
---------

You can set text on signs by separating it with a pipe symbol (``|``). Note that if the text has spaces, you must wrap the entire pattern in quotes ``""``.

.. topic:: Example: Setting sign text

    Simple Example::

        //set oak_sign|Line1|Line2

    With spaces and rotation::

        //set "oak_wall_sign[facing=north]|Hello world|Second|Third line"

Player Heads
------------

You can set the skin of a player head by specifying a username after the pipe symbol.

.. topic:: Example: Setting a skin on a head

    .. code::

        //set player_head|dinnerbone

Mob Spawners
------------

You can set the type of mob to be spawned (again via the pipe symbol). Note that the name of the mob must be an `entity ID <https://minecraft.gamepedia.com/Java_Edition_data_values#Entities>`_. Prefixing `minecraft:` is optional, modded mobs must have a namespace.

.. topic:: Example: Creating a squid spawner

    .. code::

        //set spawner|squid