:page-js: fabric-permissions.js
:page-css: perm-converter.css

===========
Permissions
===========

By default, no one can use WorldEdit. In order for yourself, moderators, and players to use WorldEdit, you must provide the proper permissions. One way is to provide op to moderators and administrators (unless disabled in the :doc:`configuration <config>`), but providing the permission nodes on this page (through a permissions plugin) is the more flexible.

You can give the ``worldedit.*`` permission to give yourself and other administrators full access to WorldEdit.

Commands
=========

See the :doc:`commands` page for an explanation of some of these commands.

.. csv-table::
  :header: Command, Permission
  :widths: 15, 25

    ``/worldedit``,""
    ``/worldedit cui``,""
    ``/worldedit help``,"``worldedit.help``"
    ``/worldedit reload``,"``worldedit.reload``"
    ``/worldedit report``,"``worldedit.report``"
    ``/worldedit trace``,""
    ``/worldedit tz``,""
    ``/worldedit version``,""
    ``/undo``,"``worldedit.history.undo``, ``worldedit.history.undo.self``"
    ``/redo``,"``worldedit.history.redo``, ``worldedit.history.redo.self``"
    ``/clearhistory``,"``worldedit.history.clear``"
    ``//limit``,"``worldedit.limit``"
    ``//timeout``,"``worldedit.timeout``"
    ``//fast``,"``worldedit.fast``"
    ``//perf``,"``worldedit.perf``"
    ``//reorder``,"``worldedit.reorder``"
    ``//drawsel``,"``worldedit.drawsel``"
    ``//world``,"``worldedit.world``"
    ``//watchdog``,"``worldedit.watchdog``"
    ``/gmask``,"``worldedit.global-mask``"
    ``/toggleplace``,""
    ``/placement``,"``worldedit.placement``"
    ``/searchitem``,"``worldedit.searchitem``"
    ``//registry``,"``worldedit.registry``"
    ``/unstuck``,"``worldedit.navigation.unstuck``"
    ``/ascend``,"``worldedit.navigation.ascend``"
    ``/descend``,"``worldedit.navigation.descend``"
    ``/ceil``,"``worldedit.navigation.ceiling``"
    ``/thru``,"``worldedit.navigation.thru.command``"
    ``/jumpto``,"``worldedit.navigation.jumpto.command``"
    ``/up``,"``worldedit.navigation.up``"
    ``//pos``,"``worldedit.selection.pos``"
    ``//pos1``,"``worldedit.selection.pos``"
    ``//pos2``,"``worldedit.selection.pos``"
    ``//hpos1``,"``worldedit.selection.hpos``"
    ``//hpos2``,"``worldedit.selection.hpos``"
    ``//chunk``,"``worldedit.selection.chunk``"
    ``//wand``,"``worldedit.wand``"
    ``/toggleeditwand``,"``worldedit.wand.toggle``"
    ``//contract``,"``worldedit.selection.contract``"
    ``//shift``,"``worldedit.selection.shift``"
    ``//outset``,"``worldedit.selection.outset``"
    ``//inset``,"``worldedit.selection.inset``"
    ``//trim``,"``worldedit.selection.trim``"
    ``//size``,"``worldedit.selection.size``"
    ``//count``,"``worldedit.analysis.count``"
    ``//distr``,"``worldedit.analysis.distr``"
    ``//sel``,""
    ``//expand``,"``worldedit.selection.expand``"
    ``//expand vert``,""
    ``//set``,"``worldedit.region.set``"
    ``//line``,"``worldedit.region.line``"
    ``//curve``,"``worldedit.region.curve``"
    ``//replace``,"``worldedit.region.replace``"
    ``//overlay``,"``worldedit.region.overlay``"
    ``//center``,"``worldedit.region.center``"
    ``//naturalize``,"``worldedit.region.naturalize``"
    ``//walls``,"``worldedit.region.walls``"
    ``//faces``,"``worldedit.region.faces``"
    ``//smooth``,"``worldedit.region.smooth``"
    ``//snowsmooth``,"``worldedit.region.snowsmooth``"
    ``//move``,"``worldedit.region.move``"
    ``//stack``,"``worldedit.region.stack``"
    ``//regen``,"``worldedit.regen``"
    ``//deform``,"``worldedit.region.deform``"
    ``//hollow``,"``worldedit.region.hollow``"
    ``//forest``,"``worldedit.region.forest``"
    ``//flora``,"``worldedit.region.flora``"
    ``//update``,"``worldedit.update``"
    ``//hcyl``,"``worldedit.generation.cylinder``"
    ``//cyl``,"``worldedit.generation.cylinder``"
    ``//cone``,"``worldedit.generation.cone``"
    ``//hsphere``,"``worldedit.generation.sphere``"
    ``//sphere``,"``worldedit.generation.sphere``"
    ``/forestgen``,"``worldedit.generation.forest``"
    ``/pumpkins``,"``worldedit.generation.pumpkins``"
    ``//feature``,"``worldedit.generation.feature``"
    ``//structure``,"``worldedit.generation.structure``"
    ``//hpyramid``,"``worldedit.generation.pyramid``"
    ``//pyramid``,"``worldedit.generation.pyramid``"
    ``//generate``,"``worldedit.generation.shape``"
    ``//generatebiome``,"``worldedit.generation.shape.biome``"
    ``/schematic``,"``worldedit.schematic.delete``, ``worldedit.schematic.list``, ``worldedit.clipboard.load``, ``worldedit.schematic.save``, ``worldedit.schematic.formats``, ``worldedit.schematic.load``, ``worldedit.clipboard.save``, ``worldedit.clipboard.share``, ``worldedit.schematic.share``"
    ``/schematic delete``,"``worldedit.schematic.delete``"
    ``/schematic formats``,"``worldedit.schematic.formats``"
    ``/schematic list``,"``worldedit.schematic.list``"
    ``/schematic load``,"``worldedit.clipboard.load``, ``worldedit.schematic.load``"
    ``/schematic save``,"``worldedit.clipboard.save``, ``worldedit.schematic.save``"
    ``/schematic share``,"``worldedit.clipboard.share``, ``worldedit.schematic.share``"
    ``//copy``,"``worldedit.clipboard.copy``"
    ``//cut``,"``worldedit.clipboard.cut``"
    ``//paste``,"``worldedit.clipboard.paste``"
    ``//rotate``,"``worldedit.clipboard.rotate``"
    ``//flip``,"``worldedit.clipboard.flip``"
    ``/clearclipboard``,"``worldedit.clipboard.clear``"
    ``//revolve``,"``worldedit.revolve``"
    ``/tool``,""
    ``/tool cycler``,"``worldedit.tool.data-cycler``"
    ``/tool deltree``,"``worldedit.tool.deltree``"
    ``/tool farwand``,"``worldedit.tool.farwand``"
    ``/tool floodfill``,"``worldedit.tool.flood-fill``"
    ``/tool info``,"``worldedit.tool.info``"
    ``/tool lrbuild``,"``worldedit.tool.lrbuild``"
    ``/tool navwand``,"``worldedit.setwand``"
    ``/tool none``,""
    ``/tool repl``,"``worldedit.tool.replacer``"
    ``/tool selwand``,"``worldedit.setwand``"
    ``/tool stacker``,"``worldedit.tool.stack``"
    ``/tool tree``,"``worldedit.tool.tree``"
    ``/none``,""
    ``/selwand``,"``worldedit.setwand``"
    ``/navwand``,"``worldedit.setwand``"
    ``/info``,"``worldedit.tool.info``"
    ``/tree``,"``worldedit.tool.tree``"
    ``/repl``,"``worldedit.tool.replacer``"
    ``/cycler``,"``worldedit.tool.data-cycler``"
    ``/floodfill``,"``worldedit.tool.flood-fill``"
    ``/deltree``,"``worldedit.tool.deltree``"
    ``/farwand``,"``worldedit.tool.farwand``"
    ``/lrbuild``,"``worldedit.tool.lrbuild``"
    ``//``,"``worldedit.superpickaxe``"
    ``/mask``,"``worldedit.brush.options.mask``"
    ``/material``,"``worldedit.brush.options.material``"
    ``/range``,"``worldedit.brush.options.range``"
    ``/size``,"``worldedit.brush.options.size``"
    ``/tracemask``,"``worldedit.brush.options.tracemask``"
    ``/superpickaxe``,"``worldedit.superpickaxe.area``, ``worldedit.superpickaxe.recursive``, ``worldedit.superpickaxe``"
    ``/superpickaxe area``,"``worldedit.superpickaxe.area``"
    ``/superpickaxe recursive``,"``worldedit.superpickaxe.recursive``"
    ``/superpickaxe single``,"``worldedit.superpickaxe``"
    ``/brush``,""
    ``/brush apply``,"``worldedit.brush.apply``"
    ``/brush apply forest``,""
    ``/brush apply item``,"``worldedit.brush.item``"
    ``/brush apply set``,""
    ``/brush biome``,"``worldedit.brush.biome``"
    ``/brush butcher``,"``worldedit.brush.butcher``"
    ``/brush clipboard``,"``worldedit.brush.clipboard``"
    ``/brush cylinder``,"``worldedit.brush.cylinder``"
    ``/brush deform``,"``worldedit.brush.deform``"
    ``/brush dilate``,"``worldedit.brush.morph``"
    ``/brush erode``,"``worldedit.brush.morph``"
    ``/brush extinguish``,"``worldedit.brush.ex``"
    ``/brush feature``,"``worldedit.brush.feature``"
    ``/brush forest``,"``worldedit.brush.forest``"
    ``/brush gravity``,"``worldedit.brush.gravity``"
    ``/brush heightmap``,"``worldedit.brush.heightmap``"
    ``/brush lower``,"``worldedit.brush.lower``"
    ``/brush morph``,"``worldedit.brush.morph``"
    ``/brush none``,""
    ``/brush paint``,"``worldedit.brush.paint``"
    ``/brush paint forest``,""
    ``/brush paint item``,"``worldedit.brush.item``"
    ``/brush paint set``,""
    ``/brush raise``,"``worldedit.brush.raise``"
    ``/brush set``,"``worldedit.brush.set``"
    ``/brush smooth``,"``worldedit.brush.smooth``"
    ``/brush snow``,"``worldedit.brush.snow``"
    ``/brush snowsmooth``,"``worldedit.brush.snowsmooth``"
    ``/brush sphere``,"``worldedit.brush.sphere``"
    ``/brush splatter``,"``worldedit.brush.splatter``"
    ``/biomelist``,"``worldedit.biome.list``"
    ``/biomeinfo``,"``worldedit.biome.info``"
    ``//setbiome``,"``worldedit.biome.set``"
    ``//replacebiome``,"``worldedit.biome.set``"
    ``/chunkinfo``,"``worldedit.chunkinfo``"
    ``/listchunks``,"``worldedit.listchunks``"
    ``/delchunks``,"``worldedit.delchunks``"
    ``/restore``,"``worldedit.snapshots.restore``"
    ``/snapshot``,"``worldedit.snapshots.restore``, ``worldedit.snapshots.list``"
    ``/snapshot after``,"``worldedit.snapshots.restore``"
    ``/snapshot before``,"``worldedit.snapshots.restore``"
    ``/snapshot list``,"``worldedit.snapshots.list``"
    ``/snapshot sel``,"``worldedit.snapshots.restore``"
    ``/snapshot use``,"``worldedit.snapshots.restore``"
    ``/cs``,"``worldedit.scripting.execute``"
    ``/.s``,"``worldedit.scripting.execute``"
    ``//fill``,"``worldedit.fill``"
    ``//fillr``,"``worldedit.fill.recursive``"
    ``//drain``,"``worldedit.drain``"
    ``/fixlava``,"``worldedit.fixlava``"
    ``/fixwater``,"``worldedit.fixwater``"
    ``/removeabove``,"``worldedit.removeabove``"
    ``/removebelow``,"``worldedit.removebelow``"
    ``/removenear``,"``worldedit.removenear``"
    ``/replacenear``,"``worldedit.replacenear``"
    ``/snow``,"``worldedit.snow``"
    ``/thaw``,"``worldedit.thaw``"
    ``/green``,"``worldedit.green``"
    ``/extinguish``,"``worldedit.extinguish``"
    ``/butcher``,"``worldedit.butcher``"
    ``/remove``,"``worldedit.remove``"
    ``//calculate``,"``worldedit.calc``"
    ``//help``,"``worldedit.help``"

Other Permissions
==================

.. csv-table::
    :header: Permission, Explanation
    :widths: 15, 25

    ``worldedit.navigation.jumpto.tool``,"Allows usage of the navigation wand's ``/jumpto`` shortcut (left click)."
    ``worldedit.navigation.thru.tool``,"Allows usage of the navigation wand's ``/thru`` shortcut (right click)."
    ``worldedit.anyblock``,"Allows usage of blocks in the :doc:`disallowed-blocks <config>` config option."
    ``worldedit.limit.unrestricted``,"Allows setting the limit via the ``//limit`` :doc:`command <commands>` higher than the maximum in the :doc:`configuration <config>`, as well as other limit bypasses."
    ``worldedit.timeout.unrestricted``,"Allows setting the calculation timeout via the ``//timeout`` :doc:`command <commands>` higher than the maximum in the :doc:`configuration <config>`."
    ``worldedit.inventory.unrestricted``,"Override the ``use-inventory`` option if enabled in the :doc:`configuration <config>`."
    ``worldedit.override.bedrock``,"Allows breaking of bedrock with the super-pickaxe tool."
    ``worldedit.override.data-cycler``,"Allows cycling non-whitelisted blocks with the data cycler tool."
    ``worldedit.setnbt``,"Allows setting `extra data <https://minecraft.wiki/w/Block_entity>`_ on blocks (such as signs, chests, etc)."
    ``worldedit.report.pastebin``,"Allows uploading report files to pastebin automatically for the ``/worldedit report`` :doc:`command <commands>`."
    ``worldedit.scripting.execute.<filename>``,"Allows using the CraftScript with the given filename."

Fabric Permissions Integration
==============================

.. versionadded:: 7.4.5

WorldEdit integrates into the Fabric Permissions API v1.
The API identifies permissions with a namespaced Minecraft ``Identifier`` rather than a dotted string,
so the nodes listed above are converted before they are checked. Depending on which permissions mod you use, you may need to write them differently.

.. warning::

    If a node cannot be converted, WorldEdit falls back to the Fabric Permissions API v0, and then to vanilla operator levels.
    This should not happen in practice as we generally don't have ``worldedit`` as its own permission node,
    but if other mods use our checks this may be an issue.

Which form do I use?
---------------------

Due to how permissions have historically worked, you might need to use different forms of the converted permission node.
There are two forms of every node, and both come from the same conversion:

``worldedit:region.set``
    The **identifier form**, for mods that expose the permission API's identifiers directly.

``worldedit.region.set``
    The **traditional form**. Some mods, like LuckPerms, rejoin the identifier's namespace and path with a ``.`` instead of a ``:``
    to match how permission nodes were traditionally formatted.

.. warning::

    The traditional form is *not* always the same as the original node listed above.
    It is the converted node rejoined with a dot, so any lowercasing or escaping still applies.
    For example, ``worldedit.scripting.execute.my script_v1!`` becomes ``worldedit.scripting.execute.my_20script_5fv1_21``.

    This only matters in practice for dynamic nodes, such as ``worldedit.scripting.execute.<filename>``.
    Every static node WorldEdit uses is already lowercase and made of safe characters, so the result is identical.

Converter
----------

To assist with setting permissions, we've provided a small tool that converts from a permission node to the forms described above:

..
    This <noscript> should be moved to a globally applied <head> if we ever need this elsewhere.
.. only:: html and not epub and not singlehtml

    .. raw:: html

        <noscript>
            <style>
                .js-only {
                    display: none;
                }
            </style>
        </noscript>

    .. admonition:: Converter Tool
        :class: admonition-tool

        .. raw:: html

            <form class="js-only perm-converter" onsubmit="return false" oninput="
                showPermissionConversion(
                    'perm-converter-input',
                    'perm-converter-identifier',
                    'perm-converter-traditional'
                )">
              <div class="perm-converter-field">
                <label for="perm-converter-input">WorldEdit permission node</label>
                <input id="perm-converter-input" type="text" placeholder="Enter a permission node here..."
                       spellcheck="false" autocapitalize="off" autocorrect="off"
                       pattern="\s*[^.\s][^.]*\..*\S\s*"
                       aria-describedby="perm-converter-hint" />
                <p class="perm-converter-hint" id="perm-converter-hint">Needs a namespace and a path
                  separated by a dot, such as <code>worldedit.region.set</code>. A node without a dot
                  is only matched by the fallback.</p>
              </div>
              <div class="perm-converter-field">
                <label for="perm-converter-identifier">Identifier form</label>
                <output id="perm-converter-identifier" for="perm-converter-input"></output>
              </div>
              <div class="perm-converter-field">
                <label for="perm-converter-traditional">Traditional form</label>
                <output id="perm-converter-traditional" for="perm-converter-input"></output>
              </div>
            </form>
            <noscript>
              <p>The interactive converter needs JavaScript. You can apply the rules below by hand instead.</p>
            </noscript>

.. only:: epub or singlehtml or not html

    .. note::

        The interactive converter is only available in the online documentation.
        You can apply the rules below by hand instead.

How the conversion works
-------------------------

#. Split the node at the **first** ``.``, into a *namespace* and *path*. If there is no ``.``, or it is the first or last character, the node is not usable with the API and only the fallback works.
#. Convert both parts to lowercase using Java's ``toLowerCase(Locale.ROOT)``, then encode it as UTF-8.
#. Keep each byte that is ``a`` to ``z``, ``0`` to ``9``, ``.`` or ``-``. The *path* must also keep ``/``. Replace every other byte with ``_`` followed by its two hex digits. Notably, this includes ``_`` itself, which is output as ``_5f``.
#. Join the two parts with ``:`` for the identifier form, or with ``.`` for the traditional form.

Examples
---------

.. csv-table::
    :header: Node, Identifier form, Traditional form
    :widths: 20, 20, 20

    ``worldedit.region.set``,"``worldedit:region.set``","``worldedit.region.set``"
    ``WorldEdit.scripting.execute.Build.js``,"``worldedit:scripting.execute.build.js``","``worldedit.scripting.execute.build.js``"
    ``worldedit.scripting.execute.my script_v1!``,"``worldedit:scripting.execute.my_20script_5fv1_21``","``worldedit.scripting.execute.my_20script_5fv1_21``"
    ``worldedit.scripting.execute.café``,"``worldedit:scripting.execute.caf_c3_a9``","``worldedit.scripting.execute.caf_c3_a9``"
    ``worldedit.scripting.execute/tools/build.js``,"``worldedit:scripting.execute/tools/build.js``","``worldedit.scripting.execute/tools/build.js``"
    ``worldedit``,"Not converted, only uses fallback","Not converted, only uses fallback"
