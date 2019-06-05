========
Commands
========

.. contents::
    :local:

.. tip::

    Arguments enclosed in ``[ ]`` are optional, those enclosed in ``< >`` are required.


General Commands
~~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /worldedit,"(or /we)"
    Description,"WorldEdit commands"
    Usage,"/worldedit <version|reload|report|cui|tz|help>"

------------

.. csv-table::
    :widths: 8, 15

    /worldedit version,"(or /worldedit ver)"
    Description,"Get WorldEdit version"
    Usage,"/worldedit version"

------------

.. csv-table::
    :widths: 8, 15

    /worldedit reload,
    Description,"Reload configuration"
    Permissions,"worldedit.reload"
    Usage,"/worldedit reload"

------------

.. csv-table::
    :widths: 8, 15

    /worldedit report,
    Description,"Writes a report on WorldEdit"
    Permissions,"worldedit.report"
    Usage,"/worldedit report [-p]"
       [-p],"Pastebins the report"

------------

.. csv-table::
    :widths: 8, 15

    /worldedit cui,
    Description,"Complete CUI handshake (internal usage)"
    Usage,"/worldedit cui"

------------

.. csv-table::
    :widths: 8, 15

    /worldedit tz,
    Description,"Set your timezone for snapshots"
    Usage,"/worldedit tz <timezone>"
       <timezone>,"The timezone to set"

------------

.. csv-table::
    :widths: 8, 15

    /worldedit help,
    Description,"Displays help for WorldEdit commands"
    Permissions,"worldedit.help"
    Usage,"/worldedit help [-s] [-p <page>] [command...]"
       [-s],"List sub-commands of the given command, if applicable"
       [-p <page>],"The page to retrieve"
       [command...],"The command to retrieve help for"

------------

.. csv-table::
    :widths: 8, 15

    /undo,"(or //undo)"
    Description,"Undoes the last action (from history)"
    Permissions,"worldedit.history.undo"
    Usage,"/undo [times] [player]"
       [times],"Number of undoes to perform"
       [player],"Undo this player's operations"

------------

.. csv-table::
    :widths: 8, 15

    /redo,"(or //redo)"
    Description,"Redoes the last action (from history)"
    Permissions,"worldedit.history.redo"
    Usage,"/redo [times] [player]"
       [times],"Number of redoes to perform"
       [player],"Redo this player's operations"

------------

.. csv-table::
    :widths: 8, 15

    /clearhistory,"(or //clearhistory)"
    Description,"Clear your history"
    Permissions,"worldedit.history.clear"
    Usage,"/clearhistory"

------------

.. csv-table::
    :widths: 8, 15

    //limit,
    Description,"Modify block change limit"
    Permissions,"worldedit.limit"
    Usage,"//limit [limit]"
       [limit],"The limit to set"

------------

.. csv-table::
    :widths: 8, 15

    //timeout,
    Description,"Modify evaluation timeout time."
    Permissions,"worldedit.timeout"
    Usage,"//timeout [limit]"
       [limit],"The timeout time to set"

------------

.. csv-table::
    :widths: 8, 15

    //fast,
    Description,"Toggle fast mode"
    Permissions,"worldedit.fast"
    Usage,"//fast [fastMode]"
       [fastMode],"The new fast mode state"

------------

.. csv-table::
    :widths: 8, 15

    //reorder,
    Description,"Sets the reorder mode of WorldEdit"
    Permissions,"worldedit.reorder"
    Usage,"//reorder [reorderMode]"
       [reorderMode],"The reorder mode"

------------

.. csv-table::
    :widths: 8, 15

    //drawsel,
    Description,"Toggle drawing the current selection"
    Permissions,"worldedit.drawsel"
    Usage,"//drawsel [drawSelection]"
       [drawSelection],"The new draw selection state"

------------

.. csv-table::
    :widths: 8, 15

    /gmask,"(or //gmask)"
    Description,"Set the global mask"
    Permissions,"worldedit.global-mask"
    Usage,"/gmask [mask]"
       [mask],"The mask to set"

------------

.. csv-table::
    :widths: 8, 15

    /toggleplace,"(or //toggleplace)"
    Description,"Switch between your position and pos1 for placement"
    Usage,"/toggleplace"

------------

.. csv-table::
    :widths: 8, 15

    /searchitem,"(or //searchitem, //l, //search)"
    Description,"Search for an item"
    Permissions,"worldedit.searchitem"
    Usage,"/searchitem [-bi] [-p <page>] <query...>"
       [-b],"Only search for blocks"
       [-i],"Only search for items"
       [-p <page>],"Page of results to return"
       <query...>,"Search query"

Navigation Commands
~~~~~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /unstuck,"(or /!)"
    Description,"Escape from being stuck inside a block"
    Permissions,"worldedit.navigation.unstuck"
    Usage,"/unstuck"

------------

.. csv-table::
    :widths: 8, 15

    /ascend,"(or /asc)"
    Description,"Go up a floor"
    Permissions,"worldedit.navigation.ascend"
    Usage,"/ascend [levels]"
       [levels],"# of levels to ascend"

------------

.. csv-table::
    :widths: 8, 15

    /descend,"(or /desc)"
    Description,"Go down a floor"
    Permissions,"worldedit.navigation.descend"
    Usage,"/descend [levels]"
       [levels],"# of levels to descend"

------------

.. csv-table::
    :widths: 8, 15

    /ceil,
    Description,"Go to the ceiling"
    Permissions,"worldedit.navigation.ceiling"
    Usage,"/ceil [-fg] [clearance]"
       [clearance],"# of blocks to leave above you"
       [-f],"Force using flight to keep you still"
       [-g],"Force using glass to keep you still"

------------

.. csv-table::
    :widths: 8, 15

    /thru,
    Description,"Pass through walls"
    Permissions,"worldedit.navigation.thru.command"
    Usage,"/thru"

------------

.. csv-table::
    :widths: 8, 15

    /jumpto,"(or /j)"
    Description,"Teleport to a location"
    Permissions,"worldedit.navigation.jumpto.command"
    Usage,"/jumpto"

------------

.. csv-table::
    :widths: 8, 15

    /up,
    Description,"Go upwards some distance"
    Permissions,"worldedit.navigation.up"
    Usage,"/up [-fg] <distance>"
       <distance>,"Distance to go upwards"
       [-f],"Force using flight to keep you still"
       [-g],"Force using glass to keep you still"

Selection Commands
~~~~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    //pos1,
    Description,"Set position 1"
    Permissions,"worldedit.selection.pos"
    Usage,"//pos1 [coordinates]"
       [coordinates],"Coordinates to set position 1 to"

------------

.. csv-table::
    :widths: 8, 15

    //pos2,
    Description,"Set position 2"
    Permissions,"worldedit.selection.pos"
    Usage,"//pos2 [coordinates]"
       [coordinates],"Coordinates to set position 2 to"

------------

.. csv-table::
    :widths: 8, 15

    //hpos1,
    Description,"Set position 1 to targeted block"
    Permissions,"worldedit.selection.hpos"
    Usage,"//hpos1"

------------

.. csv-table::
    :widths: 8, 15

    //hpos2,
    Description,"Set position 2 to targeted block"
    Permissions,"worldedit.selection.hpos"
    Usage,"//hpos2"

------------

.. csv-table::
    :widths: 8, 15

    //chunk,
    Description,"Set the selection to your current chunk."
    Permissions,"worldedit.selection.chunk"
    Usage,"//chunk [-cs] [coordinates]"
       [coordinates],"The chunk to select"
       [-s],"Expand your selection to encompass all chunks that are part of it"
       [-c],"Use chunk coordinates instead of block coordinates"

------------

.. csv-table::
    :widths: 8, 15

    //wand,
    Description,"Get the wand object"
    Permissions,"worldedit.wand"
    Usage,"//wand"

------------

.. csv-table::
    :widths: 8, 15

    /toggleeditwand,
    Description,"Toggle functionality of the edit wand"
    Permissions,"worldedit.wand.toggle"
    Usage,"/toggleeditwand"

------------

.. csv-table::
    :widths: 8, 15

    //contract,
    Description,"Contract the selection area"
    Permissions,"worldedit.selection.contract"
    Usage,"//contract <amount> [reverseAmount] [direction]"
       <amount>,"Amount to contract the selection by"
       [reverseAmount],"Amount to contract the selection by in the other direction"
       [direction],"Direction to contract"

------------

.. csv-table::
    :widths: 8, 15

    //shift,
    Description,"Shift the selection area"
    Permissions,"worldedit.selection.shift"
    Usage,"//shift <amount> [direction]"
       <amount>,"Amount to shift the selection by"
       [direction],"Direction to contract"

------------

.. csv-table::
    :widths: 8, 15

    //outset,
    Description,"Outset the selection area"
    Permissions,"worldedit.selection.outset"
    Usage,"//outset [-hv] <amount>"
       <amount>,"Amount to expand the selection by in all directions"
       [-h],"Only expand horizontally"
       [-v],"Only expand vertically"

------------

.. csv-table::
    :widths: 8, 15

    //inset,
    Description,"Inset the selection area"
    Permissions,"worldedit.selection.inset"
    Usage,"//inset [-hv] <amount>"
       <amount>,"Amount to contract the selection by in all directions"
       [-h],"Only contract horizontally"
       [-v],"Only contract vertically"

------------

.. csv-table::
    :widths: 8, 15

    //size,
    Description,"Get information about the selection"
    Permissions,"worldedit.selection.size"
    Usage,"//size [-c]"
       [-c],"Get clipboard info instead"

------------

.. csv-table::
    :widths: 8, 15

    //count,
    Description,"Counts the number of a certain type of block"
    Permissions,"worldedit.analysis.count"
    Usage,"//count [-f] <blocks>"
       <blocks>,"The block type(s) to count"
       [-f],"Fuzzy, match states using a wildcard"

------------

.. csv-table::
    :widths: 8, 15

    //distr,
    Description,"Get the distribution of blocks in the selection"
    Permissions,"worldedit.analysis.distr"
    Usage,"//distr [-cd]"
       [-c],"Get the distribution of the clipboard instead"
       [-d],"Separate blocks by state"

------------

.. csv-table::
    :widths: 8, 15

    //sel,"(or //desel, //deselect, /;)"
    Description,"Choose a region selector"
    Usage,"//sel [-d] [selector]"
       [selector],"Selector to switch to"
       [-d],"Set default selector"

------------

.. csv-table::
    :widths: 8, 15

    //expand,
    Description,"Expand the selection area"
    Permissions,"worldedit.selection.expand"
    Usage,"//expand <vert|<amount> [reverseAmount] [direction]>"
       <amount>,"Amount to expand the selection by, can be `vert` to expand to the whole vertical column"
       [reverseAmount],"Amount to expand the selection by in the other direction"
       [direction],"Direction to expand"

------------

.. csv-table::
    :widths: 8, 15

    //expand vert,
    Description,"Vertically expand the selection to world limits."
    Usage,"//expand vert"

Region Commands
~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    //set,
    Description,"Sets all the blocks in the region"
    Permissions,"worldedit.region.set"
    Usage,"//set <pattern>"
       <pattern>,"The pattern of blocks to set"

------------

.. csv-table::
    :widths: 8, 15

    //line,
    Description,"Draws a line segment between cuboid selection corners"
    Permissions,"worldedit.region.line"
    Usage,"//line [-h] <pattern> [thickness]"
       <pattern>,"The pattern of blocks to place"
       [thickness],"The thickness of the line"
       [-h],"Generate only a shell"
    ,"Can only be used with a cuboid selection"

------------

.. csv-table::
    :widths: 8, 15

    //curve,
    Description,"Draws a spline through selected points"
    Permissions,"worldedit.region.curve"
    Usage,"//curve [-h] <pattern> [thickness]"
       <pattern>,"The pattern of blocks to place"
       [thickness],"The thickness of the curve"
       [-h],"Generate only a shell"
    ,"Can only be used with a convex polyhedral selection"

------------

.. csv-table::
    :widths: 8, 15

    //replace,"(or //rep, //re)"
    Description,"Replace all blocks in the selection with another"
    Permissions,"worldedit.region.replace"
    Usage,"//replace [from] <to>"
       [from],"The mask representing blocks to replace"
       <to>,"The pattern of blocks to replace with"

------------

.. csv-table::
    :widths: 8, 15

    //overlay,
    Description,"Set a block on top of blocks in the region"
    Permissions,"worldedit.region.overlay"
    Usage,"//overlay <pattern>"
       <pattern>,"The pattern of blocks to overlay"

------------

.. csv-table::
    :widths: 8, 15

    //center,"(or //middle)"
    Description,"Set the center block(s)"
    Permissions,"worldedit.region.center"
    Usage,"//center <pattern>"
       <pattern>,"The pattern of blocks to set"

------------

.. csv-table::
    :widths: 8, 15

    //naturalize,
    Description,"3 layers of dirt on top then rock below"
    Permissions,"worldedit.region.naturalize"
    Usage,"//naturalize"

------------

.. csv-table::
    :widths: 8, 15

    //walls,
    Description,"Build the four sides of the selection"
    Permissions,"worldedit.region.walls"
    Usage,"//walls <pattern>"
       <pattern>,"The pattern of blocks to set"

------------

.. csv-table::
    :widths: 8, 15

    //faces,"(or //outline)"
    Description,"Build the walls, ceiling, and floor of a selection"
    Permissions,"worldedit.region.faces"
    Usage,"//faces <pattern>"
       <pattern>,"The pattern of blocks to set"

------------

.. csv-table::
    :widths: 8, 15

    //smooth,
    Description,"Smooth the elevation in the selection"
    Permissions,"worldedit.region.smooth"
    Usage,"//smooth [iterations] [mask]"
       [iterations],"# of iterations to perform"
       [mask],"The mask of blocks to use as the height map"
    ,"Example: '//smooth 1 grass_block,dirt,stone' would only smooth natural surface terrain."

------------

.. csv-table::
    :widths: 8, 15

    //move,
    Description,"Move the contents of the selection"
    Permissions,"worldedit.region.move"
    Usage,"//move [-as] [count] [direction] [replace]"
       [count],"# of blocks to move"
       [direction],"The direction to move"
       [replace],"The pattern of blocks to leave"
       [-s],"Shift the selection to the target location"
       [-a],"Ignore air blocks"

------------

.. csv-table::
    :widths: 8, 15

    //stack,
    Description,"Repeat the contents of the selection"
    Permissions,"worldedit.region.stack"
    Usage,"//stack [-as] [count] [direction]"
       [count],"# of copies to stack"
       [direction],"The direction to stack"
       [-s],"Shift the selection to the last stacked copy"
       [-a],"Ignore air blocks"

------------

.. csv-table::
    :widths: 8, 15

    //regen,
    Description,"Regenerates the contents of the selection"
    Permissions,"worldedit.regen"
    Usage,"//regen"
    ,"This command might affect things outside the selection, if they are within the same chunk."

------------

.. csv-table::
    :widths: 8, 15

    //deform,
    Description,"Deforms a selected region with an expression"
    Permissions,"worldedit.region.deform"
    Usage,"//deform [-or] <expression...>"
       <expression...>,"The expression to use"
       [-r],"Use the game's coordinate origin"
       [-o],"Use the selection's center as origin"
    ,"The expression is executed for each block and is expected to modify the variables x, y and z to point to a new block to fetch. See also tinyurl.com/wesyntax."

------------

.. csv-table::
    :widths: 8, 15

    //hollow,
    Description,"Hollows out the object contained in this selection"
    Permissions,"worldedit.region.hollow"
    Usage,"//hollow [thickness] [pattern]"
       [thickness],"Thickness of the shell to leave"
       [pattern],"The pattern of blocks to replace the hollowed area with"
    ,"Thickness is measured in manhattan distance."

------------

.. csv-table::
    :widths: 8, 15

    //forest,
    Description,"Make a forest within the region"
    Permissions,"worldedit.region.forest"
    Usage,"//forest [type] [density]"
       [type],"The type of tree to place"
       [density],"The density of the forest"

------------

.. csv-table::
    :widths: 8, 15

    //flora,
    Description,"Make flora within the region"
    Permissions,"worldedit.region.flora"
    Usage,"//flora [density]"
       [density],"The density of the forest"

Generation Commands
~~~~~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    //hcyl,
    Description,"Generates a hollow cylinder."
    Permissions,"worldedit.generation.cylinder"
    Usage,"//hcyl <pattern> <radii> [height]"
       <pattern>,"The pattern of blocks to generate"
       <radii>,"The radii of the cylinder. 1st is N/S, 2nd is E/W"
       [height],"The height of the cylinder"

------------

.. csv-table::
    :widths: 8, 15

    //cyl,
    Description,"Generates a cylinder."
    Permissions,"worldedit.generation.cylinder"
    Usage,"//cyl [-h] <pattern> <radii> [height]"
       <pattern>,"The pattern of blocks to generate"
       <radii>,"The radii of the cylinder. 1st is N/S, 2nd is E/W"
       [height],"The height of the cylinder"
       [-h],"Make a hollow cylinder"

------------

.. csv-table::
    :widths: 8, 15

    //hsphere,
    Description,"Generates a hollow sphere."
    Permissions,"worldedit.generation.sphere"
    Usage,"//hsphere [-r] <pattern> <radii>"
       <pattern>,"The pattern of blocks to generate"
       <radii>,"The radii of the sphere. Order is N/S, U/D, E/W"
       [-r],"Raise the bottom of the sphere to the placement position"

------------

.. csv-table::
    :widths: 8, 15

    //sphere,
    Description,"Generates a filled sphere."
    Permissions,"worldedit.generation.sphere"
    Usage,"//sphere [-hr] <pattern> <radii>"
       <pattern>,"The pattern of blocks to generate"
       <radii>,"The radii of the sphere. Order is N/S, U/D, E/W"
       [-r],"Raise the bottom of the sphere to the placement position"
       [-h],"Make a hollow sphere"

------------

.. csv-table::
    :widths: 8, 15

    /forestgen,
    Description,"Generate a forest"
    Permissions,"worldedit.generation.forest"
    Usage,"/forestgen [size] [type] [density]"
       [size],"The size of the forest, in blocks"
       [type],"The type of forest"
       [density],"The density of the forest, between 0 and 100"

------------

.. csv-table::
    :widths: 8, 15

    /pumpkins,
    Description,"Generate pumpkin patches"
    Permissions,"worldedit.generation.pumpkins"
    Usage,"/pumpkins [size]"
       [size],"The size of the patch"

------------

.. csv-table::
    :widths: 8, 15

    //hpyramid,
    Description,"Generate a hollow pyramid"
    Permissions,"worldedit.generation.pyramid"
    Usage,"//hpyramid <pattern> <size>"
       <pattern>,"The pattern of blocks to set"
       <size>,"The size of the pyramid"

------------

.. csv-table::
    :widths: 8, 15

    //pyramid,
    Description,"Generate a filled pyramid"
    Permissions,"worldedit.generation.pyramid"
    Usage,"//pyramid [-h] <pattern> <size>"
       <pattern>,"The pattern of blocks to set"
       <size>,"The size of the pyramid"
       [-h],"Make a hollow pyramid"

------------

.. csv-table::
    :widths: 8, 15

    //generate,"(or //g, //gen)"
    Description,"Generates a shape according to a formula."
    Permissions,"worldedit.generation.shape"
    Usage,"//generate [-chor] <pattern> <expression...>"
       <pattern>,"The pattern of blocks to set"
       <expression...>,"Expression to test block placement locations and set block type"
       [-h],"Generate a hollow shape"
       [-r],"Use the game's coordinate origin"
       [-o],"Use the placement's coordinate origin"
       [-c],"Use the selection's center as origin"
    ,"See also https://tinyurl.com/wesyntax."

------------

.. csv-table::
    :widths: 8, 15

    //generatebiome,"(or //genbiome, //gb)"
    Description,"Sets biome according to a formula."
    Permissions,"worldedit.generation.shape.biome"
    Usage,"//generatebiome [-chor] <target> <expression...>"
       <target>,"The biome type to set"
       <expression...>,"Expression to test block placement locations and set biome type"
       [-h],"Generate a hollow shape"
       [-r],"Use the game's coordinate origin"
       [-o],"Use the placement's coordinate origin"
       [-c],"Use the selection's center as origin"
    ,"See also https://tinyurl.com/wesyntax."

Schematic and Clipboard Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /schematic,"(or /schem, //schematic, //schem)"
    Description,"Schematic commands for saving/loading areas"
    Usage,"/schematic <load|save|delete|formats|list>"

------------

.. csv-table::
    :widths: 8, 15

    /schematic load,
    Description,"Load a schematic into your clipboard"
    Permissions,"worldedit.clipboard.load, worldedit.schematic.load"
    Usage,"/schematic load <filename> [formatName]"
       <filename>,"File name."
       [formatName],"Format name."

------------

.. csv-table::
    :widths: 8, 15

    /schematic save,
    Description,"Save a schematic into your clipboard"
    Permissions,"worldedit.clipboard.save, worldedit.schematic.save"
    Usage,"/schematic save [-f] <filename> [formatName]"
       <filename>,"File name."
       [formatName],"Format name."
       [-f],"Overwrite an existing file."

------------

.. csv-table::
    :widths: 8, 15

    /schematic delete,"(or /schematic d)"
    Description,"Delete a saved schematic"
    Permissions,"worldedit.schematic.delete"
    Usage,"/schematic delete <filename>"
       <filename>,"File name."

------------

.. csv-table::
    :widths: 8, 15

    /schematic formats,"(or /schematic listformats, /schematic f)"
    Description,"List available formats"
    Permissions,"worldedit.schematic.formats"
    Usage,"/schematic formats"

------------

.. csv-table::
    :widths: 8, 15

    /schematic list,"(or /schematic all, /schematic ls)"
    Description,"List saved schematics"
    Permissions,"worldedit.schematic.list"
    Usage,"/schematic list [-dn] [-p <page>]"
       [-p <page>],"Page to view."
       [-d],"Sort by date, oldest first"
       [-n],"Sort by date, newest first"
    ,"Note: Format is not fully verified until loading."

------------

.. csv-table::
    :widths: 8, 15

    //copy,
    Description,"Copy the selection to the clipboard"
    Permissions,"worldedit.clipboard.copy"
    Usage,"//copy [-be] [-m <mask>]"
       [-e],"Also copy entities"
       [-b],"Also copy biomes"
       [-m <mask>],"Set the include mask, non-matching blocks become air"

------------

.. csv-table::
    :widths: 8, 15

    //cut,
    Description,"Cut the selection to the clipboard"
    Permissions,"worldedit.clipboard.cut"
    Usage,"//cut [-be] [leavePattern] [-m <mask>]"
       [leavePattern],"Pattern to leave in place of the selection"
       [-e],"Also cut entities"
       [-b],"Also copy biomes, source biomes are unaffected"
       [-m <mask>],"Set the exclude mask, matching blocks become air"
    ,"WARNING: Cutting and pasting entities cannot be undone!"

------------

.. csv-table::
    :widths: 8, 15

    //paste,
    Description,"Paste the clipboard's contents"
    Permissions,"worldedit.clipboard.paste"
    Usage,"//paste [-abeos] [-m <sourceMask>]"
       [-a],"Skip air blocks"
       [-o],"Paste at the original position"
       [-s],"Select the region after pasting"
       [-e],"Paste entities if available"
       [-b],"Paste biomes if available"
       [-m <sourceMask>],"Only paste blocks matching this mask"

------------

.. csv-table::
    :widths: 8, 15

    //rotate,
    Description,"Rotate the contents of the clipboard"
    Permissions,"worldedit.clipboard.rotate"
    Usage,"//rotate <yRotate> [xRotate] [zRotate]"
       <yRotate>,"Amount to rotate on the y-axis"
       [xRotate],"Amount to rotate on the x-axis"
       [zRotate],"Amount to rotate on the z-axis"
    ,"Non-destructively rotate the contents of the clipboard. Angles are provided in degrees and a positive angle will result in a clockwise rotation. Multiple rotations can be stacked. Interpolation is not performed so angles should be a multiple of 90 degrees. "

------------

.. csv-table::
    :widths: 8, 15

    //flip,
    Description,"Flip the contents of the clipboard across the origin"
    Permissions,"worldedit.clipboard.flip"
    Usage,"//flip [direction]"
       [direction],"The direction to flip, defaults to look direction."

------------

.. csv-table::
    :widths: 8, 15

    /clearclipboard,
    Description,"Clear your clipboard"
    Permissions,"worldedit.clipboard.clear"
    Usage,"/clearclipboard"

Tool Commands
~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /none,
    Description,"Unbind a bound tool from your current item"
    Usage,"/none"

------------

.. csv-table::
    :widths: 8, 15

    /info,
    Description,"Block information tool"
    Permissions,"worldedit.tool.info"
    Usage,"/info"

------------

.. csv-table::
    :widths: 8, 15

    /tree,
    Description,"Tree generator tool"
    Permissions,"worldedit.tool.tree"
    Usage,"/tree [type]"
       [type],"Type of tree to generate"

------------

.. csv-table::
    :widths: 8, 15

    /repl,
    Description,"Block replacer tool"
    Permissions,"worldedit.tool.replacer"
    Usage,"/repl <pattern>"
       <pattern>,"The pattern of blocks to place"

------------

.. csv-table::
    :widths: 8, 15

    /cycler,
    Description,"Block data cycler tool"
    Permissions,"worldedit.tool.data-cycler"
    Usage,"/cycler"

------------

.. csv-table::
    :widths: 8, 15

    /floodfill,"(or /flood)"
    Description,"Flood fill tool"
    Permissions,"worldedit.tool.flood-fill"
    Usage,"/floodfill <pattern> <range>"
       <pattern>,"The pattern to flood fill"
       <range>,"The range to perform the fill"

------------

.. csv-table::
    :widths: 8, 15

    /deltree,
    Description,"Floating tree remover tool"
    Permissions,"worldedit.tool.deltree"
    Usage,"/deltree"

------------

.. csv-table::
    :widths: 8, 15

    /farwand,
    Description,"Wand at a distance tool"
    Permissions,"worldedit.tool.farwand"
    Usage,"/farwand"

------------

.. csv-table::
    :widths: 8, 15

    /lrbuild,"(or //lrbuild)"
    Description,"Long-range building tool"
    Permissions,"worldedit.tool.lrbuild"
    Usage,"/lrbuild <primary> <secondary>"
       <primary>,"Block to set on left-click"
       <secondary>,"Block to set on right-click"

------------

.. csv-table::
    :widths: 8, 15

    //,"(or /,)"
    Description,"Toggle the super pickaxe function"
    Permissions,"worldedit.superpickaxe"
    Usage,"// [superPickaxe]"
       [superPickaxe],"The new super pickaxe state"

------------

.. csv-table::
    :widths: 8, 15

    /mask,
    Description,"Set the brush mask"
    Permissions,"worldedit.brush.options.mask"
    Usage,"/mask [mask]"
       [mask],"The mask to set"

------------

.. csv-table::
    :widths: 8, 15

    /material,"(or //material)"
    Description,"Set the brush material"
    Permissions,"worldedit.brush.options.material"
    Usage,"/material <pattern>"
       <pattern>,"The pattern of blocks to use"

------------

.. csv-table::
    :widths: 8, 15

    /range,
    Description,"Set the brush range"
    Permissions,"worldedit.brush.options.range"
    Usage,"/range <range>"
       <range>,"The range of the brush"

------------

.. csv-table::
    :widths: 8, 15

    /size,
    Description,"Set the brush size"
    Permissions,"worldedit.brush.options.size"
    Usage,"/size <size>"
       <size>,"The size of the brush"

------------

.. csv-table::
    :widths: 8, 15

    /tracemask,
    Description,"Set the mask used to stop tool traces"
    Permissions,"worldedit.brush.options.tracemask"
    Usage,"/tracemask [mask]"
       [mask],"The trace mask to set"

Super Pickaxe Commands
~~~~~~~~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /superpickaxe,"(or /sp, /pickaxe)"
    Description,"Super-pickaxe commands"
    Usage,"/superpickaxe <single|area|recursive>"

------------

.. csv-table::
    :widths: 8, 15

    /superpickaxe single,
    Description,"Enable the single block super pickaxe mode"
    Permissions,"worldedit.superpickaxe"
    Usage,"/superpickaxe single"

------------

.. csv-table::
    :widths: 8, 15

    /superpickaxe area,
    Description,"Enable the area super pickaxe pickaxe mode"
    Permissions,"worldedit.superpickaxe.area"
    Usage,"/superpickaxe area <range>"
       <range>,"The range of the area pickaxe"

------------

.. csv-table::
    :widths: 8, 15

    /superpickaxe recursive,"(or /superpickaxe recur)"
    Description,"Enable the recursive super pickaxe pickaxe mode"
    Permissions,"worldedit.superpickaxe.recursive"
    Usage,"/superpickaxe recursive <range>"
       <range>,"The range of the recursive pickaxe"

Brush Commands
~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /brush,"(or //br, //brush, /br)"
    Description,"Brushing commands"
    Usage,"/brush <sphere|cylinder|clipboard|smooth|extinguish|gravity|butcher|deform|set|forest|raise|lower|paint|apply>"

------------

.. csv-table::
    :widths: 8, 15

    /brush sphere,"(or /brush s)"
    Description,"Choose the sphere brush"
    Permissions,"worldedit.brush.sphere"
    Usage,"/brush sphere [-h] <pattern> [radius]"
       <pattern>,"The pattern of blocks to set"
       [radius],"The radius of the sphere"
       [-h],"Create hollow spheres instead"

------------

.. csv-table::
    :widths: 8, 15

    /brush cylinder,"(or /brush cyl, /brush c)"
    Description,"Choose the cylinder brush"
    Permissions,"worldedit.brush.cylinder"
    Usage,"/brush cylinder [-h] <pattern> [radius] [height]"
       <pattern>,"The pattern of blocks to set"
       [radius],"The radius of the cylinder"
       [height],"The height of the cylinder"
       [-h],"Create hollow cylinders instead"

------------

.. csv-table::
    :widths: 8, 15

    /brush clipboard,"(or /brush copy)"
    Description,"Choose the clipboard brush"
    Permissions,"worldedit.brush.clipboard"
    Usage,"/brush clipboard [-abeo] [-m <sourceMask>]"
       [-a],"Don't paste air from the clipboard"
       [-o],"Paste using clipboard origin, instead of being centered at the target location"
       [-e],"Paste entities if available"
       [-b],"Paste biomes if available"
       [-m <sourceMask>],"Skip blocks matching this mask in the clipboard"

------------

.. csv-table::
    :widths: 8, 15

    /brush smooth,
    Description,"Choose the terrain softener brush"
    Permissions,"worldedit.brush.smooth"
    Usage,"/brush smooth [radius] [iterations] [mask]"
       [radius],"The radius to sample for softening"
       [iterations],"The number of iterations to perform"
       [mask],"The mask of blocks to use for the heightmap"
    ,"Example: '/brush smooth 2 4 grass_block,dirt,stone'"

------------

.. csv-table::
    :widths: 8, 15

    /brush extinguish,"(or /brush ex)"
    Description,"Shortcut fire extinguisher brush"
    Permissions,"worldedit.brush.ex"
    Usage,"/brush extinguish [radius]"
       [radius],"The radius to extinguish"

------------

.. csv-table::
    :widths: 8, 15

    /brush gravity,"(or /brush grav)"
    Description,"Gravity brush, simulates the effect of gravity"
    Permissions,"worldedit.brush.gravity"
    Usage,"/brush gravity [-h] [radius]"
       [radius],"The radius to apply gravity in"
       [-h],"Affect blocks starting at max Y, rather than the target location Y + radius"

------------

.. csv-table::
    :widths: 8, 15

    /brush butcher,"(or /brush kill)"
    Description,"Butcher brush, kills mobs within a radius"
    Permissions,"worldedit.brush.butcher"
    Usage,"/brush butcher [-abfgnprt] [radius]"
       [radius],"Radius to kill mobs in"
       [-p],"Also kill pets"
       [-n],"Also kill NPCs"
       [-g],"Also kill golems"
       [-a],"Also kill animals"
       [-b],"Also kill ambient mobs"
       [-t],"Also kill mobs with name tags"
       [-f],"Also kill all friendly mobs (Applies the flags `-abgnpt`)"
       [-r],"Also destroy armor stands"

------------

.. csv-table::
    :widths: 8, 15

    /brush deform,
    Description,"Deform brush, applies an expression to an area"
    Permissions,"worldedit.brush.deform"
    Usage,"/brush deform [-or] <shape> [radius] [expression]"
       <shape>,"The shape of the region"
       [radius],"The size of the brush"
       [expression],"Expression to apply"
       [-r],"Use the game's coordinate origin"
       [-o],"Use the placement position as the origin"

------------

.. csv-table::
    :widths: 8, 15

    /brush set,
    Description,"Set brush, sets all blocks in the area"
    Permissions,"worldedit.brush.set"
    Usage,"/brush set <shape> [radius] <pattern>"
       <shape>,"The shape of the region"
       [radius],"The size of the brush"
       <pattern>,"The pattern of blocks to set"

------------

.. csv-table::
    :widths: 8, 15

    /brush forest,
    Description,"Forest brush, creates a forest in the area"
    Permissions,"worldedit.brush.forest"
    Usage,"/brush forest <shape> [radius] [density] <type>"
       <shape>,"The shape of the region"
       [radius],"The size of the brush"
       [density],"The density of the brush"
       <type>,"The type of tree to use"

------------

.. csv-table::
    :widths: 8, 15

    /brush raise,
    Description,"Raise brush, raise all blocks by one"
    Permissions,"worldedit.brush.raise"
    Usage,"/brush raise <shape> [radius]"
       <shape>,"The shape of the region"
       [radius],"The size of the brush"

------------

.. csv-table::
    :widths: 8, 15

    /brush lower,
    Description,"Lower brush, lower all blocks by one"
    Permissions,"worldedit.brush.lower"
    Usage,"/brush lower <shape> [radius]"
       <shape>,"The shape of the region"
       [radius],"The size of the brush"

------------

.. csv-table::
    :widths: 8, 15

    /brush paint,
    Description,"Paint brush, apply a function to a surface"
    Permissions,"worldedit.brush.paint"
    Usage,"/brush paint <shape> [radius] [density] <forest|item|set>"
       <shape>,"The shape of the region"
       [radius],"The size of the brush"
       [density],"The density of the brush"

------------

.. csv-table::
    :widths: 8, 15

    /brush apply,
    Description,"Apply brush, apply a function to every block"
    Permissions,"worldedit.brush.apply"
    Usage,"/brush apply <shape> [radius] <forest|item|set>"
       <shape>,"The shape of the region"
       [radius],"The size of the brush"

Biome Commands
~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /biomelist,"(or /biomels)"
    Description,"Gets all biomes available."
    Permissions,"worldedit.biome.list"
    Usage,"/biomelist [-p <page>]"
       [-p <page>],"Page number."

------------

.. csv-table::
    :widths: 8, 15

    /biomeinfo,
    Description,"Get the biome of the targeted block."
    Permissions,"worldedit.biome.info"
    Usage,"/biomeinfo [-pt]"
       [-t],"Use the block you are looking at."
       [-p],"Use the block you are currently in."
    ,"By default, uses all blocks in your selection."

------------

.. csv-table::
    :widths: 8, 15

    //setbiome,
    Description,"Sets the biome of your current block or region."
    Permissions,"worldedit.biome.set"
    Usage,"//setbiome [-p] <target>"
       <target>,"Biome type."
       [-p],"Use your current position"
    ,"By default, uses all the blocks in your selection"

Chunk Commands
~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /chunkinfo,
    Description,"Get information about the chunk you're inside"
    Permissions,"worldedit.chunkinfo"
    Usage,"/chunkinfo"

------------

.. csv-table::
    :widths: 8, 15

    /listchunks,
    Description,"List chunks that your selection includes"
    Permissions,"worldedit.listchunks"
    Usage,"/listchunks [-p <page>]"
       [-p <page>],"Page number."

------------

.. csv-table::
    :widths: 8, 15

    /delchunks,
    Description,"Delete chunks that your selection includes"
    Permissions,"worldedit.delchunks"
    Usage,"/delchunks"

Snapshot Commands
~~~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /restore,"(or //restore)"
    Description,"Restore the selection from a snapshot"
    Permissions,"worldedit.snapshots.restore"
    Usage,"/restore [snapshot]"
       [snapshot],"The snapshot to restore"

------------

.. csv-table::
    :widths: 8, 15

    /snapshot,"(or /snap)"
    Description,"Snapshot commands for restoring backups"
    Usage,"/snapshot <list|use|sel|before|after>"

------------

.. csv-table::
    :widths: 8, 15

    /snapshot list,
    Description,"List snapshots"
    Permissions,"worldedit.snapshots.list"
    Usage,"/snapshot list [num]"
       [num],"# of snapshots to list"

------------

.. csv-table::
    :widths: 8, 15

    /snapshot use,
    Description,"Choose a snapshot to use"
    Permissions,"worldedit.snapshots.restore"
    Usage,"/snapshot use <name>"
       <name>,"Snapeshot to use"

------------

.. csv-table::
    :widths: 8, 15

    /snapshot sel,
    Description,"Choose the snapshot based on the list id"
    Permissions,"worldedit.snapshots.restore"
    Usage,"/snapshot sel <index>"
       <index>,"The list ID to select"

------------

.. csv-table::
    :widths: 8, 15

    /snapshot before,
    Description,"Choose the nearest snapshot before a date"
    Permissions,"worldedit.snapshots.restore"
    Usage,"/snapshot before <date>"
       <date>,"The soonest date that may be used"

------------

.. csv-table::
    :widths: 8, 15

    /snapshot after,
    Description,"Choose the nearest snapshot after a date"
    Permissions,"worldedit.snapshots.restore"
    Usage,"/snapshot after <date>"
       <date>,"The soonest date that may be used"

Scripting Commands
~~~~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    /cs,
    Description,"Execute a CraftScript"
    Permissions,"worldedit.scripting.execute"
    Usage,"/cs <filename> [args...]"
       <filename>,"Filename of the CraftScript to load"
       [args...],"Arguments to the CraftScript"

------------

.. csv-table::
    :widths: 8, 15

    /.s,
    Description,"Execute last CraftScript"
    Permissions,"worldedit.scripting.execute"
    Usage,"/.s [args...]"
       [args...],"Arguments to the CraftScript"

Utility Commands
~~~~~~~~~~~~~~~~
.. csv-table::
    :widths: 8, 15

    //fill,
    Description,"Fill a hole"
    Permissions,"worldedit.fill"
    Usage,"//fill <pattern> <radius> [depth]"
       <pattern>,"The blocks to fill with"
       <radius>,"The radius to fill in"
       [depth],"The depth to fill"

------------

.. csv-table::
    :widths: 8, 15

    //fillr,
    Description,"Fill a hole recursively"
    Permissions,"worldedit.fill.recursive"
    Usage,"//fillr <pattern> <radius> [depth]"
       <pattern>,"The blocks to fill with"
       <radius>,"The radius to fill in"
       [depth],"The depth to fill"

------------

.. csv-table::
    :widths: 8, 15

    //drain,
    Description,"Drain a pool"
    Permissions,"worldedit.drain"
    Usage,"//drain [-w] <radius>"
       <radius>,"The radius to drain"
       [-w],"Also un-waterlog blocks"

------------

.. csv-table::
    :widths: 8, 15

    /fixlava,"(or //fixlava)"
    Description,"Fix lava to be stationary"
    Permissions,"worldedit.fixlava"
    Usage,"/fixlava <radius>"
       <radius>,"The radius to fix in"

------------

.. csv-table::
    :widths: 8, 15

    /fixwater,"(or //fixwater)"
    Description,"Fix water to be stationary"
    Permissions,"worldedit.fixwater"
    Usage,"/fixwater <radius>"
       <radius>,"The radius to fix in"

------------

.. csv-table::
    :widths: 8, 15

    /removeabove,"(or //removeabove)"
    Description,"Remove blocks above your head."
    Permissions,"worldedit.removeabove"
    Usage,"/removeabove [size] [height]"
       [size],"The apothem of the square to remove from"
       [height],"The maximum height above you to remove from"

------------

.. csv-table::
    :widths: 8, 15

    /removebelow,"(or //removebelow)"
    Description,"Remove blocks below you."
    Permissions,"worldedit.removebelow"
    Usage,"/removebelow [size] [height]"
       [size],"The apothem of the square to remove from"
       [height],"The maximum height below you to remove from"

------------

.. csv-table::
    :widths: 8, 15

    /removenear,"(or //removenear)"
    Description,"Remove blocks near you."
    Permissions,"worldedit.removenear"
    Usage,"/removenear <mask> [radius]"
       <mask>,"The mask of blocks to remove"
       [radius],"The radius of the square to remove from"

------------

.. csv-table::
    :widths: 8, 15

    /replacenear,"(or //replacenear)"
    Description,"Replace nearby blocks"
    Permissions,"worldedit.replacenear"
    Usage,"/replacenear <radius> [from] <to>"
       <radius>,"The radius of the square to remove in"
       [from],"The mask matching blocks to remove"
       <to>,"The pattern of blocks to replace with"

------------

.. csv-table::
    :widths: 8, 15

    /snow,"(or //snow)"
    Description,"Simulates snow"
    Permissions,"worldedit.snow"
    Usage,"/snow [size]"
       [size],"The radius of the circle to snow in"

------------

.. csv-table::
    :widths: 8, 15

    /thaw,"(or //thaw)"
    Description,"Thaws the area"
    Permissions,"worldedit.thaw"
    Usage,"/thaw [size]"
       [size],"The radius of the circle to thaw in"

------------

.. csv-table::
    :widths: 8, 15

    /green,"(or //green)"
    Description,"Converts dirt to grass blocks in the area"
    Permissions,"worldedit.green"
    Usage,"/green [-f] [size]"
       [size],"The radius of the circle to convert in"
       [-f],"Also convert coarse dirt"

------------

.. csv-table::
    :widths: 8, 15

    /extinguish,"(or /ex, /ext, //ex, //ext, //extinguish)"
    Description,"Extinguish nearby fire"
    Permissions,"worldedit.extinguish"
    Usage,"/extinguish [radius]"
       [radius],"The radius of the square to remove in"

------------

.. csv-table::
    :widths: 8, 15

    /butcher,
    Description,"Kill all or nearby mobs"
    Permissions,"worldedit.butcher"
    Usage,"/butcher [-abfgnprt] [radius]"
       [radius],"Radius to kill mobs in"
       [-p],"Also kill pets"
       [-n],"Also kill NPCs"
       [-g],"Also kill golems"
       [-a],"Also kill animals"
       [-b],"Also kill ambient mobs"
       [-t],"Also kill mobs with name tags"
       [-f],"Also kill all friendly mobs (Applies the flags `-abgnpt`)"
       [-r],"Also destroy armor stands"

------------

.. csv-table::
    :widths: 8, 15

    /remove,"(or /rem, /rement)"
    Description,"Remove all entities of a type"
    Permissions,"worldedit.remove"
    Usage,"/remove <remover> <radius>"
       <remover>,"The type of entity to remove"
       <radius>,"The radius of the cuboid to remove from"

------------

.. csv-table::
    :widths: 8, 15

    //calculate,"(or //eval, //evaluate, //calc, //solve)"
    Description,"Evaluate a mathematical expression"
    Permissions,"worldedit.calc"
    Usage,"//calculate <input...>"
       <input...>,"Expression to evaluate"

------------

.. csv-table::
    :widths: 8, 15

    //help,
    Description,"Displays help for WorldEdit commands"
    Permissions,"worldedit.help"
    Usage,"//help [-s] [-p <page>] [command...]"
       [-s],"List sub-commands of the given command, if applicable"
       [-p <page>],"The page to retrieve"
       [command...],"The command to retrieve help for"
