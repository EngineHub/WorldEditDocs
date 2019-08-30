========
Commands
========

.. contents::
    :local:

.. note::

    Arguments enclosed in ``[ ]`` are optional, those enclosed in ``< >`` are required.

.. tip::

    You can access a command listing in-game via the ``//help`` command.

General Commands
~~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/worldedit"></span>

.. topic:: ``/worldedit`` (or ``/we``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"WorldEdit commands"
        **Usage**,"``/worldedit <help|version|reload|cui|tz|report>``"

.. raw:: html

    <span id="command-/worldedit-help"></span>

.. topic:: ``/worldedit help``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Displays help for WorldEdit commands"
        **Permissions**,"``worldedit.help``"
        **Usage**,"``/worldedit help [-s] [-p <page>] [command...]``"
          ``[-s]``,"List sub-commands of the given command, if applicable"
          ``[-p <page>]``,"The page to retrieve"
          ``[command...]``,"The command to retrieve help for"

.. raw:: html

    <span id="command-/worldedit-version"></span>

.. topic:: ``/worldedit version`` (or ``/worldedit ver``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Get WorldEdit version"
        **Usage**,"``/worldedit version``"

.. raw:: html

    <span id="command-/worldedit-reload"></span>

.. topic:: ``/worldedit reload``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Reload configuration"
        **Permissions**,"``worldedit.reload``"
        **Usage**,"``/worldedit reload``"

.. raw:: html

    <span id="command-/worldedit-cui"></span>

.. topic:: ``/worldedit cui``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Complete CUI handshake (internal usage)"
        **Usage**,"``/worldedit cui``"

.. raw:: html

    <span id="command-/worldedit-tz"></span>

.. topic:: ``/worldedit tz``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set your timezone for snapshots"
        **Usage**,"``/worldedit tz <timezone>``"
          ``<timezone>``,"The timezone to set"

.. raw:: html

    <span id="command-/worldedit-report"></span>

.. topic:: ``/worldedit report``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Writes a report on WorldEdit"
        **Permissions**,"``worldedit.report``"
        **Usage**,"``/worldedit report [-p]``"
          ``[-p]``,"Pastebins the report"

.. raw:: html

    <span id="command-/undo"></span>

.. topic:: ``/undo`` (or ``//undo``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Undoes the last action (from history)"
        **Permissions**,"``worldedit.history.undo``, ``worldedit.history.undo.self``"
        **Usage**,"``/undo [times] [player]``"
          ``[times]``,"Number of undoes to perform"
          ``[player]``,"Undo this player's operations"

.. raw:: html

    <span id="command-/redo"></span>

.. topic:: ``/redo`` (or ``//redo``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Redoes the last action (from history)"
        **Permissions**,"``worldedit.history.redo``, ``worldedit.history.redo.self``"
        **Usage**,"``/redo [times] [player]``"
          ``[times]``,"Number of redoes to perform"
          ``[player]``,"Redo this player's operations"

.. raw:: html

    <span id="command-/clearhistory"></span>

.. topic:: ``/clearhistory`` (or ``//clearhistory``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Clear your history"
        **Permissions**,"``worldedit.history.clear``"
        **Usage**,"``/clearhistory``"

.. raw:: html

    <span id="command-//limit"></span>

.. topic:: ``//limit``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Modify block change limit"
        **Permissions**,"``worldedit.limit``"
        **Usage**,"``//limit [limit]``"
          ``[limit]``,"The limit to set"

.. raw:: html

    <span id="command-//timeout"></span>

.. topic:: ``//timeout``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Modify evaluation timeout time."
        **Permissions**,"``worldedit.timeout``"
        **Usage**,"``//timeout [limit]``"
          ``[limit]``,"The timeout time to set"

.. raw:: html

    <span id="command-//fast"></span>

.. topic:: ``//fast``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Toggle fast mode"
        **Permissions**,"``worldedit.fast``"
        **Usage**,"``//fast [fastMode]``"
          ``[fastMode]``,"The new fast mode state"

.. raw:: html

    <span id="command-//reorder"></span>

.. topic:: ``//reorder``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Sets the reorder mode of WorldEdit"
        **Permissions**,"``worldedit.reorder``"
        **Usage**,"``//reorder [reorderMode]``"
          ``[reorderMode]``,"The reorder mode"

.. raw:: html

    <span id="command-//drawsel"></span>

.. topic:: ``//drawsel``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Toggle drawing the current selection"
        **Permissions**,"``worldedit.drawsel``"
        **Usage**,"``//drawsel [drawSelection]``"
          ``[drawSelection]``,"The new draw selection state"

.. raw:: html

    <span id="command-//world"></span>

.. topic:: ``//world``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Sets the world override"
        **Permissions**,"``worldedit.world``"
        **Usage**,"``//world [world]``"
          ``[world]``,"The world override"

.. raw:: html

    <span id="command-/gmask"></span>

.. topic:: ``/gmask`` (or ``//gmask``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set the global mask"
        **Permissions**,"``worldedit.global-mask``"
        **Usage**,"``/gmask [mask]``"
          ``[mask]``,"The mask to set"

.. raw:: html

    <span id="command-/toggleplace"></span>

.. topic:: ``/toggleplace`` (or ``//toggleplace``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Switch between your position and pos1 for placement"
        **Usage**,"``/toggleplace``"

.. raw:: html

    <span id="command-/searchitem"></span>

.. topic:: ``/searchitem`` (or ``//searchitem``, ``//l``, ``//search``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Search for an item"
        **Permissions**,"``worldedit.searchitem``"
        **Usage**,"``/searchitem [-bi] [-p <page>] <query...>``"
          ``[-b]``,"Only search for blocks"
          ``[-i]``,"Only search for items"
          ``[-p <page>]``,"Page of results to return"
          ``<query...>``,"Search query"


Navigation Commands
~~~~~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/unstuck"></span>

.. topic:: ``/unstuck`` (or ``/!``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Escape from being stuck inside a block"
        **Permissions**,"``worldedit.navigation.unstuck``"
        **Usage**,"``/unstuck``"

.. raw:: html

    <span id="command-/ascend"></span>

.. topic:: ``/ascend`` (or ``/asc``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Go up a floor"
        **Permissions**,"``worldedit.navigation.ascend``"
        **Usage**,"``/ascend [levels]``"
          ``[levels]``,"# of levels to ascend"

.. raw:: html

    <span id="command-/descend"></span>

.. topic:: ``/descend`` (or ``/desc``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Go down a floor"
        **Permissions**,"``worldedit.navigation.descend``"
        **Usage**,"``/descend [levels]``"
          ``[levels]``,"# of levels to descend"

.. raw:: html

    <span id="command-/ceil"></span>

.. topic:: ``/ceil``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Go to the ceiling"
        **Permissions**,"``worldedit.navigation.ceiling``"
        **Usage**,"``/ceil [-fg] [clearance]``"
          ``[clearance]``,"# of blocks to leave above you"
          ``[-f]``,"Force using flight to keep you still"
          ``[-g]``,"Force using glass to keep you still"

.. raw:: html

    <span id="command-/thru"></span>

.. topic:: ``/thru``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Pass through walls"
        **Permissions**,"``worldedit.navigation.thru.command``"
        **Usage**,"``/thru``"

.. raw:: html

    <span id="command-/jumpto"></span>

.. topic:: ``/jumpto`` (or ``/j``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Teleport to a location"
        **Permissions**,"``worldedit.navigation.jumpto.command``"
        **Usage**,"``/jumpto``"

.. raw:: html

    <span id="command-/up"></span>

.. topic:: ``/up``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Go upwards some distance"
        **Permissions**,"``worldedit.navigation.up``"
        **Usage**,"``/up [-fg] <distance>``"
          ``<distance>``,"Distance to go upwards"
          ``[-f]``,"Force using flight to keep you still"
          ``[-g]``,"Force using glass to keep you still"


Selection Commands
~~~~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-//pos1"></span>

.. topic:: ``//pos1``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set position 1"
        **Permissions**,"``worldedit.selection.pos``"
        **Usage**,"``//pos1 [coordinates]``"
          ``[coordinates]``,"Coordinates to set position 1 to"

.. raw:: html

    <span id="command-//pos2"></span>

.. topic:: ``//pos2``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set position 2"
        **Permissions**,"``worldedit.selection.pos``"
        **Usage**,"``//pos2 [coordinates]``"
          ``[coordinates]``,"Coordinates to set position 2 to"

.. raw:: html

    <span id="command-//hpos1"></span>

.. topic:: ``//hpos1``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set position 1 to targeted block"
        **Permissions**,"``worldedit.selection.hpos``"
        **Usage**,"``//hpos1``"

.. raw:: html

    <span id="command-//hpos2"></span>

.. topic:: ``//hpos2``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set position 2 to targeted block"
        **Permissions**,"``worldedit.selection.hpos``"
        **Usage**,"``//hpos2``"

.. raw:: html

    <span id="command-//chunk"></span>

.. topic:: ``//chunk``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set the selection to your current chunk."
        **Permissions**,"``worldedit.selection.chunk``"
        **Usage**,"``//chunk [-cs] [coordinates]``"
          ``[coordinates]``,"The chunk to select"
          ``[-s]``,"Expand your selection to encompass all chunks that are part of it"
          ``[-c]``,"Use chunk coordinates instead of block coordinates"

.. raw:: html

    <span id="command-//wand"></span>

.. topic:: ``//wand``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Get the wand object"
        **Permissions**,"``worldedit.wand``"
        **Usage**,"``//wand [-n]``"
          ``[-n]``,"Get a navigation wand"

.. raw:: html

    <span id="command-/toggleeditwand"></span>

.. topic:: ``/toggleeditwand``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Remind the user that the wand is now a tool and can be unbound with /none."
        **Permissions**,"``worldedit.wand.toggle``"
        **Usage**,"``/toggleeditwand``"

.. raw:: html

    <span id="command-//contract"></span>

.. topic:: ``//contract``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Contract the selection area"
        **Permissions**,"``worldedit.selection.contract``"
        **Usage**,"``//contract <amount> [reverseAmount] [direction]``"
          ``<amount>``,"Amount to contract the selection by"
          ``[reverseAmount]``,"Amount to contract the selection by in the other direction"
          ``[direction]``,"Direction to contract"

.. raw:: html

    <span id="command-//shift"></span>

.. topic:: ``//shift``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Shift the selection area"
        **Permissions**,"``worldedit.selection.shift``"
        **Usage**,"``//shift <amount> [direction]``"
          ``<amount>``,"Amount to shift the selection by"
          ``[direction]``,"Direction to contract"

.. raw:: html

    <span id="command-//outset"></span>

.. topic:: ``//outset``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Outset the selection area"
        **Permissions**,"``worldedit.selection.outset``"
        **Usage**,"``//outset [-hv] <amount>``"
          ``<amount>``,"Amount to expand the selection by in all directions"
          ``[-h]``,"Only expand horizontally"
          ``[-v]``,"Only expand vertically"

.. raw:: html

    <span id="command-//inset"></span>

.. topic:: ``//inset``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Inset the selection area"
        **Permissions**,"``worldedit.selection.inset``"
        **Usage**,"``//inset [-hv] <amount>``"
          ``<amount>``,"Amount to contract the selection by in all directions"
          ``[-h]``,"Only contract horizontally"
          ``[-v]``,"Only contract vertically"

.. raw:: html

    <span id="command-//size"></span>

.. topic:: ``//size``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Get information about the selection"
        **Permissions**,"``worldedit.selection.size``"
        **Usage**,"``//size [-c]``"
          ``[-c]``,"Get clipboard info instead"

.. raw:: html

    <span id="command-//count"></span>

.. topic:: ``//count``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Counts the number of blocks matching a mask"
        **Permissions**,"``worldedit.analysis.count``"
        **Usage**,"``//count <mask>``"
          ``<mask>``,"The mask of blocks to match"

.. raw:: html

    <span id="command-//distr"></span>

.. topic:: ``//distr``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Get the distribution of blocks in the selection"
        **Permissions**,"``worldedit.analysis.distr``"
        **Usage**,"``//distr [-cd] [-p <page>]``"
          ``[-c]``,"Get the distribution of the clipboard instead"
          ``[-d]``,"Separate blocks by state"
          ``[-p <page>]``,"Gets page from a previous distribution."

.. raw:: html

    <span id="command-//sel"></span>

.. topic:: ``//sel`` (or ``/;``, ``//desel``, ``//deselect``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Choose a region selector"
        **Usage**,"``//sel [-d] [selector]``"
          ``[selector]``,"Selector to switch to"
          ``[-d]``,"Set default selector"

.. raw:: html

    <span id="command-//expand"></span>

.. topic:: ``//expand``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Expand the selection area"
        **Permissions**,"``worldedit.selection.expand``"
        **Usage**,"``//expand <vert|<amount> [reverseAmount] [direction]>``"
          ``<amount>``,"Amount to expand the selection by, can be `vert` to expand to the whole vertical column"
          ``[reverseAmount]``,"Amount to expand the selection by in the other direction"
          ``[direction]``,"Direction to expand"

.. raw:: html

    <span id="command-//expand-vert"></span>

.. topic:: ``//expand vert``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Vertically expand the selection to world limits."
        **Usage**,"``//expand vert``"


Region Commands
~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-//set"></span>

.. topic:: ``//set``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Sets all the blocks in the region"
        **Permissions**,"``worldedit.region.set``"
        **Usage**,"``//set <pattern>``"
          ``<pattern>``,"The pattern of blocks to set"

.. raw:: html

    <span id="command-//line"></span>

.. topic:: ``//line``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Draws a line segment between cuboid selection corners

        Can only be used with a cuboid selection"
        **Permissions**,"``worldedit.region.line``"
        **Usage**,"``//line [-h] <pattern> [thickness]``"
          ``<pattern>``,"The pattern of blocks to place"
          ``[thickness]``,"The thickness of the line"
          ``[-h]``,"Generate only a shell"

.. raw:: html

    <span id="command-//curve"></span>

.. topic:: ``//curve``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Draws a spline through selected points

        Can only be used with a convex polyhedral selection"
        **Permissions**,"``worldedit.region.curve``"
        **Usage**,"``//curve [-h] <pattern> [thickness]``"
          ``<pattern>``,"The pattern of blocks to place"
          ``[thickness]``,"The thickness of the curve"
          ``[-h]``,"Generate only a shell"

.. raw:: html

    <span id="command-//replace"></span>

.. topic:: ``//replace`` (or ``//re``, ``//rep``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Replace all blocks in the selection with another"
        **Permissions**,"``worldedit.region.replace``"
        **Usage**,"``//replace [from] <to>``"
          ``[from]``,"The mask representing blocks to replace"
          ``<to>``,"The pattern of blocks to replace with"

.. raw:: html

    <span id="command-//overlay"></span>

.. topic:: ``//overlay``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set a block on top of blocks in the region"
        **Permissions**,"``worldedit.region.overlay``"
        **Usage**,"``//overlay <pattern>``"
          ``<pattern>``,"The pattern of blocks to overlay"

.. raw:: html

    <span id="command-//center"></span>

.. topic:: ``//center`` (or ``//middle``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set the center block(s)"
        **Permissions**,"``worldedit.region.center``"
        **Usage**,"``//center <pattern>``"
          ``<pattern>``,"The pattern of blocks to set"

.. raw:: html

    <span id="command-//naturalize"></span>

.. topic:: ``//naturalize``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"3 layers of dirt on top then rock below"
        **Permissions**,"``worldedit.region.naturalize``"
        **Usage**,"``//naturalize``"

.. raw:: html

    <span id="command-//walls"></span>

.. topic:: ``//walls``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Build the four sides of the selection"
        **Permissions**,"``worldedit.region.walls``"
        **Usage**,"``//walls <pattern>``"
          ``<pattern>``,"The pattern of blocks to set"

.. raw:: html

    <span id="command-//faces"></span>

.. topic:: ``//faces`` (or ``//outline``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Build the walls, ceiling, and floor of a selection"
        **Permissions**,"``worldedit.region.faces``"
        **Usage**,"``//faces <pattern>``"
          ``<pattern>``,"The pattern of blocks to set"

.. raw:: html

    <span id="command-//smooth"></span>

.. topic:: ``//smooth``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Smooth the elevation in the selection

        Example: '//smooth 1 grass_block,dirt,stone' would only smooth natural surface terrain."
        **Permissions**,"``worldedit.region.smooth``"
        **Usage**,"``//smooth [iterations] [mask]``"
          ``[iterations]``,"# of iterations to perform"
          ``[mask]``,"The mask of blocks to use as the height map"

.. raw:: html

    <span id="command-//move"></span>

.. topic:: ``//move``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Move the contents of the selection"
        **Permissions**,"``worldedit.region.move``"
        **Usage**,"``//move [-abes] [count] [direction] [replace] [-m <mask>]``"
          ``[count]``,"# of blocks to move"
          ``[direction]``,"The direction to move"
          ``[replace]``,"The pattern of blocks to leave"
          ``[-s]``,"Shift the selection to the target location"
          ``[-a]``,"Ignore air blocks"
          ``[-e]``,"Also copy entities"
          ``[-b]``,"Also copy biomes"
          ``[-m <mask>]``,"Set the include mask, non-matching blocks become air"

.. raw:: html

    <span id="command-//stack"></span>

.. topic:: ``//stack``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Repeat the contents of the selection"
        **Permissions**,"``worldedit.region.stack``"
        **Usage**,"``//stack [-abes] [count] [direction] [-m <mask>]``"
          ``[count]``,"# of copies to stack"
          ``[direction]``,"The direction to stack"
          ``[-s]``,"Shift the selection to the last stacked copy"
          ``[-a]``,"Ignore air blocks"
          ``[-e]``,"Also copy entities"
          ``[-b]``,"Also copy biomes"
          ``[-m <mask>]``,"Set the include mask, non-matching blocks become air"

.. raw:: html

    <span id="command-//regen"></span>

.. topic:: ``//regen``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Regenerates the contents of the selection

        This command might affect things outside the selection,
        if they are within the same chunk."
        **Permissions**,"``worldedit.regen``"
        **Usage**,"``//regen``"

.. raw:: html

    <span id="command-//deform"></span>

.. topic:: ``//deform``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Deforms a selected region with an expression

        The expression is executed for each block and is expected
        to modify the variables x, y and z to point to a new block
        to fetch. See also https://tinyurl.com/weexpr"
        **Permissions**,"``worldedit.region.deform``"
        **Usage**,"``//deform [-or] <expression...>``"
          ``<expression...>``,"The expression to use"
          ``[-r]``,"Use the game's coordinate origin"
          ``[-o]``,"Use the selection's center as origin"

.. raw:: html

    <span id="command-//hollow"></span>

.. topic:: ``//hollow``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Hollows out the object contained in this selection

        Thickness is measured in manhattan distance."
        **Permissions**,"``worldedit.region.hollow``"
        **Usage**,"``//hollow [thickness] [pattern]``"
          ``[thickness]``,"Thickness of the shell to leave"
          ``[pattern]``,"The pattern of blocks to replace the hollowed area with"

.. raw:: html

    <span id="command-//forest"></span>

.. topic:: ``//forest``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Make a forest within the region"
        **Permissions**,"``worldedit.region.forest``"
        **Usage**,"``//forest [type] [density]``"
          ``[type]``,"The type of tree to place"
          ``[density]``,"The density of the forest"

.. raw:: html

    <span id="command-//flora"></span>

.. topic:: ``//flora``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Make flora within the region"
        **Permissions**,"``worldedit.region.flora``"
        **Usage**,"``//flora [density]``"
          ``[density]``,"The density of the forest"


Generation Commands
~~~~~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-//hcyl"></span>

.. topic:: ``//hcyl``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Generates a hollow cylinder."
        **Permissions**,"``worldedit.generation.cylinder``"
        **Usage**,"``//hcyl <pattern> <radii> [height]``"
          ``<pattern>``,"The pattern of blocks to generate"
          ``<radii>``,"The radii of the cylinder. 1st is N/S, 2nd is E/W"
          ``[height]``,"The height of the cylinder"

.. raw:: html

    <span id="command-//cyl"></span>

.. topic:: ``//cyl``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Generates a cylinder."
        **Permissions**,"``worldedit.generation.cylinder``"
        **Usage**,"``//cyl [-h] <pattern> <radii> [height]``"
          ``<pattern>``,"The pattern of blocks to generate"
          ``<radii>``,"The radii of the cylinder. 1st is N/S, 2nd is E/W"
          ``[height]``,"The height of the cylinder"
          ``[-h]``,"Make a hollow cylinder"

.. raw:: html

    <span id="command-//hsphere"></span>

.. topic:: ``//hsphere``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Generates a hollow sphere."
        **Permissions**,"``worldedit.generation.sphere``"
        **Usage**,"``//hsphere [-r] <pattern> <radii>``"
          ``<pattern>``,"The pattern of blocks to generate"
          ``<radii>``,"The radii of the sphere. Order is N/S, U/D, E/W"
          ``[-r]``,"Raise the bottom of the sphere to the placement position"

.. raw:: html

    <span id="command-//sphere"></span>

.. topic:: ``//sphere``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Generates a filled sphere."
        **Permissions**,"``worldedit.generation.sphere``"
        **Usage**,"``//sphere [-hr] <pattern> <radii>``"
          ``<pattern>``,"The pattern of blocks to generate"
          ``<radii>``,"The radii of the sphere. Order is N/S, U/D, E/W"
          ``[-r]``,"Raise the bottom of the sphere to the placement position"
          ``[-h]``,"Make a hollow sphere"

.. raw:: html

    <span id="command-/forestgen"></span>

.. topic:: ``/forestgen``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Generate a forest"
        **Permissions**,"``worldedit.generation.forest``"
        **Usage**,"``/forestgen [size] [type] [density]``"
          ``[size]``,"The size of the forest, in blocks"
          ``[type]``,"The type of forest"
          ``[density]``,"The density of the forest, between 0 and 100"

.. raw:: html

    <span id="command-/pumpkins"></span>

.. topic:: ``/pumpkins``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Generate pumpkin patches"
        **Permissions**,"``worldedit.generation.pumpkins``"
        **Usage**,"``/pumpkins [size]``"
          ``[size]``,"The size of the patch"

.. raw:: html

    <span id="command-//hpyramid"></span>

.. topic:: ``//hpyramid``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Generate a hollow pyramid"
        **Permissions**,"``worldedit.generation.pyramid``"
        **Usage**,"``//hpyramid <pattern> <size>``"
          ``<pattern>``,"The pattern of blocks to set"
          ``<size>``,"The size of the pyramid"

.. raw:: html

    <span id="command-//pyramid"></span>

.. topic:: ``//pyramid``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Generate a filled pyramid"
        **Permissions**,"``worldedit.generation.pyramid``"
        **Usage**,"``//pyramid [-h] <pattern> <size>``"
          ``<pattern>``,"The pattern of blocks to set"
          ``<size>``,"The size of the pyramid"
          ``[-h]``,"Make a hollow pyramid"

.. raw:: html

    <span id="command-//generate"></span>

.. topic:: ``//generate`` (or ``//gen``, ``//g``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Generates a shape according to a formula.

        See also https://tinyurl.com/weexpr."
        **Permissions**,"``worldedit.generation.shape``"
        **Usage**,"``//generate [-chor] <pattern> <expression...>``"
          ``<pattern>``,"The pattern of blocks to set"
          ``<expression...>``,"Expression to test block placement locations and set block type"
          ``[-h]``,"Generate a hollow shape"
          ``[-r]``,"Use the game's coordinate origin"
          ``[-o]``,"Use the placement's coordinate origin"
          ``[-c]``,"Use the selection's center as origin"

.. raw:: html

    <span id="command-//generatebiome"></span>

.. topic:: ``//generatebiome`` (or ``//genbiome``, ``//gb``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Sets biome according to a formula.

        See also https://tinyurl.com/weexpr."
        **Permissions**,"``worldedit.generation.shape.biome``"
        **Usage**,"``//generatebiome [-chor] <target> <expression...>``"
          ``<target>``,"The biome type to set"
          ``<expression...>``,"Expression to test block placement locations and set biome type"
          ``[-h]``,"Generate a hollow shape"
          ``[-r]``,"Use the game's coordinate origin"
          ``[-o]``,"Use the placement's coordinate origin"
          ``[-c]``,"Use the selection's center as origin"


Schematic and Clipboard Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/schematic"></span>

.. topic:: ``/schematic`` (or ``/schem``, ``//schematic``, ``//schem``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Schematic commands for saving/loading areas"
        **Permissions**,"``worldedit.schematic.delete``, ``worldedit.schematic.list``, ``worldedit.clipboard.load``, ``worldedit.schematic.save``, ``worldedit.schematic.formats``, ``worldedit.schematic.load``, ``worldedit.clipboard.save``"
        **Usage**,"``/schematic <list|formats|load|delete|save>``"

.. raw:: html

    <span id="command-/schematic-list"></span>

.. topic:: ``/schematic list`` (or ``/schematic all``, ``/schematic ls``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"List saved schematics

        Note: Format is not fully verified until loading."
        **Permissions**,"``worldedit.schematic.list``"
        **Usage**,"``/schematic list [-dn] [-p <page>]``"
          ``[-p <page>]``,"Page to view."
          ``[-d]``,"Sort by date, oldest first"
          ``[-n]``,"Sort by date, newest first"

.. raw:: html

    <span id="command-/schematic-formats"></span>

.. topic:: ``/schematic formats`` (or ``/schematic listformats``, ``/schematic f``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"List available formats"
        **Permissions**,"``worldedit.schematic.formats``"
        **Usage**,"``/schematic formats``"

.. raw:: html

    <span id="command-/schematic-load"></span>

.. topic:: ``/schematic load``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Load a schematic into your clipboard"
        **Permissions**,"``worldedit.clipboard.load``, ``worldedit.schematic.load``"
        **Usage**,"``/schematic load <filename> [formatName]``"
          ``<filename>``,"File name."
          ``[formatName]``,"Format name."

.. raw:: html

    <span id="command-/schematic-delete"></span>

.. topic:: ``/schematic delete`` (or ``/schematic d``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Delete a saved schematic"
        **Permissions**,"``worldedit.schematic.delete``"
        **Usage**,"``/schematic delete <filename>``"
          ``<filename>``,"File name."

.. raw:: html

    <span id="command-/schematic-save"></span>

.. topic:: ``/schematic save``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Save a schematic into your clipboard"
        **Permissions**,"``worldedit.clipboard.save``, ``worldedit.schematic.save``"
        **Usage**,"``/schematic save [-f] <filename> [formatName]``"
          ``<filename>``,"File name."
          ``[formatName]``,"Format name."
          ``[-f]``,"Overwrite an existing file."

.. raw:: html

    <span id="command-//copy"></span>

.. topic:: ``//copy``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Copy the selection to the clipboard"
        **Permissions**,"``worldedit.clipboard.copy``"
        **Usage**,"``//copy [-be] [-m <mask>]``"
          ``[-e]``,"Also copy entities"
          ``[-b]``,"Also copy biomes"
          ``[-m <mask>]``,"Set the include mask, non-matching blocks become air"

.. raw:: html

    <span id="command-//cut"></span>

.. topic:: ``//cut``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Cut the selection to the clipboard"
        **Permissions**,"``worldedit.clipboard.cut``"
        **Usage**,"``//cut [-be] [leavePattern] [-m <mask>]``"
          ``[leavePattern]``,"Pattern to leave in place of the selection"
          ``[-e]``,"Also cut entities"
          ``[-b]``,"Also copy biomes, source biomes are unaffected"
          ``[-m <mask>]``,"Set the exclude mask, non-matching blocks become air"

.. raw:: html

    <span id="command-//paste"></span>

.. topic:: ``//paste``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Paste the clipboard's contents"
        **Permissions**,"``worldedit.clipboard.paste``"
        **Usage**,"``//paste [-abeos] [-m <sourceMask>]``"
          ``[-a]``,"Skip air blocks"
          ``[-o]``,"Paste at the original position"
          ``[-s]``,"Select the region after pasting"
          ``[-e]``,"Paste entities if available"
          ``[-b]``,"Paste biomes if available"
          ``[-m <sourceMask>]``,"Only paste blocks matching this mask"

.. raw:: html

    <span id="command-//rotate"></span>

.. topic:: ``//rotate``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Rotate the contents of the clipboard

        Non-destructively rotate the contents of the clipboard.
        Angles are provided in degrees and a positive angle will result in a clockwise rotation. Multiple rotations can be stacked. Interpolation is not performed so angles should be a multiple of 90 degrees."
        **Permissions**,"``worldedit.clipboard.rotate``"
        **Usage**,"``//rotate <yRotate> [xRotate] [zRotate]``"
          ``<yRotate>``,"Amount to rotate on the y-axis"
          ``[xRotate]``,"Amount to rotate on the x-axis"
          ``[zRotate]``,"Amount to rotate on the z-axis"

.. raw:: html

    <span id="command-//flip"></span>

.. topic:: ``//flip``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Flip the contents of the clipboard across the origin"
        **Permissions**,"``worldedit.clipboard.flip``"
        **Usage**,"``//flip [direction]``"
          ``[direction]``,"The direction to flip, defaults to look direction."

.. raw:: html

    <span id="command-/clearclipboard"></span>

.. topic:: ``/clearclipboard``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Clear your clipboard"
        **Permissions**,"``worldedit.clipboard.clear``"
        **Usage**,"``/clearclipboard``"


Tool Commands
~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/none"></span>

.. topic:: ``/none``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Unbind a bound tool from your current item"
        **Usage**,"``/none``"

.. raw:: html

    <span id="command-//selwand"></span>

.. topic:: ``//selwand`` (or ``/selwand``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Selection wand tool"
        **Permissions**,"``worldedit.setwand``"
        **Usage**,"``//selwand``"

.. raw:: html

    <span id="command-//navwand"></span>

.. topic:: ``//navwand`` (or ``/navwand``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Navigation wand tool"
        **Permissions**,"``worldedit.setwand``"
        **Usage**,"``//navwand``"

.. raw:: html

    <span id="command-/info"></span>

.. topic:: ``/info``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Block information tool"
        **Permissions**,"``worldedit.tool.info``"
        **Usage**,"``/info``"

.. raw:: html

    <span id="command-/tree"></span>

.. topic:: ``/tree``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Tree generator tool"
        **Permissions**,"``worldedit.tool.tree``"
        **Usage**,"``/tree [type]``"
          ``[type]``,"Type of tree to generate"

.. raw:: html

    <span id="command-/repl"></span>

.. topic:: ``/repl``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Block replacer tool"
        **Permissions**,"``worldedit.tool.replacer``"
        **Usage**,"``/repl <pattern>``"
          ``<pattern>``,"The pattern of blocks to place"

.. raw:: html

    <span id="command-/cycler"></span>

.. topic:: ``/cycler``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Block data cycler tool"
        **Permissions**,"``worldedit.tool.data-cycler``"
        **Usage**,"``/cycler``"

.. raw:: html

    <span id="command-/floodfill"></span>

.. topic:: ``/floodfill`` (or ``/flood``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Flood fill tool"
        **Permissions**,"``worldedit.tool.flood-fill``"
        **Usage**,"``/floodfill <pattern> <range>``"
          ``<pattern>``,"The pattern to flood fill"
          ``<range>``,"The range to perform the fill"

.. raw:: html

    <span id="command-/deltree"></span>

.. topic:: ``/deltree``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Floating tree remover tool"
        **Permissions**,"``worldedit.tool.deltree``"
        **Usage**,"``/deltree``"

.. raw:: html

    <span id="command-/farwand"></span>

.. topic:: ``/farwand``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Wand at a distance tool"
        **Permissions**,"``worldedit.tool.farwand``"
        **Usage**,"``/farwand``"

.. raw:: html

    <span id="command-/lrbuild"></span>

.. topic:: ``/lrbuild`` (or ``//lrbuild``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Long-range building tool"
        **Permissions**,"``worldedit.tool.lrbuild``"
        **Usage**,"``/lrbuild <primary> <secondary>``"
          ``<primary>``,"Pattern to set on left-click"
          ``<secondary>``,"Pattern to set on right-click"

.. raw:: html

    <span id="command-//"></span>

.. topic:: ``//`` (or ``/,``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Toggle the super pickaxe function"
        **Permissions**,"``worldedit.superpickaxe``"
        **Usage**,"``// [superPickaxe]``"
          ``[superPickaxe]``,"The new super pickaxe state"

.. raw:: html

    <span id="command-/mask"></span>

.. topic:: ``/mask``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set the brush mask"
        **Permissions**,"``worldedit.brush.options.mask``"
        **Usage**,"``/mask [mask]``"
          ``[mask]``,"The mask to set"

.. raw:: html

    <span id="command-/material"></span>

.. topic:: ``/material`` (or ``//material``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set the brush material"
        **Permissions**,"``worldedit.brush.options.material``"
        **Usage**,"``/material <pattern>``"
          ``<pattern>``,"The pattern of blocks to use"

.. raw:: html

    <span id="command-/range"></span>

.. topic:: ``/range``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set the brush range"
        **Permissions**,"``worldedit.brush.options.range``"
        **Usage**,"``/range <range>``"
          ``<range>``,"The range of the brush"

.. raw:: html

    <span id="command-/size"></span>

.. topic:: ``/size``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set the brush size"
        **Permissions**,"``worldedit.brush.options.size``"
        **Usage**,"``/size <size>``"
          ``<size>``,"The size of the brush"

.. raw:: html

    <span id="command-/tracemask"></span>

.. topic:: ``/tracemask``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set the mask used to stop tool traces"
        **Permissions**,"``worldedit.brush.options.tracemask``"
        **Usage**,"``/tracemask [mask]``"
          ``[mask]``,"The trace mask to set"


Super Pickaxe Commands
~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/superpickaxe"></span>

.. topic:: ``/superpickaxe`` (or ``/pickaxe``, ``/sp``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Super-pickaxe commands"
        **Permissions**,"``worldedit.superpickaxe.area``, ``worldedit.superpickaxe.recursive``, ``worldedit.superpickaxe``"
        **Usage**,"``/superpickaxe <single|area|recursive>``"

.. raw:: html

    <span id="command-/superpickaxe-single"></span>

.. topic:: ``/superpickaxe single``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Enable the single block super pickaxe mode"
        **Permissions**,"``worldedit.superpickaxe``"
        **Usage**,"``/superpickaxe single``"

.. raw:: html

    <span id="command-/superpickaxe-area"></span>

.. topic:: ``/superpickaxe area``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Enable the area super pickaxe pickaxe mode"
        **Permissions**,"``worldedit.superpickaxe.area``"
        **Usage**,"``/superpickaxe area <range>``"
          ``<range>``,"The range of the area pickaxe"

.. raw:: html

    <span id="command-/superpickaxe-recursive"></span>

.. topic:: ``/superpickaxe recursive`` (or ``/superpickaxe recur``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Enable the recursive super pickaxe pickaxe mode"
        **Permissions**,"``worldedit.superpickaxe.recursive``"
        **Usage**,"``/superpickaxe recursive <range>``"
          ``<range>``,"The range of the recursive pickaxe"


Brush Commands
~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/brush"></span>

.. topic:: ``/brush`` (or ``/br``, ``//brush``, ``//br``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Brushing commands"
        **Permissions**,"``worldedit.brush.ex``, ``worldedit.brush.paint``, ``worldedit.brush.clipboard``, ``worldedit.brush.butcher``, ``worldedit.brush.set``, ``worldedit.brush.gravity``, ``worldedit.brush.forest``, ``worldedit.brush.lower``, ``worldedit.brush.smooth``, ``worldedit.brush.cylinder``, ``worldedit.brush.apply``, ``worldedit.brush.deform``, ``worldedit.brush.sphere``, ``worldedit.brush.raise``"
        **Usage**,"``/brush <forest|cylinder|set|apply|deform|lower|butcher|paint|clipboard|gravity|extinguish|sphere|raise|smooth>``"

.. raw:: html

    <span id="command-/brush-forest"></span>

.. topic:: ``/brush forest``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Forest brush, creates a forest in the area"
        **Permissions**,"``worldedit.brush.forest``"
        **Usage**,"``/brush forest <shape> [radius] [density] <type>``"
          ``<shape>``,"The shape of the region"
          ``[radius]``,"The size of the brush"
          ``[density]``,"The density of the brush"
          ``<type>``,"The type of tree to use"

.. raw:: html

    <span id="command-/brush-cylinder"></span>

.. topic:: ``/brush cylinder`` (or ``/brush cyl``, ``/brush c``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Choose the cylinder brush"
        **Permissions**,"``worldedit.brush.cylinder``"
        **Usage**,"``/brush cylinder [-h] <pattern> [radius] [height]``"
          ``<pattern>``,"The pattern of blocks to set"
          ``[radius]``,"The radius of the cylinder"
          ``[height]``,"The height of the cylinder"
          ``[-h]``,"Create hollow cylinders instead"

.. raw:: html

    <span id="command-/brush-set"></span>

.. topic:: ``/brush set``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Set brush, sets all blocks in the area"
        **Permissions**,"``worldedit.brush.set``"
        **Usage**,"``/brush set <shape> [radius] <pattern>``"
          ``<shape>``,"The shape of the region"
          ``[radius]``,"The size of the brush"
          ``<pattern>``,"The pattern of blocks to set"

.. raw:: html

    <span id="command-/brush-apply"></span>

.. topic:: ``/brush apply``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Apply brush, apply a function to every block"
        **Permissions**,"``worldedit.brush.apply``"
        **Usage**,"``/brush apply <shape> [radius] <forest|item|set>``"
          ``<shape>``,"The shape of the region"
          ``[radius]``,"The size of the brush"

.. raw:: html

    <span id="command-/brush-deform"></span>

.. topic:: ``/brush deform``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Deform brush, applies an expression to an area"
        **Permissions**,"``worldedit.brush.deform``"
        **Usage**,"``/brush deform [-or] <shape> [radius] [expression]``"
          ``<shape>``,"The shape of the region"
          ``[radius]``,"The size of the brush"
          ``[expression]``,"Expression to apply"
          ``[-r]``,"Use the game's coordinate origin"
          ``[-o]``,"Use the placement position as the origin"

.. raw:: html

    <span id="command-/brush-lower"></span>

.. topic:: ``/brush lower``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Lower brush, lower all blocks by one"
        **Permissions**,"``worldedit.brush.lower``"
        **Usage**,"``/brush lower <shape> [radius]``"
          ``<shape>``,"The shape of the region"
          ``[radius]``,"The size of the brush"

.. raw:: html

    <span id="command-/brush-butcher"></span>

.. topic:: ``/brush butcher`` (or ``/brush kill``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Butcher brush, kills mobs within a radius"
        **Permissions**,"``worldedit.brush.butcher``"
        **Usage**,"``/brush butcher [-abfgnprt] [radius]``"
          ``[radius]``,"Radius to kill mobs in"
          ``[-p]``,"Also kill pets"
          ``[-n]``,"Also kill NPCs"
          ``[-g]``,"Also kill golems"
          ``[-a]``,"Also kill animals"
          ``[-b]``,"Also kill ambient mobs"
          ``[-t]``,"Also kill mobs with name tags"
          ``[-f]``,"Also kill all friendly mobs (Applies the flags `-abgnpt`)"
          ``[-r]``,"Also destroy armor stands"

.. raw:: html

    <span id="command-/brush-paint"></span>

.. topic:: ``/brush paint``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Paint brush, apply a function to a surface"
        **Permissions**,"``worldedit.brush.paint``"
        **Usage**,"``/brush paint <shape> [radius] [density] <forest|item|set>``"
          ``<shape>``,"The shape of the region"
          ``[radius]``,"The size of the brush"
          ``[density]``,"The density of the brush"

.. raw:: html

    <span id="command-/brush-clipboard"></span>

.. topic:: ``/brush clipboard`` (or ``/brush copy``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Choose the clipboard brush"
        **Permissions**,"``worldedit.brush.clipboard``"
        **Usage**,"``/brush clipboard [-abeo] [-m <sourceMask>]``"
          ``[-a]``,"Don't paste air from the clipboard"
          ``[-o]``,"Paste starting at the target location, instead of centering on it"
          ``[-e]``,"Paste entities if available"
          ``[-b]``,"Paste biomes if available"
          ``[-m <sourceMask>]``,"Skip blocks matching this mask in the clipboard"

.. raw:: html

    <span id="command-/brush-gravity"></span>

.. topic:: ``/brush gravity`` (or ``/brush grav``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Gravity brush, simulates the effect of gravity"
        **Permissions**,"``worldedit.brush.gravity``"
        **Usage**,"``/brush gravity [-h] [radius]``"
          ``[radius]``,"The radius to apply gravity in"
          ``[-h]``,"Affect blocks starting at max Y, rather than the target location Y + radius"

.. raw:: html

    <span id="command-/brush-extinguish"></span>

.. topic:: ``/brush extinguish`` (or ``/brush ex``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Shortcut fire extinguisher brush"
        **Permissions**,"``worldedit.brush.ex``"
        **Usage**,"``/brush extinguish [radius]``"
          ``[radius]``,"The radius to extinguish"

.. raw:: html

    <span id="command-/brush-sphere"></span>

.. topic:: ``/brush sphere`` (or ``/brush s``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Choose the sphere brush"
        **Permissions**,"``worldedit.brush.sphere``"
        **Usage**,"``/brush sphere [-h] <pattern> [radius]``"
          ``<pattern>``,"The pattern of blocks to set"
          ``[radius]``,"The radius of the sphere"
          ``[-h]``,"Create hollow spheres instead"

.. raw:: html

    <span id="command-/brush-raise"></span>

.. topic:: ``/brush raise``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Raise brush, raise all blocks by one"
        **Permissions**,"``worldedit.brush.raise``"
        **Usage**,"``/brush raise <shape> [radius]``"
          ``<shape>``,"The shape of the region"
          ``[radius]``,"The size of the brush"

.. raw:: html

    <span id="command-/brush-smooth"></span>

.. topic:: ``/brush smooth``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Choose the terrain softener brush

        Example: '/brush smooth 2 4 grass_block,dirt,stone'"
        **Permissions**,"``worldedit.brush.smooth``"
        **Usage**,"``/brush smooth [radius] [iterations] [mask]``"
          ``[radius]``,"The radius to sample for softening"
          ``[iterations]``,"The number of iterations to perform"
          ``[mask]``,"The mask of blocks to use for the heightmap"


Biome Commands
~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/biomelist"></span>

.. topic:: ``/biomelist`` (or ``/biomels``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Gets all biomes available."
        **Permissions**,"``worldedit.biome.list``"
        **Usage**,"``/biomelist [-p <page>]``"
          ``[-p <page>]``,"Page number."

.. raw:: html

    <span id="command-/biomeinfo"></span>

.. topic:: ``/biomeinfo``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Get the biome of the targeted block.

        By default, uses all blocks in your selection."
        **Permissions**,"``worldedit.biome.info``"
        **Usage**,"``/biomeinfo [-pt]``"
          ``[-t]``,"Use the block you are looking at."
          ``[-p]``,"Use the block you are currently in."

.. raw:: html

    <span id="command-//setbiome"></span>

.. topic:: ``//setbiome``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Sets the biome of your current block or region.

        By default, uses all the blocks in your selection"
        **Permissions**,"``worldedit.biome.set``"
        **Usage**,"``//setbiome [-p] <target>``"
          ``<target>``,"Biome type."
          ``[-p]``,"Use your current position"


Chunk Commands
~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/chunkinfo"></span>

.. topic:: ``/chunkinfo``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Get information about the chunk you're inside"
        **Permissions**,"``worldedit.chunkinfo``"
        **Usage**,"``/chunkinfo``"

.. raw:: html

    <span id="command-/listchunks"></span>

.. topic:: ``/listchunks``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"List chunks that your selection includes"
        **Permissions**,"``worldedit.listchunks``"
        **Usage**,"``/listchunks [-p <page>]``"
          ``[-p <page>]``,"Page number."

.. raw:: html

    <span id="command-/delchunks"></span>

.. topic:: ``/delchunks``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Delete chunks that your selection includes"
        **Permissions**,"``worldedit.delchunks``"
        **Usage**,"``/delchunks [-o <beforeTime>]``"
          ``[-o <beforeTime>]``,"Only delete chunks older than the specified time."


Snapshot Commands
~~~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/restore"></span>

.. topic:: ``/restore`` (or ``//restore``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Restore the selection from a snapshot"
        **Permissions**,"``worldedit.snapshots.restore``"
        **Usage**,"``/restore [snapshot]``"
          ``[snapshot]``,"The snapshot to restore"

.. raw:: html

    <span id="command-/snapshot"></span>

.. topic:: ``/snapshot`` (or ``/snap``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Snapshot commands for restoring backups"
        **Permissions**,"``worldedit.snapshots.restore``, ``worldedit.snapshots.list``"
        **Usage**,"``/snapshot <before|use|sel|after|list>``"

.. raw:: html

    <span id="command-/snapshot-before"></span>

.. topic:: ``/snapshot before``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Choose the nearest snapshot before a date"
        **Permissions**,"``worldedit.snapshots.restore``"
        **Usage**,"``/snapshot before <date>``"
          ``<date>``,"The soonest date that may be used"

.. raw:: html

    <span id="command-/snapshot-use"></span>

.. topic:: ``/snapshot use``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Choose a snapshot to use"
        **Permissions**,"``worldedit.snapshots.restore``"
        **Usage**,"``/snapshot use <name>``"
          ``<name>``,"Snapeshot to use"

.. raw:: html

    <span id="command-/snapshot-sel"></span>

.. topic:: ``/snapshot sel``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Choose the snapshot based on the list id"
        **Permissions**,"``worldedit.snapshots.restore``"
        **Usage**,"``/snapshot sel <index>``"
          ``<index>``,"The list ID to select"

.. raw:: html

    <span id="command-/snapshot-after"></span>

.. topic:: ``/snapshot after``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Choose the nearest snapshot after a date"
        **Permissions**,"``worldedit.snapshots.restore``"
        **Usage**,"``/snapshot after <date>``"
          ``<date>``,"The soonest date that may be used"

.. raw:: html

    <span id="command-/snapshot-list"></span>

.. topic:: ``/snapshot list``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"List snapshots"
        **Permissions**,"``worldedit.snapshots.list``"
        **Usage**,"``/snapshot list [-p <page>]``"
          ``[-p <page>]``,"Page of results to return"


Scripting Commands
~~~~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-/cs"></span>

.. topic:: ``/cs``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Execute a CraftScript"
        **Permissions**,"``worldedit.scripting.execute``"
        **Usage**,"``/cs <filename> [args...]``"
          ``<filename>``,"Filename of the CraftScript to load"
          ``[args...]``,"Arguments to the CraftScript"

.. raw:: html

    <span id="command-/.s"></span>

.. topic:: ``/.s``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Execute last CraftScript"
        **Permissions**,"``worldedit.scripting.execute``"
        **Usage**,"``/.s [args...]``"
          ``[args...]``,"Arguments to the CraftScript"


Utility Commands
~~~~~~~~~~~~~~~~
.. raw:: html

    <span id="command-//fill"></span>

.. topic:: ``//fill``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Fill a hole"
        **Permissions**,"``worldedit.fill``"
        **Usage**,"``//fill <pattern> <radius> [depth]``"
          ``<pattern>``,"The blocks to fill with"
          ``<radius>``,"The radius to fill in"
          ``[depth]``,"The depth to fill"

.. raw:: html

    <span id="command-//fillr"></span>

.. topic:: ``//fillr``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Fill a hole recursively"
        **Permissions**,"``worldedit.fill.recursive``"
        **Usage**,"``//fillr <pattern> <radius> [depth]``"
          ``<pattern>``,"The blocks to fill with"
          ``<radius>``,"The radius to fill in"
          ``[depth]``,"The depth to fill"

.. raw:: html

    <span id="command-//drain"></span>

.. topic:: ``//drain``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Drain a pool"
        **Permissions**,"``worldedit.drain``"
        **Usage**,"``//drain [-w] <radius>``"
          ``<radius>``,"The radius to drain"
          ``[-w]``,"Also un-waterlog blocks"

.. raw:: html

    <span id="command-/fixlava"></span>

.. topic:: ``/fixlava`` (or ``//fixlava``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Fix lava to be stationary"
        **Permissions**,"``worldedit.fixlava``"
        **Usage**,"``/fixlava <radius>``"
          ``<radius>``,"The radius to fix in"

.. raw:: html

    <span id="command-/fixwater"></span>

.. topic:: ``/fixwater`` (or ``//fixwater``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Fix water to be stationary"
        **Permissions**,"``worldedit.fixwater``"
        **Usage**,"``/fixwater <radius>``"
          ``<radius>``,"The radius to fix in"

.. raw:: html

    <span id="command-/removeabove"></span>

.. topic:: ``/removeabove`` (or ``//removeabove``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Remove blocks above your head."
        **Permissions**,"``worldedit.removeabove``"
        **Usage**,"``/removeabove [size] [height]``"
          ``[size]``,"The apothem of the square to remove from"
          ``[height]``,"The maximum height above you to remove from"

.. raw:: html

    <span id="command-/removebelow"></span>

.. topic:: ``/removebelow`` (or ``//removebelow``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Remove blocks below you."
        **Permissions**,"``worldedit.removebelow``"
        **Usage**,"``/removebelow [size] [height]``"
          ``[size]``,"The apothem of the square to remove from"
          ``[height]``,"The maximum height below you to remove from"

.. raw:: html

    <span id="command-/removenear"></span>

.. topic:: ``/removenear`` (or ``//removenear``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Remove blocks near you."
        **Permissions**,"``worldedit.removenear``"
        **Usage**,"``/removenear <mask> [radius]``"
          ``<mask>``,"The mask of blocks to remove"
          ``[radius]``,"The radius of the square to remove from"

.. raw:: html

    <span id="command-/replacenear"></span>

.. topic:: ``/replacenear`` (or ``//replacenear``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Replace nearby blocks"
        **Permissions**,"``worldedit.replacenear``"
        **Usage**,"``/replacenear <radius> [from] <to>``"
          ``<radius>``,"The radius of the square to remove in"
          ``[from]``,"The mask matching blocks to remove"
          ``<to>``,"The pattern of blocks to replace with"

.. raw:: html

    <span id="command-/snow"></span>

.. topic:: ``/snow`` (or ``//snow``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Simulates snow"
        **Permissions**,"``worldedit.snow``"
        **Usage**,"``/snow [size]``"
          ``[size]``,"The radius of the circle to snow in"

.. raw:: html

    <span id="command-/thaw"></span>

.. topic:: ``/thaw`` (or ``//thaw``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Thaws the area"
        **Permissions**,"``worldedit.thaw``"
        **Usage**,"``/thaw [size]``"
          ``[size]``,"The radius of the circle to thaw in"

.. raw:: html

    <span id="command-/green"></span>

.. topic:: ``/green`` (or ``//green``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Converts dirt to grass blocks in the area"
        **Permissions**,"``worldedit.green``"
        **Usage**,"``/green [-f] [size]``"
          ``[size]``,"The radius of the circle to convert in"
          ``[-f]``,"Also convert coarse dirt"

.. raw:: html

    <span id="command-/extinguish"></span>

.. topic:: ``/extinguish`` (or ``//ex``, ``//ext``, ``//extinguish``, ``/ex``, ``/ext``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Extinguish nearby fire"
        **Permissions**,"``worldedit.extinguish``"
        **Usage**,"``/extinguish [radius]``"
          ``[radius]``,"The radius of the square to remove in"

.. raw:: html

    <span id="command-/butcher"></span>

.. topic:: ``/butcher``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Kill all or nearby mobs"
        **Permissions**,"``worldedit.butcher``"
        **Usage**,"``/butcher [-abfgnprt] [radius]``"
          ``[radius]``,"Radius to kill mobs in"
          ``[-p]``,"Also kill pets"
          ``[-n]``,"Also kill NPCs"
          ``[-g]``,"Also kill golems"
          ``[-a]``,"Also kill animals"
          ``[-b]``,"Also kill ambient mobs"
          ``[-t]``,"Also kill mobs with name tags"
          ``[-f]``,"Also kill all friendly mobs (Applies the flags `-abgnpt`)"
          ``[-r]``,"Also destroy armor stands"

.. raw:: html

    <span id="command-/remove"></span>

.. topic:: ``/remove`` (or ``/rem``, ``/rement``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Remove all entities of a type"
        **Permissions**,"``worldedit.remove``"
        **Usage**,"``/remove <remover> <radius>``"
          ``<remover>``,"The type of entity to remove"
          ``<radius>``,"The radius of the cuboid to remove from"

.. raw:: html

    <span id="command-//calculate"></span>

.. topic:: ``//calculate`` (or ``//calc``, ``//eval``, ``//evaluate``, ``//solve``)
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Evaluate a mathematical expression"
        **Permissions**,"``worldedit.calc``"
        **Usage**,"``//calculate <input...>``"
          ``<input...>``,"Expression to evaluate"

.. raw:: html

    <span id="command-//help"></span>

.. topic:: ``//help``
    :class: command-topic

    .. csv-table::
        :widths: 8, 15

        **Description**,"Displays help for WorldEdit commands"
        **Permissions**,"``worldedit.help``"
        **Usage**,"``//help [-s] [-p <page>] [command...]``"
          ``[-s]``,"List sub-commands of the given command, if applicable"
          ``[-p <page>]``,"The page to retrieve"
          ``[command...]``,"The command to retrieve help for"

