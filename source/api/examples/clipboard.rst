Clipboard Examples
==================

.. note::
    This documentation covers the API for using clipboards.
    See :doc:`/usage/clipboard` for in-game usage & explanations of what clipboards are.

Concepts used in these examples: :doc:`../concepts/regions`, :doc:`../concepts/edit-sessions`,
:doc:`../concepts/extents`

Copying
-------
Copying is the most common way to create a clipboard. To do it, you'll need a ``Region``, and a source and target extent,
such as a ``World`` and a ``Clipboard``. In this example we use a ``CuboidRegion`` and the standard ``BlockArrayClipboard``.
Then, all you need to do is pass the parameters to the ``ForwardExtentCopy``, apply configuration (such as calling
``setCopyingEntities(true))`` to copy entities), and call ``Operations.complete``.

.. code-block:: java

    CuboidRegion region = new CuboidRegion(min, max);
    BlockArrayClipboard clipboard = new BlockArrayClipboard(region);

    ForwardExtentCopy forwardExtentCopy = new ForwardExtentCopy(
        world, region, clipboard, region.getMinimumPoint()
    );
    // configure here
    Operations.complete(forwardExtentCopy);

You may want to :ref:`save <Saving>` the clipboard after this. Note that if you are only copying a clipboard to paste it
immediately again, you should skip making the clipboard entirely. Instead, build an ``EditSession`` for the target world and
pass that to ``ForwardExtentCopy`` - it is capable of copying blocks between any two extents,
or even between the same one, and is not limited to clipboards.

Pasting
-------
Pasting is the only way to move blocks from a ``Clipboard`` to another ``Extent``, typically a ``World``.
To paste, you'll need a target ``Extent`` (generally an ``EditSession`` for a ``World``) and a ``Clipboard``. Create a ``ClipboardHolder``
with your clipboard, then get a ``PasteBuilder`` by calling ``createPaste`` with the ``EditSession``.
Call ``.to`` to set the position at which you want to paste (this will be offset by the clipboard offset,
see the clipboard page above for more information). Add any other configuration you want (masks, paste entities,
paste biomes, etc.), and then call ``build()`` to get an operation. Complete the operation, and all the blocks
will be pasted. Note that if you want to rotate the clipboard, you'll need to ``setTransform`` on
the ``ClipboardHolder`` *before* calling ``createPaste``.

Full example:

.. code-block:: java

    try (EditSession editSession = WorldEdit.getInstance().newEditSession(world)) {
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
