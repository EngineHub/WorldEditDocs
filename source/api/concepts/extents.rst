Extents
=======

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
