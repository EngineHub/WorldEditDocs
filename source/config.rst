=============
Configuration
=============

Although WorldEdit is primarily command driven, there are some configuration options which may change or limit the behavior of WorldEdit's commands and tools.

Configuration Files
===================

Once you have run your server with WorldEdit installed, you will find the main configuration file generated in a location which depends on your platform.

Bukkit Server
~~~~~~~~~~~~~

Configuration options for the Bukkit version of WorldEdit are found in ``plugins/WorldEdit/config.yml``, relative to the server root.

Note that the YAML format which Bukkit uses is very sensitive to errors. You must use 4 spaces for indentation (tabs will break the file!), and adhere to YAML's syntax. If you are unfamiliar with editing YAML files, you can run your config through an online validator (like `this one <http://yaml-online-parser.appspot.com/>`_) and ensure that it does not return an error.

Forge/Fabric
~~~~~~~~~~~~

Configuration options in Forge/Fabric can be found in the ``config/worldedit/worldedit.properties`` file. On a server, this is relative to the server root (where the main server .jar is). On a single-player installation, this is in your ".minecraft" folder.

Sponge Server
~~~~~~~~~~~~~

Configuration options in Sponge servers (either SpongeForge or SpongeVanilla) can be found in the ``config/worldedit/worldedit.conf`` file.

Settings
========

.. note::

    Since the underlying platforms are often in various states of development, not all settings will work on all platforms. Please :doc:`notify us <support>` if you find this to be the case.

.. csv-table::
    :header: Setting, Default, Description
    :widths: 12, 5, 30

    defaultLocale,default,"The default locale to use for translations, defaults to the system locale."
    profile,false,"Whether to print out a blocks changed/time info after each operation."
    traceUnflushedSessions,false,"Display a debug message when an edit isn't completed properly."
    disallowedBlocks,"<list of blocks>",A list of blocks that cannot be used in patterns (mostly physics blocks that will "pop off" and may severely lag or crash the server if thousands of items are spawned).
    defaultChangeLimit,-1,The default amount of blocks that can be set in one operation.
    maxChangeLimit,-1,The maximum amount of blocks for the change limit (set with ``//limit`` in-game)
    defaultMaxPolygonalPoints,-1,
    maxPolygonalPoints,20,
    defaultMaxPolyhedronPoints,-1,
    maxPolyhedronPoints,20,
    snapshotRepo,,"If not left empty, the directory name to look for snapshots"
    snapshotsExperimental,false,"If true, uses the new snapshot code. Try it out and report bugs!"
    maxRadius,-1,"Maximum radius of commands that take a radius"
    maxSuperPickaxeSize,5,"Maximum size of super pickaxe tools"
    maxBrushRadius,6,"Maximum size of brushes"
    logCommands,false,"Whether to log more informative information on command usage."
    logFile,"","If logCommands is true, the file to log to."
    logFormat,"[%1$tY-%1$tm-%1$td %1$tH:%1$tM:%1$tS %4$s]: %5$s%6$s%n",The format of command logging
    wandItem,"minecraft:wooden_axe",The default item used for selection regions, overriden by existing sessions
    superPickaxeDrop,true,Whether the single super pickaxe mode will drop items for blocks it breaks
    superPickaxeManyDrop,true,Whether multi super pickaxe modes will drop items for blocks they break
    useInventory,false,Require players to have items in their inventory to make edits (this option is not well supported and not recommended)
    useInventoryOverride,false,Allow a permission node to override the above setting
    useInventoryCreativeOverride,false,Allow creative mode to override the above setting
    navigationUseGlass,true,Whether the ``/up`` and ``/ceil`` commands should place a glass block for the player to stand on if in mid-air
    navigationWand,"minecraft:compass",The default item used for the navigation wand which allows ``/jumpto`` and ``/thru`` as left-click/right-click, overriden by existing sessions
    navigationWandMaxDistance,50,The max distance the navigation wand should trace to find a block to jump to
    scriptTimeout,3000,The maximum time a craftscript can run before it is terminated
    calculationTimeout,100,The default time an expression can run before it is terminated
    maxCalculationTimeout,300,The maximum time an expression can run before termination (changed in game with ``//timeout``)
    allowedDataCycleBlocks,,"If not empty, a whitelist of blocks which the data cycler tool can be used on"
    saveDir,"schematics",The directory in which to save schematics (relative to the worldedit folder)
    scriptsDir,"craftscripts",The directory in which to look for craftscripts
    allowSymlinks,false,Whether to allow the above to be symlinked locations (useful for sharing between servers)
    butcherDefaultRadius,-1,The default radius of the ``/butcher`` command (-1 for infinite)
    butcherMaxRadius,-1,The maximum radius of the ``/butcher`` command
    serverSideCUI,true,Whether to allow the usage of ``//drawsel``
    defaultVerticalHeight,256,"The height to use for commands that take an optional height."
    extendedYLimit,false,"If true, use slower but unbounded positions. This should only be needed with a mod that extends the height limit."
