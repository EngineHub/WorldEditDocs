================
Common Questions
================

.. contents::
    :local:
    :backlinks: none

General
=======

Why don't any commands work?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If no commands work, it may because WorldEdit failed to start:

* Make sure that you are running Bukkit/Forge/Sponge/etc. A vanilla minecraft server will not load plugins/mods!

  * You can run a command such as ``version`` (Bukkit), ``sponge version`` (Sponge) or ``forge help`` (Forge) to ensure your server is running proper software. In single-player, the Main Menu should have a "Mods" button (and WorldEdit should be in the list!).

* Make sure that you have the proper version of WorldEdit for your version of Minecraft.

If those solutions do not help you, you will need to look through your startup log:

* If you use a game server host, use its log viewer.
* You can also open up "latest.log" in the logs folder of your server directory. (On older versions of Minecraft, the log file was "server.log" in the root directory.)

If you are unable to discover the problem from reading the server log, you can :doc:`ask for help or submit a bug report <support>`.

How old is WorldEdit?
~~~~~~~~~~~~~~~~~~~~~~

WorldEdit began in September 2010 for the "hMod" modding platform by `sk89q <http://www.sk89q.com>`_. Later on, WorldEdit was ported to Bukkit, and eventually to Forge and other platforms.

Who works on WorldEdit?
~~~~~~~~~~~~~~~~~~~~~~~~

WorldEdit has been developed by many people, and large portions of WorldEdit include contributed code. The list of top contributors can be `found on GitHub <https://github.com/EngineHub/WorldEdit/graphs/contributors>`_.

World-Editing
=============

Commands all return "0 blocks changed" even though they should be changing.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you've previously set a global mask with ``//gmask <mask>``, you'll have to clear it again with ``//gmask`` so it no longer masks your edits.

How do I remove a tool/brush from the item I'm holding?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``/none`` command while holding the item.


Why isn't sign text/chest contents/entities/etc working?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
On all versions of WorldEdit, you need to have the ``worldedit.setnbt`` permission (which can be granted through OP) in order to set block entities.

.. _bukkit-adapters:

On Bukkit servers, WorldEdit has to use some version-specific adapters to get full access to many functions due to how Bukkit works. It uses these adapters for block entities (blocks that use additional data including signs, containers, etc.), entities, and some other functionality. What this generally means is that every new release of Minecraft will require you to update WorldEdit. Usually, WorldEdit will be updated quickly, and you can find new releases or experimental builds via the links on the :doc:`main page <index>`.
