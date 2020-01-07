Generation
==========

Sometimes you may want to generate forests or create spheres automatically, as doing it by hand may be too tedious. WorldEdit has a number of tools that allow you to do just that. These commands don't need a region; they use the block that you are standing in.

As most commands in WorldEdit, these commands all accept :doc:`patterns <general/patterns>` as arguments.

.. tip:: These commands actually use your "placement position", which defaults to your current location. You can use the ``//togglepos`` command to instead use your first selection point (the one selected via wand left-click, or ``//pos1``).

.. contents::
    :local:
    :backlinks: none

Cylinders
~~~~~~~~~

::

    //cyl <pattern> <radius> [height]
    //hcyl <pattern> <radius> [height]

WorldEdit is capable of producing both hollow and filled cylinders as well as hollow and filled circles. It uses a fast algorithm to generate the objects and the algorithm is capable of creating nice and symmetrical edges. The cylinders are created at your feet and extend upwards. If you are creating a circle, you simply only need to create a cylinder of height 1.

.. tip:: For better control over the edges of the shape, you can use decimal numbers for the radius.

For elliptical cylinders, you can instead specify two radii: one for the east-west axis, one for the north-south axis.

::

    //cyl <pattern> <radiusEW>,<radiusNS> [height]
    //hcyl <pattern> <radiusEW>,<radiusNS> [height]

.. topic:: Example: Creating cylinders and circles

    Creating a filled glass cylinder of radius 5 and height 10::

        //cyl glass 5 10

    Creating an elliptical hollow cylinder out of stone with radii of 5.5 and 15 and height of 1::

        //hcyl stone 5.5,15 1

Sphere
~~~~~~

::

    //sphere <pattern> <radius> [raised]
    //hsphere <pattern> <radius> [raised]

Both hollow and filled spheres can be created. By default, the center of the sphere will be the block above the one that you are standing on, but if you provide "yes" for the last parameter, the sphere will be raised by its radius so that its bottom is at your feet instead.

Like cylinders, you can create ellipsoids by specifying multiple radii (which can again be decimals). The order of the radii is north-south axis, up-down axis, and then east-west axis.

::

    //sphere <pattern> <radius>,<radius>,<radius> [raised]
    //hsphere <pattern> <radius>,<radius>,<radius> [raised]

Pyramids
~~~~~~~~

::

    //pyramid <pattern> <size>
    //hpyramid <pattern> <size>

This command creates a pyramid out of the given pattern with the specified *height*. That is, if you specify a height of say, 5, there will be 5 layers, each one block shorter than the last (in each direction, from bottom to top). The side-length of the lowest layer will be twice the height.

Forests
~~~~~~~

::

    /forestgen [size] [type] [density]

Forests can be generated with this command. The size parameter indicates the width and height of the square area to generate the forests in. The density can vary between 0 and 100, and numbers like 0.1 will work. Note that the default density (of 5) is already rather dense. The size is the apothem (radius) of a cuboid, centered on your placement position.

.. tip:: This command operates the same as the forest generator in :doc:`region operations <regions/regionops>` except this one takes a size from your placement position, instead of using your selection.

.. warning:: Depending on the platform used, WorldEdit may not be able to //undo the generation of these trees.

Pumpkin patches
~~~~~~~~~~~~~~~

::

    /pumpkins [size]

WorldEdit can generate some pumpkin patches. The size parameter is the width and height of the square area to generate the patches within, radiating out from your feet. The density of the patches is currently not adjustable.

Generating Arbitrary Shapes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    //generate <pattern> <expression>

Aliases: ``//g``, ``//gen``

Generates any shape that can be described with a mathematical formula:

    * A torus
    * Rotated cylinders
    * Jagged canyons
    * Any shape you can imagine and boil down into a formula

This uses the :doc:`expression parser <other/expressions>`.

Flags
------

* ``-r`` - Use raw coordinates, with one block equaling one unit
* ``-c`` - Shift the origin to the center of your selection, with one block equaling one unit
* ``-o`` - Shift the origin to your placement position (your position or pos1, with ``/togglepos``), with one block equaling one unit
* Without any of these flags, coordinates will be normalized to -1..1 (from selection min/max points, meaning the entire selection is 2x2x2 units), note that each axis may be a different number of blocks per unit depending on your selection skewness.

* ``-h`` - Generate a hollow shape. Blocks will only be set if they neighbour any blocks that are not part of the shape.

Variables
----------

* ``x``, ``y``, ``z`` (input) - Coordinates
* ``type``, ``data`` (input/output) - Material to use, defaults to the block/pattern entered

.. note:: Since the expression parser only takes numbers as variables, type/data variables and query functions only work with blocks that have legacy type/data values. If you need to use it with newer blocks (> MC 1.13), use a placeholder and ``//replace`` that placeholder after generating your shape. The ``<pattern>`` arg of the command is not restricted, only the expression.

The expression should return true (``> 0``) for blocks that are part of the shape and false (``<= 0``) for blocks not part of the shape. The expression is tested for each block in your selection.

Shape Examples
--------------

.. topic:: Example: Generating various shapes

    Torus of major radius 0.75 and minor radius 0.25::

        //g stone (0.75-sqrt(x^2+y^2))^2+z^2 < 0.25^2

    Gnarled hollow tree::

        //g -h oak_log (0.5+sin(atan2(x,z)*8)*0.2)*(sqrt(x*x+z*z)/0.5)^(-2)-1.2 < y

    Rainbow Torus::

        //g white_wool data=(32+15/2/pi*atan2(x,y))%16; (0.75-sqrt(x^2+y^2))^2+z^2 < 0.25^2

    Rainbow Egg::

        //g white_wool data=(32+y*16+1)%16; y^2/9+x^2/6*(1/(1-0.4*y))+z^2/6*(1/(1-0.4*y))<0.08

    A heart::

        //g red_wool (z/2)^2+x^2+(5*y/4-sqrt(abs(x)))^2<0.6

    Sine wave::

        //g -h glass sin(x*5)/2<y

    Radial cosine wave::

        //g -h glass cos(sqrt(x^2+z^2)*5)/2<y

    Circular hyperboloid::

        //g stone -(z^2/12)+(y^2/4)-(x^2/12)>-0.03


.. tip:: Want more cool shapes? Try out a program like `MathMod <https://github.com/parisolab/mathmod/releases>`_ which comes with tons of shapes and helps you make more. Note that WorldEdit uses isometric (x,y,z) formulas, not parametric (u,v,t). Also, you may have to scale your x, y, and z variable depending on your selection size and the domain of the function.


Generating Biome Shapes
~~~~~~~~~~~~~~~~~~~~~~~

Just like the generate command, you can use an expression to set a biome in a particular shape. This uses the same syntax as above, but takes a biome id instead of a pattern. It currently only uses ``x`` and ``z`` as inputs.

.. note:: As of Minecraft 1.15, biomes are stored in 3 dimensions. However, neither Minecraft nor WorldEdit can fully use this format yet, so biomes are still just treated as full columns.