Developer API
=============

.. toctree::
    :maxdepth: 2
    :hidden:

    concepts/index
    examples/index
    internal-apis

WorldEdit provides a stable public interface for other mods and plugins to build off of. It provides
platform-independent interfaces and classes for working with Minecraft blocks, biomes, and worlds.
Limited entity support is present as well.

.. _api-libraries:

API Libraries
-------------

You can get the API via a `Maven repository`_, compatible with Maven_, Gradle_, sbt_, and many other build systems.
The repository is `<https://maven.enginehub.org/repo/>`_, and WorldEdit is under the group ``com.sk89q.worldedit``.
Depending on which parts of the API you need, choose one of the following names:

- ``worldedit-core``: The core APIs. Does not depend on any platform, and provides no conversion classes.
- ``worldedit-bukkit``: The Bukkit implementation. Depends on Bukkit API and provides conversion between Bukkit types
  and WorldEdit types using ``BukkitAdapter``.
- ``worldedit-fabric-mcXYZ``: The Fabric implementation. Depends on Fabric API and provides conversion between Fabric
  types and WorldEdit types using ``FabricAdapter``. Replace XYZ with the appropriate Minecraft version.
- ``worldedit-neoforge-mcXYZ``: The NeoForge implementation. Depends on NeoForge and provides conversion between NeoForge types
  and WorldEdit types using ``ForgeAdapter``. Replace XYZ with the appropriate Minecraft version.
- ``worldedit-sponge-mcXYZ``: The Sponge implementation. Depends on Sponge API and provides conversion between Sponge
  types and WorldEdit types using ``SpongeAdapter``. Replace XYZ with the appropriate Minecraft version.
  (Only supports up to 1.12.2 due to Sponge only being available up to that version.)
- ``worldedit-cli``: The command-line implementation. Probably not very useful as a dependency, but could be used
  to automatically run WorldEdit outside of Minecraft.

The version is dependent on the version of Minecraft you are building for. 6 is for Minecraft versions
1.12.2 and below, and 7 is for 1.13 and above. Support is only offered for the latest WorldEdit version, and the
latest Minecraft version, but generally the API is similar enough across versions that examples are very similar.
These documents also only cover the latest version of WorldEdit, although old versions may be reached using the
navigator in the bottom right. The exact version matches the version on the downloads page, or you can browse
the repository itself: https://maven.enginehub.org/repo/com/sk89q/worldedit/worldedit-core/

To get started with the API, read :doc:`concepts/index`. Some common API usages are documented in
:doc:`examples/index`.
When developing, take note of :doc:`internal-apis` to ensure you're using supported APIs.
If you need the Javadocs, they are hosted at
`<https://docs.enginehub.org/javadoc/com.sk89q.worldedit/worldedit-core/7.3.0/>`_.

.. _Maven repository: https://maven.apache.org/repositories/layout.html
.. _Maven: https://maven.apache.org/
.. _Gradle: https://gradle.org/
.. _sbt: https://www.scala-sbt.org/

