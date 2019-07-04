Masks
=====

Masks, alongside :doc:`patterns <patterns>`, are commonly used in WorldEdit commands. Unlike patterns, masks determine *which* blocks will be affected by commands, brushes, and so on.

Aside from commands that take a mask as a parameter (such as ``//replace [mask] <pattern>``), you can also apply masks to individual :doc:`brushes <../tools/brushes>` by using the ``/mask`` command while holding the brush, or you can apply a mask to all your WorldEdit actions globally with ``//gmask``.

.. note:: Masks applied through different means will stack with each other. If you set your global mask with ``//gmask dirt``, and then set a brush mask with ``/mask stone``, that brush will not be able to modify any blocks at all! This is because the combined mask will only match blocks which are both stone *and* dirt!

.. tip:: You can clear your global mask by using ``//gmask`` again without arguments.

.. contents::
    :local:
    :backlinks: none

Combining Masks
~~~~~~~~~~~~~~~

To get a mask which matches the *intersection* of multiple masks, use a space to separate them. The intersection will match when *all* of the given masks match.

.. topic:: Example: Combining Masks

    Replacing surface stone with dirt using a mask intersection::

        //replace "stone <air" dirt

    Setting a mask which restricts the current brush to modifying air blocks in your selection::

        /mask "air #sel"

Available Patterns
~~~~~~~~~~~~~~~~~~

Block Mask
----------

The simplest of masks, the block mask matches one or more blocks or block states. Just like the :doc:`single block pattern <patterns>`, you can specify either a block type alone, or a block type with any number of states specified. Unlike the pattern, masks will *not* use default values for unspecified block states - they will "fuzzy" match any value of the unspecified state(s).

To match more than one block, separate each with a comma.

.. topic:: Example: Using the block mask

    Removing all oak fences from your selection::

        //replace oak_fence air

    Removing all oak fences that are attached on the east side, and oak fence gates::

        //replace oak_fence[east=true],oak_fence_gate air

Mask Negation
-------------

The ``!`` symbol can be used to negate everything that comes after it. That is, it matches anything *not* matched by a different mask. Any other mask can follow this.

.. topic:: Example: Negating a mask

    Replace any block that isn't dirt, stone, or grass with stone::

        //replace !dirt,stone,grass_block stone

Existing Block Mask
-------------------

The mask ``#existing`` will match any blocks that aren't air. Note that this isn't the same as `!air`, since the game actually has multiple types or air that it uses in some cases.

Solid Block Mask
----------------

The mask ``#solid`` will match any blocks that are considered "solid". That is - blocks that restrict entities (such as players) from moving through them.

Offset Mask
-----------

Using ``>`` (overlay) or ``<`` (underlay) preceding another mask will match blocks that are above or below the other mask, respectively.

.. topic:: Example: Offset masks

    Creating a layer of slabs above planks in your selection::

        //replace >##planks smooth_stone_slab

Region Masks
------------

While it doesn't make sense for commands like replace, setting a region mask can be very useful for using brushes inside a limited area. For example, if you want to brush some dirt around the base of your wall, you can select the wall, and then negate a region mask so that the dirt doesn't affect the wall (but still affects the ground around it).

The first type of region mask is ``#region`` (aliases: ``#sel``, ``#selection``), which will make a copy of your region at the time you run the command and use that as the mask.

The second type of region mask is ``#dregion`` (d for dynamic, also ``#dsel``, ``#dselection``) which will always stay updated with your current selection.

Block Category Mask
-------------------

Block categories, or `tags <https://minecraft.gamepedia.com/Tag>`_ can also be used as masks. A category mask will match any block that is in that category. Just like the pattern, the syntax is `##<tag>`.

.. topic:: Example: Block Category Masks

   Replacing all carpets with a layer of snow::

       //replace ##carpets snow

Noise Mask
----------

The noise mask can create random noise. Specifying ``%<percent>`` will match the given percentage of blocks. Unlike the weighted patterns, ``%50`` is actually 50% of blocks.

Block State Mask
----------------

Like the block mask, this mask matches block states. Unlike the block mask, you don't need to specify a block type. This means you can match any block that has a property in a given value.

The state mask has two modes, lenient and strict. In lenient mode (``^[state=value,...]``, it will match any block that has the given block states equal the given value, *or* any block that does not even have those properties. In strict mode (``^=[state=value,...]``), it will *only* match blocks that have the block states equal to that value.

.. topic:: Example: Using the block state mask

    Removing all closed door, gates, and trapdoors::

        //replace ^=[open=false] air

Expression Mask
---------------

This mask can evaluate a mathematical expression upon each block. The mask starts with ``=`` and then must have an :doc:`expression <../other/expressions>` which can use the variables ``x``, ``y``, and ``z``. The mask will match if the expression returns a positive value.

.. topic:: Example: Expression masks

    Only edit blocks below a certain y-level::

        //gmask =y<64

    Only edit blocks two blocks below air::

        //gmask =queryRel(0,-2,0,0,0)

Biome Mask
----------

The biome mask matches blocks in columns with the given biome. It's syntax is ``$<biome id>``. The biome ID must be the `namespaced id <https://minecraft.gamepedia.com/Java_Edition_data_values#Biomes>`_, with `minecraft:` being optional for vanilla biomes, and mod ids being required for mod-added biomes.
