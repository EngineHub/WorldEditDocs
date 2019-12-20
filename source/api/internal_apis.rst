Internal APIs
=============

Some of WorldEdit is not considered public API and may be changed at any moment without warning. Usage of this
code is not considered proper, and will receive no support.

The precise definition of internal API is anything not accessible according to standard Java access rules,
and any of the following types:

- Anything in the platform implementations. An exception is the ``*Adapter`` class for each platform.
- Anything in the following packages:
   - ``com.sk89q.worldedit.command``
   - ``com.sk89q.worldedit.internal``
- Anything explicitly marked as internal.
