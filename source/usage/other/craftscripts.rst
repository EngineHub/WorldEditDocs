CraftScripts
============

.. highlight:: javascript

CraftScripts allow you to write scripts with as little overhead as possible: no compiling WorldEdit, no setting up a plugins configuration file, etc. CraftScripts are written in JavaScript.

The advantages of writing CraftScripts with WorldEdit are:

* Hook right into WorldEdit's undo/redo system
* Use WorldEdit's block place prioritization
* Accept WorldEdit's powerful block type syntax (``//set sign[facing=north]``)
* Get the region selected by the user

.. note:: A basic understanding of both JavaScript and Java is recommended.

Requirements
~~~~~~~~~~~~

Before you start using CraftScripts, you'll have to install the `Rhino JavaScript engine <https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino>`_. A direct link to the download is `here <https://github.com/mozilla/rhino/releases/download/Rhino1_7_12_Release/rhino-1.7.12.zip>`_. Open the zip file, and extract ``js.jar``. Note that if you download a newer version than the recommended one, the ``.jar`` file may have a different name. Move ``js.jar`` to the ``plugins/`` or ``plugins/WorldEdit`` directory (on Bukkit) or the ``mods`` directory (other platforms).

Using CraftScripts
~~~~~~~~~~~~~~~~~~

Once you have the JS engine installed, drop your CraftScript ``.js`` files in the ``craftscripts`` directory (in the WorldEdit config directory - either ``plugins/WorldEdit`` or ``config/WorldEdit`` depending on platform).

To run a CraftScript

.. code-block:: text

    /cs <filename> <args>
    /.s <args>

The ``/cs`` command will run the CraftScript with the given filename (``.js`` can be left out). Each CraftScript may have its own arguments. The ``/.s`` command will re-run your last used CraftScript.

Writing CraftScripts
~~~~~~~~~~~~~~~~~~~~

Introduction
------------

Scripts have the following three variables in their global namespace:

* ``context`` is an instance of `CraftScriptContext <https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/scripting/CraftScriptContext.java>`_.
* ``player`` is the player who invoked the script, an instance of `Player <https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/entity/Player.java>`_.
* ``argv`` is a Java array strings, which are the arguments used upon invoking the scripts

In addition to these globals, if you wish to import any WorldEdit or Java packages or classes you must use the function ``importPackage`` or ``importClass``, respectively:

.. topic:: Example: Importing packages and classes

    ::

        // Equivalent to `import com.sk89q.worldedit.world.*`
        importPackage(Packages.com.sk89q.worldedit.world);
        // Equivalent to `import com.sk89q.worldedit.world.block.*`
        importPackage(Packages.com.sk89q.worldedit.world.block);
        // Equivalent to `import java.util.*`
        importPackage(java.util)

        // Equivalent to `import com.sk89q.worldedit.math.BlockVector3`
        importClass(Packages.com.sk89q.worldedit.math.BlockVector3);
        // Equivalent to `import java.util.ArrayList`
        importClass(java.util.ArrayList)

Warning: unlike Java, Rhino JavaScript does not implicitly import ``java.lang.*``, and doing so explicitly is not permitted.

Working with Blocks
-------------------

All block editing in WorldEdit is done through an EditSession. This object handles history and block placement order automatically. To get an edit session for your own script, use:

::

    var editSession = context.remember();

This returns a new instance of `EditSession <https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/EditSession.java>`_. To set blocks, you will need to provide a `BlockVector3 <https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/math/BlockVector3.java>`_ and then either a `BlockState <https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/world/block/BlockState.java>`_ or a `BaseBlock <https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/world/block/BaseBlock.java>`_ to the ``EditSession``.


.. topic:: Example: Setting white wool at (431, 63, -41)

    ::

        importClass(Packages.com.sk89q.worldedit.world.block.BlockTypes);
        importClass(Packages.com.sk89q.worldedit.math.BlockVector3);

        var editSession = context.remember();
        editSession.setBlock(BlockVector3.at(431, 63, -41), BlockTypes.WHITE_WOOL.getDefaultState());



To get blocks, use the function ``EditSession#getBlock``, which accepts a ``BlockVector3`` and returns an instance of ``BlockState``.

.. topic:: Example: Replacing white wool at (431, 63, -41) with black wool

    ::

        importClass(Packages.com.sk89q.worldedit.world.block.BlockTypes);
        importClass(Packages.com.sk89q.worldedit.math.BlockVector3);

        var editSession = context.remember();
        var block = BlockVector3.at(431, 63, -41);
        if (editSession.getBlock(block).getBlockType().equals(BlockTypes.WHITE_WOOL)) {
          editSession.setBlock(block, BlockTypes.BLACK_WOOL.getDefaultState());
        }

To get the player's selected region, use:

::

    var region = context.getSession().getRegionSelector(player.getWorld()).getRegion();

This returns an instance of `Region <https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/regions/Region.java>`_.

Processing Arguments
--------------------

Arguments are passed in under the ``argv`` variable. ``argv`` is a JavaScript array, and the first element of the array is the filename of your script (which may or may not have the file extension). If you need to check whether the right number of arguments was provided by the player, you can use ``CraftScriptContext#checkArgs``.

The ``CraftScriptContext`` can do some basic argument parsing with ``CraftScriptContext#getBlock``. You can also hook directly into WorldEdit's parsers via ``WorldEdit.getInstance().getPatternFactory()`` and ``.getMaskFactory()``.

.. topic:: Example: Checking arguments

    ::

        // This script accepts at least 1 and at most 3 required arguments, separated by a space.
        // Use -1 as the second argument for no maximum limit.
        context.checkArgs(1, 3, "<block> [width] [height]");
        var block = context.getBlock(argv[1]);
        var width = 5;
        var height = 5;
        if (argv.length >= 3) {
          width = parseInt(argv[2])
        }
        if (argv.length >= 4) {
          height = parseInt(argv[3])
        }

If the player inputs an invalid block, then an exception will be raised. If the exception is not caught, then the player will be informed about the error, and your script will be halted.

Printing Output
--------------------

Sometimes, you may want to write output to chat. Perhaps you would like to notify that the script has completed running, or perhaps you are debugging your script. In any case, you can do so through ``CraftScriptContext#print``:

::

    context.print("Hello!")

Other printing functions, such as ``CraftScriptContext#error`` and ``CraftScriptContext#printRaw``, also exist. This code snippet will print the exception raised if the player inputs an invalid block:

.. topic:: Example: Printing an exception to error output

    ::

        context.checkArgs(1, 1, "<block>");
        try {
          var block = context.getBlock(argv[1]);
        } catch (e) {
          context.error(e);
        }

Note that ``console.log`` will not work because there is no console. ``System.out.println`` will work if the ``System`` class is imported but is not recommended because it will not be reported to the player.


Miscellaneous
---------------

Rhino does not support all ES2015+ features yet, see https://mozilla.github.io/rhino/compat/engines.html for details.

Example Scripts
---------------

You can find some example scripts in the `GitHub repository for WorldEdit <https://github.com/EngineHub/WorldEdit/tree/master/contrib/craftscripts>`_. Note that they may not all be updated for current WorldEdit API. You can find more about the WorldEdit API in the :doc:`API section <../../api/index>`.
