Registries
==========

Almost everything in Minecraft uses the same format for identifying a particular type, such as ``minecraft:stone``.
This is known as a `namespaced ID <https://minecraft.wiki/w/Resource_location>`_ (see page for details).
WorldEdit keeps some `registries` that allow access to blocks, items, biomes, entities, fluids, and more from the
current Minecraft platform using their ID in a platform-independent way.

These registries are available on most classes named ``*Type``, such as ``BlockType`` and ``ItemType``.
However, it is recommended to use the ``*Types`` classes instead, which either provide potentially-null constants
or a ``get`` method for retrieving types that aren't built-in, such as modded blocks.

.. note::
    The constants on these registries may be ``null`` because the API does not change across Minecraft versions,
    and this means that some blocks won't exist on earlier Minecraft versions, or like in 1.13, were renamed
    from their ID in 1.12 and WorldEdit no longer recognizes the block properly. If you require a block, you should
    wrap the access to the constant in ``Objects.requireNonNull`` or a similar check to properly communicate that
    you do not expect the constant to be missing at runtime.
