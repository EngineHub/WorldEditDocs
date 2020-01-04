Regions
=======

WorldEdit uses regions to define where an operation works. A ``Region`` is a set of positions, potentially associated
with a ``World``. There is no requirement that a region be fully continuous.

Regions implement ``Iterable<BlockVector3>``, meaning that the best way to get all the points of `any` region is to
use a ``for-each`` loop, e.g. ``for (BlockVector3 point : region)``. In addition to this, there are convenience
methods to retrieve the minimum, maximum, center, area, width, height, length, chunks, and cubic chunks.
You can also easily ``expand()``, ``contract()``, and ``shift()`` regions, which work like the commands of the same
name. Note that these methods `do not` change any blocks.

Creating a region is as simple as calling the appropriate constructor of the region you want. Typically you want a
``CuboidRegion``, but there are other subclasses for each of the selection types in WorldEdit, or you can implement
your own!

Some common region usages are the actor's selection and clipboard bounds.
