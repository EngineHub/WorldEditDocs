Expression Syntax
=================

The WorldEdit expression parser is supposed to work like Java and related languages, with a few subtle differences:

* Final semicolons can be omitted in most cases.
* The last value in a sequence is always returned, even without a return statement.
* The binary infix ``^`` operator is a power operator instead of an xor operator and has an according priority as well.
* There is a postfix factorial operator (``!``).
* There is a binary infix near operator (``~=``).
* No objects :)

.. contents::
    :local:
    :backlinks: none

Operators
~~~~~~~~~

The expression parser uses `Java's precedence rules <https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html>`_, with the following exceptions and additions:

    * The binary power operator (``^``) is between priority 2 and 3
    * The postfix factorial operator (``!``) has a priority of 2
    * The near operator (``~=``) has a priority of 7

Binary infix
------------

These operators are put between their two operands.

.. topic:: Arithmetic

    .. csv-table::
        :widths: 3, 15

        ``+``,Addition
        ``-``,Subtraction
        ``*``,Multiplication
        ``/``,Division
        ``%``,Modulo
        ``^``,Power

.. topic:: Bitwise

    These operators interpret their operands as 32 bit integers and operate on their bits.

    .. csv-table::
        :widths: 3, 15

        ``<<``,Left-shift
        ``>>``,Right-shift

.. topic:: Logical

    These operators interpret everything greater than zero as true and everything else as false.
    They return 1 for true and 0 for false.

    .. csv-table::
        :widths: 3, 15

        ``&&``,Logical and
        ``||``,Logical or

.. topic:: Comparison

    These operators compare their operands and return 1 for true and 0 for false.

    .. csv-table::
        :widths: 3, 15

        ``<``,less than
        ``>``,greater than
        ``<=``,less or equal
        ``>=``,greater or equal
        ``==``,equal
        ``!=``,not equal
        ``~=``,near

.. topic:: Assignment

    These operators require a variable on the left side.
    Using the simple assignment operator (``=``) to assign to a non-existant variable creates a temporary variable.

    .. csv-table::
        :widths: 3, 15

        ``=``,simple assignment
        ``+=``,addition+assignment
        ``-=``,subtraction+assignment
        ``*=``,multiplication+assignment
        ``/=``,division+assignment
        ``%=``,modulo+assignment
        ``^=``,power+assignment

Prefix
------

These operators precede the expression they apply to.

.. topic:: Prefix Operators

    .. csv-table::
        :widths: 3, 15

        ``-x``,(negation)
        ``~x``,Bitwise complement (see bitwise binary operators)
        ``!x``,Logical complement (see logical binary operators)
        ``++x``,Pre-increment
        ``--x``,Pre-decrement

Postfix
-------

These operators succeed the expression they apply to.

.. topic:: Postfix Operators

    .. csv-table::
        :widths: 3, 15

        ``x!``,Factorial
        ``x++``,Post-increment
        ``x--``,Post-decrement

Ternary infix
-------------

The ternary operator is used to represent a conditional expression in a compact way::

        <condition> ? <true-branch> : <false-branch>

It works exactly like the if/else statement, except that the branches can only be single expressions.

Functions
~~~~~~~~~

.. topic:: Math Functions

    The expression parser provides the following functions from the Java Math library:

    .. csv-table::
        :widths: 3, 15

        ``abs``,"Returns the absolute value of a number."
        ``acos``,"Returns the arc cosine of a value; the returned angle is in the range 0.0 through pi."
        ``asin``,"Returns the arc sine of a value; the returned angle is in the range -pi/2 through pi/2."
        ``atan2``,"Returns the angle theta from the conversion of rectangular coordinates (x, y) to polar coordinates (r, theta)."
        ``atan``,"Returns the arc tangent of a value; the returned angle is in the range -pi/2 through pi/2."
        ``cbrt``,"Returns the cube root of a value."
        ``ceil``,"Returns the smallest (closest to negative infinity) value that is greater than or equal to the argument and is equal to a mathematical integer."
        ``cos``,"Returns the trigonometric cosine of an angle."
        ``cosh``,"Returns the hyperbolic cosine of a value."
        ``exp``,"Returns Euler's number e raised to the power of a value."
        ``floor``,"Returns the largest (closest to positive infinity) value that is less than or equal to the argument and is equal to a mathematical integer."
        ``ln``,"Returns the natural logarithm (base e) of a value."
        ``log``,"Returns the natural logarithm (base e) of a value."
        ``log10``,"Returns the base 10 logarithm (base e) of a value."
        ``max``,"Returns the greatest of the values. (supports 2 and 3 arguments)"
        ``min``,"Returns the smallest of the values. (supports 2 and 3 arguments)"
        ``rint``,"Returns the number that is closest in value to the argument and is equal to a mathematical integer."
        ``round``,"Returns the closest number to the argument"
        ``sin``,"Returns the trigonometric sine of an angle."
        ``sinh``,"Returns the hyperbolic sine of a value."
        ``sqrt``,"Returns the correctly rounded positive square root of a value."
        ``tan``,"Returns the trigonometric tangent of an angle."
        ``tanh``,"Returns the hyperbolic tangent of a value."

.. topic:: Additional Functions

    Additionally, it provides the following functions:

    .. csv-table::
        :widths: 7, 15

        "``rotate(x, y, angle)``","Rotates the given coordinate pair by the given angle, in radians."
        "``swap(x, y)``","Swaps the contents of the 2 given variables."
        "``random()``","Returns a random positive number less than 1.0."
        "``randint(max)``","Returns a random positive integer less than max."
        "``perlin(seed, x, y, z, frequency, octaves, persisence)``","Generates perlin noise with the given parameters."
        "``voronoi(seed, x, y, z, frequency)``","Generates voronoi noise with the given parameters."
        "``ridgedmulti(seed, x, y, z, frequency, octaves)``","Generated ridged multi fractal noise with the given parameters."

.. topic:: Block Query Functions

    The following functions can be used to query blocks in a world in an editing context. Note that they still use legacy ID and data, so they may have undefined behaviors for new (1.13+) blocks.

    .. csv-table::
        :widths: 8, 13

        "``query(x, y, z, type, data)``","Returns true if the block at the given coordinates has the given legacy id and data value. If type or data are variables, the id and data of the block will be assigned to that variable."
        "``queryRel(dx, dy, dz, type, data)``","Like query, except with an offset from the currently evaluated block coordinates"
        "``queryAbs(xp, yp, zp, type, data)``","Like query, except with absolute world coordinates"

.. topic:: Buffer Functions

    These functions provide access to data buffers (essentially, arrays). Two buffers are provided, one is a global shared buffer, and one is local to the expression. The function with `g` prepended accesses the global buffer, without the `g` accesses the local buffer.

    .. csv-table::
        :widths: 8, 13

        "``(g)megabuf(index)``","Returns the value of the buffer at the given index."
        "``(g)megabuf(index, value)``","Sets the value of the buffer at the given index."
        "``(g)closest(x, y, z, index, count, stride)``","Finds the index of the closest set of x,y,z values (as in, three consecutive buffer values) to the given x,y,z values within *count* iterations and *stride* space between each iteration, starting at the given index value."


Constants
~~~~~~~~~

.. topic:: Constants

    The following constants are always available, and cannot be assigned.

    .. csv-table::
        :widths: 3, 6, 10

        ``e``,2.7182818284590452354,The base of the natural logarithm
        ``pi``,3.14159265358979323846,The ratio between circumference and diameter of a circle
        ``true``,1,for boolean operations
        ``false``,0,for boolean operations

Block Statements
~~~~~~~~~~~~~~~~

Block statements are groups of statements enclosed in braces::

        { x=5; y=6; }

They are mostly used in conjunction with control structures.

Control Structures
~~~~~~~~~~~~~~~~~~

.. topic:: if/else

    .. code::

        if (<condition>) <true-branch>
        if (<condition>) <true-branch> else <false-branch>

    * ``<condition>`` is evaluated to decide which branch to execute.
    * Everything greater than zero is interpreted as true and everything else as false.
    * ``<true-code>`` and ``<false-code>`` can either be single statements delimited with a semicolon or block statements.

    **Note:** An else keyword is always associated with the last if.
    This allows elseif constructs like these::

        if (<condition 1>) <true-code 1> else if (<condition 2>) <true-code 2> else <false-code>

Loops
-----

Loops can at most loop 256 times.

.. topic:: while

    .. code::

        while (<condition>) <body>
        do <body> while (<condition>);

    * ``<condition>`` is evaluated to decide whether to continue looping.
    * ``<body>`` can either be a single statement delimited with a semicolon or a block statement.
    * do-while checks the condition after executing the body.

.. topic:: Java/C-style for

    .. code::

        for (<init>; <condition>; <increment>) <body>

    * ``<init>``, ``<condition>`` and ``<increment>`` are single expressions.
    * ``<body>`` can either be a single statement delimited with a semicolon or a block statement.

    **Execution steps**

    First, ``<init>`` is evaluated once, then, each iteration follows these steps:

    #. If ``<condition>`` evaluates as less than or equal to zero (i.e. false), the loop is aborted.
    #. ``<body>`` is executed.
    #. ``<increment>`` is executed.

.. topic:: Simple for

    .. code::

        for (<counter> = <first>, <last>) <body>

    * ``<counter>`` is a variable used to count the iterations.
    * ``<first>`` and ``<last>`` are single expressions.
    * ``<body>`` can either be a single statement delimited with a semicolon or a block statement.

    **Execution steps**

    First, an internal counter is set to ``<first>``. Then, each iteration follows these steps:

    #. If the internal counter exceeds ``<last>``, the loop is aborted.
    #. ``<counter>`` is set to the internal counter.
    #. <body> is executed.
    #. <counter> is incremented by 1.0.

    ``<first>`` and ``<last>`` are only evaluated once.
