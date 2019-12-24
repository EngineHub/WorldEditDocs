Patterns and Masks
==================

Patterns and masks are the same as described in :doc:`/usage/general/patterns` and :doc:`/usage/general/masks`.
The only difference is that they must be constructed via their respective classes, rather than from formatted strings.

A single block pattern can be represented using a ``BlockStateHolder``, such as ``BlockState`` and ``BaseBlock``.
Other patterns types are fairly obvious from their names, such as ``TypeApplyingPattern`` or ``RandomStatePattern``.
Use your IDE to find subclasses of ``Pattern``.

Masks are a slightly different story. Exact and fuzzy block `state` masks are done using ``BlockMask``, but you can
also mask only over block `type` (``BlockTypeMask``) or only the `properties` (``BlockStateMask``).
There are also some utility masks in the ``Masks`` class. Again, using your IDE to find ``Mask`` subclasses is
recommended.
