Clipboard
=========

WorldEdit has a powerful clipboard function that allows you to copy an area, paste it, and even save it to and load it from files. Clipboard contents are currently only cuboids and copying use the region you have selected.

.. contents::
    :local:
    :backlinks: none

Note that like :doc:`history <general/history>`, your current clipboard is stored in your session and thus will be kept for 10 minutes after logging off (of a server).

Also like history, your current clipboard can be cleared with the `/clearclipboard` command.

Copy and cut
~~~~~~~~~~~~

The ``//copy`` command copies your current selection to your session's clipboard, **keeping track of where you are relative to the copy**. The second part of that sentence is very important; if you want to later paste, for example, a bridge so that it is under where you are standing, you must stand in a location above the bridge when you make the copy. This method allows you to easily align your later paste because you can plan ahead a bit; it requires some spatial abilities to master the copying process but you will find it particularly helpful once you get the hang of it.

``//cut`` works just like ``//copy`` except that it also deletes the selected area afterwards. By default, it leaves air, but you can also specify a different block to leave behind.

.. note:: This remembers your **current position relative to the copy**. This is a very important concept to grasp otherwise you will not be able to control where you paste your copy!

Both commands have three additional flags:

* ``-e`` can be specified to also copy/cut entities from the selection
* ``-b`` can be specified to also copy biomes from the selection ("cutting" selections doesn't make sense - some biome needs to be left there)
* ``-m <mask>`` can be used to specify a :doc:`mask <general/masks>` of blocks to copy/cut. Any blocks that do not match will be replaced with air in your clipboard.

Pasting
~~~~~~~

Once you have something in your clipboard, you can paste it to world. The last argument is optional: if you want the copy to paste at the same point that it was copied at, type ``//paste -o``, otherwise the paste will be placed relative to you. **Remember that if you are pasting relatively, it will be relative to where you were when you made the initial copy.** For example, if you were on top of your castle when you copied it, pasting it would result in the castle being pasted under you.

.. figure:: /images/clipboard/copypasta.png

    A primer on how relative positions work for clipboards

Like the copy/cut commands, the paste command also allows the same three flags:

* ``-e`` can be specified to also paste entities, if your clipboard contains any
* ``-b`` can be specified to also paste biomes, if your clipboard contains any
* ``-m <mask>`` can be used to specify a :doc:`mask <general/masks>` of blocks to paste. Blocks that do not match the mask will not be pasted.

In addition, there are some additional flags:

* ``-a`` will not paste air from your clipboard. This is the same as ``-m #existing``. The ``-a`` and ``-m`` flag *can* be combined (or you can just add ``#existing`` to your mask).
* ``-s`` will set your selection to the area you are pasting into.
* ``-n`` will set your selection like ``-s`` does, but will *not* actually paste anything. This can be useful to check where your clipboard will end up before actually pasting.
* ``-o`` will paste the clipboard back to its original origin, as explained above. This will disregard the entire "relative positions".

Rotating
~~~~~~~~

Sometimes you may want to rotate your copy. The ``//rotate <y> [x] [z]`` command currently lets you rotate your copy
around the Y (up-down) axis 90 degrees or at any multiple of 90 degrees. To be accurate, it actually allows you to
revolve your copy around the relative offset that you were at when you originally made the copy. If you wanted to rotate
a copy around its center, you would have had to stand in the middle of the copy when you had made it.

Note that the rotate command can also take an angle to rotate around the X or Z axis, though you must specify 0 for the
axes that you don't use, e.g. for X axis rotation ``//rotate 0 90``, and for Z axis ``//rotate 0 0 90``. These two axes
can be used to make something vertical, horizontal, or vice versa.

.. figure:: /images/clipboard/rotate.png

    Rotating around your relative position

Flipping
~~~~~~~~

The ``//flip [direction]`` command flips the current clipboard across the plane perpendicular to the given direction.
By default this direction will be whichever way you are facing, but you can also specify it explicitly. There are
three planes you can flip across: XY, YZ, and XZ. The mapping used is included below for reference.

.. csv-table::
  :header: Directions, Plane
  :widths: 1, 1

  ``north`` or ``south``, XY
  ``east`` or ``west``, YZ
  ``up`` or ``down``, XZ
   

.. figure:: /images/clipboard/flip.png

    Flipping the clipboard across a plane

Loading and Saving
~~~~~~~~~~~~~~~~~~

WorldEdit can work with "schematic" files to save or load your clipboard to disk.

To save your current clipboard to file, use ``//schem save <filename>``.

To load a saved schematic, use ``//schem load <filename>``.

.. topic:: A note on schematic formats

    Before WorldEdit version 7 (corresponding to Minecraft 1.13), the files were saved with a ".schematic" file extension in a format that was compatible with many other software such as MCEdit, Redstone Simulator, and more. Unfortunately, the format wasn't suited for the new block format Mojang was migrating to, so a new format was devised - named the `Sponge schematic format <https://github.com/SpongePowered/Schematic-Specification>`_, using the extension ".schem".

    Note that WorldEdit can still import old ".schematic" files saved in older versions (or third party programs) through a legacy compatibility layer, but they can no longer be written to.

.. topic:: Relative positions and schematics

    Both the origin of the copy and your offset to the copy are saved with the file so that you can load it back later on and paste the copy at its original location or relative to you as if you had copied it. You should be familiar with how ``//copy`` and ``//paste`` store your relative position.

    Note that third party software which uses the format may not necessarily use relative positions as WorldEdit does, so they may not have that information.

Schematic Management
--------------------

.. topic:: List available schematics

    ::

        //schem list [-dn] [-p <page>]

    The ``-d`` *or* ``-n`` flag may be used to sort by newest/oldest file modification time. The ``-p`` flag will get a specific page number. Note that the output of this command is interactive - the arrows at the bottom will retrieve the previous/next page automatically, and the ``[L]`` "button" on the left will load the schematic.

.. topic:: Deleting schematics

    .. code::

        //schem delete <filename>

.. topic:: Listing available formats

    .. code::

        //schem listformats

    Although the note above only mentions the older "MCEdit" schematic format and the newer "Sponge" schematic format, WorldEdit actually has no limit on how clipboards are stored. Third-party plugins can register new formats with WorldEdit for saving and/or loading.

Schematic Storage
-----------------

Schematics are saved to and loaded from WorldEdit's schematic folder, which is named ``schematics`` by default, but
can be changed in the :doc:`config <../config>`. The folder is not created until you save a schematic in-game.
If you've downloaded a schematic somewhere and want to add it, you can make the folder manually. The folder needs
to be inside WorldEdit's config folder, which is ``plugins/WorldEdit`` on Bukkit/Spigot/Paper, and ``config/worldedit``
on other platforms. This means that **by default** the schematics folder is located at ``plugins/WorldEdit/schematics`` or
``config/worldedit/schematics``.

.. note:: If you want to share schematic folders between servers/installations, or simply want to store them elsewhere, you will have to enable the "allow-symbolic-links" option in the config.

.. tip:: The save and load commands, although they ask for a file name, can take ``folder/file``, in which case a sub-folder will be created in your schematics folder. This can be useful to organize your schematics.
