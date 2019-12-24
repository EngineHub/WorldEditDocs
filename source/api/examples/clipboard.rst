Clipboard Examples
==================

.. note::
    This documentation covers the API for using clipboards.
    See :doc:`Clipboard <../../../usage/clipboard>` for in-game usage & explanations of what clipboards are.

Concepts used in these examples: :doc:`Regions <../concepts/regions>`,
:doc:`Edit Sessions <../concepts/edit-sessions>`, :doc:`Extents <../concepts/extents>`

Copying
-------
Copying is the most common way to create a clipboard. To do it, you'll need a ``Region``, a target ``Clipboard``,
and an ``EditSession``. In this example we use a ``CuboidRegion`` and the standard ``BlockArrayClipboard``.
Then, all you need to do is pass the parameters to the ``ForwardExtentCopy``, apply configuration (such as calling
``setCopyingEntities(true))`` to copy entities), and call ``Operations.complete``.

.. code-block:: java

    CuboidRegion region = new CuboidRegion(world, min, max);
    BlockArrayClipboard clipboard = new BlockArrayClipboard(region);

    try (EditSession editSession = WorldEdit.getInstance().getEditSessionFactory().getEditSession(world, -1)) {
        ForwardExtentCopy forwardExtentCopy = new ForwardExtentCopy(
            editSession, region, clipboard, region.getMinimumPoint()
        );
        // configure here
        Operations.complete(forwardExtentCopy);
    }

You may want to :ref:`save <Saving>` the clipboard after this.

Pasting
-------
Pasting is the only way to move blocks from a ``Clipboard`` to another ``Extent``, typically a ``World``.
To paste, you'll need a ``World``, an ``EditSession`` and a ``Clipboard``. Create a ``ClipboardHolder``
with your clipboard, then get a ``PasteBuilder`` by calling ``createPaste`` with the ``EditSession``.
Call ``.to`` to set the position at which you want to paste (this will be offset by the clipboard offset,
see the clipboard page above for more information). Add any other configuration you want (masks, paste entities,
paste biomes, etc.), and then call ``build()`` to get an operation. Complete the operation, and all the blocks
will be pasted.

Full example:

.. code-block:: java

    try (EditSession editSession = WorldEdit.getInstance().getEditSessionFactory().getEditSession(world, -1)) {
        Operation operation = new ClipboardHolder(clipboard)
                .createPaste(editSession)
                .to(BlockVector3.at(x, y, z))
                // configure here
                .build();
        Operations.complete(operation);
    }

You may want to :ref:`load <Loading>` a clipboard before this.

Schematic Examples
==================
This section deals with schematics, which are a related but distinct concept. Schematics
specifically refer to a saved clipboard, not a clipboard in-memory.

.. _saving:

Saving
------
A ``Clipboard`` can be saved to disk very easily. All you need is a ``ClipboardFormat``, a ``Clipboard``, and an
``OutputStream``. Then you can call ``getWriter`` on the format and ``write`` on the writer with
your ``Clipboard``. Here's an example for saving a clipboard to file.

.. code-block:: java

    File file = /* figure out where to save the clipboard */;

    try (ClipboardWriter writer = BuiltInClipboardFormat.SPONGE_SCHEMATIC.getWriter(new FileOutputStream(file))) {
        writer.write(clipboard);
    }

.. _loading:

Loading
-------
Loading a ``Clipboard`` is nearly as simple. You can either force a specific ``ClipboardFormat``, or have WorldEdit
discover the format of the schematic you want to load. The example does the latter. Then you can call ``getReader``
on the format and ``read`` on the reader to get a ``Clipboard`` instance.

.. code-block:: java

    Clipboard clipboard;

    ClipboardFormat format = ClipboardFormats.findByFile(file);
    try (ClipboardReader reader = format.getReader(new FileInputStream(file))) {
        clipboard = reader.read();
    }
    /* use the clipboard here */
