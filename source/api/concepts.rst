API Concepts
============

WorldEdit uses some simple concepts to create flexible operations.

Blocks
------
Blocks are broken into two parts, `type` and `state`. These are represented by the ``BlockType`` and
``BlockState`` classes. An example of block type is ``minecraft:stone``, and a state would be the
combination of the type ``minecraft:stone`` and the `properties` ``[stone_type=granite]``.

You can get a ``BlockState`` from a ``BlockType`` using either ``getDefaultState()`` or providing the
correct property mappings to ``getState(Map)``.

For example, to get the state for ``minecraft:stone[stone_type=granite]``

.. code-block:: java

    BlockType stone = Objects.requireNonNull(BlockTypes.STONE);
    BlockState granite = stone.getState(ImmutableMap.of(
        stone.getProperty("stone_type"), "granite"
    ));
    System.err.println("State: " + granite);


Some blocks include NBT_, and these are represented by the ``BaseBlock`` type.

You can get a ``BaseBlock`` from a ``BlockState`` using ``toBaseBlock(CompoundTag)``.

.. _NBT: https://minecraft.gamepedia.com/NBT_format


Patterns and Masks
------------------
Patterns and masks are the same as described in :doc:`Patterns <../usage/general/patterns>` and
:doc:`Masks <../usage/general/masks>`. The only difference is that they must be constructed via
their respective classes, rather than from formatted strings.

A single block pattern can be represented using a ``BlockStateHolder``, such as ``BlockState`` and ``BaseBlock``.
Other patterns types are fairly obvious from their names, such as ``TypeApplyingPattern`` or ``RandomStatePattern``.
Use your IDE to find subclasses of ``Pattern``.

Masks are a slightly different story. Exact and fuzzy block `state` masks are done using ``BlockMask``, but you can
also mask only over block `type` (``BlockTypeMask``) or only the `properties` (``BlockStateMask``).
There are also some utility masks in the ``Masks`` class. Again, using your IDE to find ``Mask`` subclasses is
recommended.

Extents
-------
Extents form the backbone of WorldEdit's block manipulation. Extents are generally split into three categories:
input, output, and both. Although extents provide and receive block and biome information, they are not always
associated with a world / dimension.

Input extents are responsible for providing block and biome information for a given location. They do not provide
a way to set blocks.

Output extents are responsible for receiving block and biome information for a given location. They do not provide
a way to get blocks.

Most or all extents in WorldEdit implement both ``*Extent`` interfaces, typically through the ``Extent`` interface.
``Extent`` instances also provide a minimum and maximum point, as well as entity manipulation methods.

Some examples of extents are worlds and clipboards. Many block placement features in WorldEdit - such as fast and
reorder mode - are implemented using ``AbstractDelegateExtent`` and hooking into ``setBlock``.
