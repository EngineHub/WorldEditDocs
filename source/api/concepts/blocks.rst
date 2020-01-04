Blocks
======

Blocks are broken into two parts, `type` and `state`. These are represented by the ``BlockType`` and
``BlockState`` classes. An example of block type is ``minecraft:oak_log``, and a state would be the
combination of the type ``minecraft:oak_log`` and the `properties` ``[axis=y]``.

You can get a ``BlockState`` from a ``BlockType`` using either ``getDefaultState()`` or providing the
correct property mappings to ``getState(Map)``.

For example, to get the state for ``minecraft:oak_log[axis=y]``

.. code-block:: java

    BlockType oakLog = Objects.requireNonNull(BlockTypes.OAK_LOG);
    BlockState yFacingOakLog = oakLog.getState(ImmutableMap.of(
        oakLog.getProperty("axis"), "y"
    ));
    System.err.println("State: " + yFacingOakLog);


Some blocks include NBT_, and these are represented by the ``BaseBlock`` type.

You can get a ``BaseBlock`` from a ``BlockState`` using ``toBaseBlock(CompoundTag)``.

.. _NBT: https://minecraft.gamepedia.com/NBT_format
