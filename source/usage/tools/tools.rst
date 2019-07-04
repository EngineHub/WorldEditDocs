Tools
=====

Sometimes, running commands over and over is too tedious for some tasks. WorldEdit comes with a wide variety of tools which can be bound to an item and will activate upon clicking on a block. Most tools activate on right-click, while some also have actions for left-clicks. Some tools, including all "brush"-style tools, can be used at a distance, and will act as if you clicked the block you are looking at, even from far away.

To use a tool, hold an item in your hand, then type that tool's command. You will get a message that the tool was bound to that item. Now, every time you activate the tool (by clicking with the item in your hand), that tool will perform its action. **To unbind a tool, hold the item and use the** ``/none`` **command.**

.. tip:: 

    The selection wand (default: wooden axe) and navigation wand (default: compass) are technically tools. They are described on the :doc:`selections <regions/selections>` and :doc:`navigation <navigation>` pages respectively. You can bind and unbind them just as any other tool.

.. contents::
    :local:
    :backlinks: none
    :depth: 2

Tool Listing
~~~~~~~~~~~~

Tree generation tool
--------------------

::

    /tree [type]

This tool will generate a tree of the chosen type when you right click a block. Note that it uses Minecraft's tree generator, and has the same limitations - it will not generate trees on unplantable blocks, or through solid blocks above (unless the tree would normally be able to gross there).

Floating tree remover
---------------------

::

    /deltree

Have players who chop down trees half-way and leave floating tree tops everywhere? This tool, upon right-clicking a floating leaf or log block (or mushroom block), will remove all connected floating tree blocks. This tool will not operate on trees that are still connected to something (such as the ground).

Block replacer tool
-------------------

::

    /repl <pattern>

This tool will replace the right-clicked block with a block from your pattern. You can also left-click a block to replace your current pattern with the left-clicked block.

Long range building tool
------------------------

::

    /lrbuild <leftclick pattern> <rightclick pattern>

This tool allows you to place and destroy blocks at a distance. Just aim and click. Blocks are placed as if you right clicked the block. If you set one of the blocks to air, it will instead delete the block you are targeting.

Long range wand
---------------

::

    /farwand
    
This tool works just like the normal selection wand - but at any distance. Instead of being ``//pos1`` and ``//pos2``, it's ``//hpos1`` and ``//hpos2``.

Cycler Tool
-----------

::

    /cycler

This tool can be used to cycle a block's states. Left-clicking will choose which property to cycle, and right-clicking will cycle the available values of that property. This is useful for example, to rotate individual blocks in place.

Query Tool
----------

::

    /info

The query tool will show information about the right-clicked block. It will show the coordinates, the block type, states, light level (emitted/above), and the internal id (if available).

Flood fill tool
---------------

::

    /floodfill <pattern> <range>

The flood fill tool will, starting at the right-clicked block, change it and all connected blocks of the same type (within the given range) to the specified pattern.

Super-pickaxes
~~~~~~~~~~~~~~

Super-pickaxes are slightly different than other tools. Instead of being bound to a single item, they are just toggled on or off with their commands. When on, left-clicking with *any* pickaxe in your hand will trigger the superpick. Unlike normal tools, they are toggled off with ``//``.

Single Superpick
----------------

::

    //
    /sp single

This super-pickaxe allows you to instantly break blocks. That may seem redundant, but it predates creative mode (creative mode was removed before alpha and wasn't re-added until Beta 1.8). It also will drop the blocks you break as items (:doc:`configurably <../../config>`), which creative mode does not do.

Area Superpick
--------------

::

    /sp area <radius>

This super-pickaxe will break all blocks matching the same type as the initially clicked block within the radius. Like the single mode superpick, it can be configured to drop items.

Recursive Superpick
-------------------

::

    /sp recur <radius>
    
This super-pickaxe also breaks all blocks matching the same type as the initially clicked block within the radius, but only those that are connected (via matching blocks) to the original. Think of this as a "vein miner" mode.

Brushes
~~~~~~~

Unlike the above tools, which are mostly for utility, another group of tools, known as brushes, are mainly designed for painting and building quickly from afar.

They can be found on the :doc:`brush page <brushes>`.