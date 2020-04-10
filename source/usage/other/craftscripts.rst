CraftScripts
============

.. highlight:: javascript

Scripts allow you to program small tasks without having to learn Java, figure out how to compile WorldEdit, or bother with reinventing the wheel. CraftScripts are written in JavaScript.

Requirements
~~~~~~~~~~~~

Before you start using CraftScripts, you'll have to install the `Rhino JavaScript engine <https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino>`_. A direct link to the download is `here <http://ftp.mozilla.org/pub/mozilla.org/js/rhino1_7R2.zip>`_. Open the zip file, and extract ``js.jar``. Note that if you download a newer version than the recommended one, the ``.jar`` file may have a different name. Move ``js.jar`` to the ``plugins/`` or ``plugins/WorldEdit`` folder (on Bukkit) or the ``mods`` folder (other platforms).

Using CraftScripts
~~~~~~~~~~~~~~~~~~

Once you have the JS engine installed, drop your CraftScript ``.js`` files in the ``craftscripts`` folder (in the WorldEdit config folder - either ``plugins/WorldEdit`` or ``config/WorldEdit`` depending on platform).

To run a CraftScript

.. code-block:: text

    /cs <filename> <args>
    /.s <args>

The ``/cs`` command will run the CraftScript with the given filename (``.js`` can be left out). Each CraftScript may have its own arguments. The ``/.s`` command will re-run your last used CraftScript.

Writing CraftScripts
~~~~~~~~~~~~~~~~~~~~

Scripting in WorldEdit allows you to write world manipulation code without having to learn Java or compile your code. Scripts, called CraftScripts in WorldEdit, and are written in JavaScript and go into your craftscripts/ directory. The advantages of writing scripts with WorldEdit are:

* Hook right into WorldEdit's undo/redo system
* Use WorldEdit's block place prioritization
* Accept WorldEdit's powerful block type syntax (``//set sign[facing=north]``)
* Get the region selected by the user

.. note:: It is recommended you have a basic understanding of JavaScript or Java to begin writing CraftScripts.

.. tip:: While we'll be going over using CraftScripts with the WorldEdit API, there are no real restrictions on what you can do. Advanced users may even hook into the API of the underlying platform (Bukkit, Forge, etc).

Introduction
------------

Scripts have the following three variables in their global namespace:

* ``context`` is an instance of `CraftScriptContext <https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/scripting/CraftScriptContext.java>`_.
* ``player`` is the player who invoked the script, an instance of `Player <https://github.com/EngineHub/WorldEdit/blob/master/worldedit-core/src/main/java/com/sk89q/worldedit/entity/Player.java>`_.
* ``argv`` is a Java array strings, which are the arguments used upon invoking the scripts

Working with blocks
-------------------

All block editing in WorldEdit is done through an EditSession. This object handles history and block placement order all automatically. To get an edit session for your own script, use:

::

    var sess = context.remember();

Every time you call that method, you will get a new ``EditSession``, so be sure to keep one around. To set blocks, you will either need to provide a ``BlockState`` which is a combination of a block type and one or more states, or a ``BaseBlock``, which is a ``BlockState`` that may additionally have NBT data.

.. topic:: Example: Setting a block to white wool

    ::

        importPackage(Packages.com.sk89q.worldedit.world.block);

        var sess = context.remember();
        sess.setBlock(player.getBlockOn().toVector().toBlockPoint(), BlockTypes.WHITE_WOOL.getDefaultState());

Note that because ``BlockTypes`` is in the ``com.sk89q.worldedit.world.block`` namespace, it had to be imported first. The first argument for ``setBlock()`` is a ``BlockVector3`` indicating the position in the world.

To get blocks, use ``getBlock()`` on ``EditSession``. You'll get back a ``BaseBlock`` too.

Processing arguments
--------------------

Arguments are passed in under the ``argv`` variable. If you need to check whether the right number of arguments was provided by the user, you can use ``CraftScriptContext#checkArgs()``.

The ``CraftScriptContext`` can to some basic argument parsing with ``CraftScriptContext#getBlock()``. You can also hook directly into WorldEdit's parsers via ``WorldEdit.getInstance().getPatternFactory()`` and ``.getMaskFactory()``.

.. topic:: Example: Checking arguments

    ::

        context.checkArgs(1, 3, "<block> [width] [height]");
        var block = context.getBlock(argv[1]);

What happens if the user inputs an invalid block? An exception will be raised and if you don't catch it, the user will be informed about their error and your script will be halted.

Working with Java packages
--------------------------

To import a java package, you can use the following syntax::

    importPackage(Packages.package.name.here);

You can import any package available in the Java classpath - not restricted to WorldEdit.

Example Scripts
---------------

You can find some example scripts in the `GitHub repository for WorldEdit <https://github.com/EngineHub/WorldEdit/tree/master/contrib/craftscripts>`_. Note that they may not all be updated for current WorldEdit API. You can find more about the WorldEdit API in the :doc:`API section <../../api/index>`.
