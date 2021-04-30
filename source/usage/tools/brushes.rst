Brushes
=======

Brush tools are general more designed for building, sculpting, and painting than the general utility :doc:`tools <tools>`. Like the rest of the tools, they are bound to an item by using the command, and are activated by right-clicking (or left clicking, for those with two actions). They are unbound with the ``/brush none`` command.

Brushes have a few unique settings available to them. Brushes allow you to choose a mask, size, pattern, and range. These allow fine-tuning how you build and paint.

.. contents::
    :local:
    :backlinks: none
    :depth: 2

Brush Listing
~~~~~~~~~~~~~

Sphere brush
------------

::

    /brush sphere [-h] <pattern> [radius]
    /br s [-h] <pattern> [radius]

The sphere brush, as its name suggests, creates sphere at the target point. The ``-h`` flag will make a hollow sphere.

Cylinder brush
--------------

::

    /brush cylinder [-h] <pattern> [radius] [height]
    /br cyl [-h] <pattern> [radius] [height]

The cylinder brush creates cylinders of the given radius and height. ``-h`` is hollow as usual.

Set brush
---------

::

    /brush set <shape> [size] <pattern>

The set brush can set spheres, cylinders, or cuboids of the given size and pattern. It is mostly redundant to the previous two brushes, unless you need a cube.

Clipboard brush
---------------

::

    /brush clipboard [-aoeb] [-m <mask>]

The clipboard brush uses your clipboard as a shape and places it at the target location each brush activation. The ``aebm`` flags all work just like the :doc:`paste command <../clipboard>`. The ``-o`` flag is a bit different - it makes the clipboard paste at the brush's location as the origin. Otherwise, the clipboard is centered to that location. Choose your relative position carefully when copying a clipboard for use with this brush.


Smooth brush
------------

::

    /brush smooth [radius] [iterations] [mask]

Smoothes the area, just like the ``//smooth`` command explained in :doc:`region ops <../regions/regionops>`. You can specify the mask of blocks to consider while building a heightmap (this is separate from the mask of blocks that will be affected).

Gravity brush
-------------

::

    /brush gravity [radius] [-h]

The gravity brush will move blocks downwards within the affected brush area. Using the ``-h`` flag will start from the max y, instead of from the top of the brush area.

Forest brush
------------

::

    /brush forest <shape> [radius] [density] <tree type>

Like the ``//forest`` and ``//forestgen`` commands, this brush plants trees, using the shape, radius, density, and tree type provided.

Extinguish brush
----------------

::

    /brush extinguish [radius]
    /br ex [radius]

A handy shortcut for a sphere brush of air masked to fire blocks, in case something is burning and you don't have time to type in 3 commands to put it out.

Butcher brush
-------------

::

    /brush butcher [radius] [-pngabtfr]
    /br kill [radius] [-pngabtfr]

Just like the ``//butcher`` :doc:`utility command <../utilities>`, the butcher brush kills entities in its area. Note that the radius is strictly cylindrical, but goes from minimum to maximum world height. It is not a sphere. By default, it only kills hostile mobs. The flags can be specified to determine what other mobs will be butchered.

.. include:: ../butcherflags.rst

Deform brush
------------

::

    /brush deform <shape> [size] [expression] [-ro]

Just like the ``//deform`` command described in :doc:`region operations <../regions/regionops>`, this brush will apply an expression to blocks within the area given by the shape and radius. Also just like the command, ``-r`` uses raw coordinates, and ``-o`` offsets from your placement position. The default is the brush target point.

Raise Brush
^^^^^^^^^^^

::

    /brush raise <shape> [size]

A special case of the deform brush which uses the expression ``y-=1``.

Lower Brush
^^^^^^^^^^^

::

    /brush lower <shape> [size]

A special case of the deform brush which uses the expression ``y+=1``.

Biome brush
-------------

::

    /brush biome <shape> [radius] <biomeType>

Sets the biome within the area given by the shape and radius. Keep in mind that since 1.15 the biomes are 3D and the smallest area you can change is a 4x4x4 cuboid. Changing the biome in a large area can be slow. Effects can't be seen until you rejoin the world.

Brush Settings
~~~~~~~~~~~~~~

These commands modify the settings on your *currently selected* brush only. Each brush you have bound has its own settings.

Not all settings are used by all brushes - the clipboard brush doesn't have a size setting (it uses your clipboard's size), the butcher brush doesn't have a mask or material (it affects entities, not blocks), and so on.

Mask
----

::

    /mask [mask]
    /mask

Sets a :doc:`mask <../general/masks>` on your current brush, which restricts what blocks will be affected by it. Not specifying a mask will disable it for your brush, allowing it to affect everything again. Note that if you already have a global mask set with ``//gmask``, it will be combined with this one.

Size
----

::

    /size [size]

Sets the size of the brush. Generally, this means the radius or affected area. Note that the maximum size is :doc:`configurable <../../config>`.

Material
--------

::

    /material <pattern>

Sets the pattern used by the brush.

Range
-----

::

    /range <range>

Sets the maximum range that the brush will try to build at. Note that with a short enough range, brushes *will build in mid-air* if they can't find a block in your ray trace.

Trace Mask
----------

::

    /tracemask [mask]
    /tracemask

Sets the mask used for the ray tracer. By default, brushes will perform their action on the first non-air block (or when the trace hits the range, whichever comes first). By setting the tracemask, you can make brushes trace through any block you choose. For example, ``/tracemask #solid`` will go through non-solid blocks, such as water. This is useful for building underwater, through walls, and whatever else.
