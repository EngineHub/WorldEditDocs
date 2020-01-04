Adapters
========
WorldEdit works across many Minecraft modding platforms. This implies that WorldEdit's API does not use any platform's
API types, such as Bukkit's ``Player`` or Sponge's ``World``. Instead, WorldEdit has its own set of API types,
and the platform-specific library (see :ref:`api-libraries`) contains an `adapter` class to turn the platform's
API types into WorldEdit's API types, and vice versa. For example, you can turn an
``org.bukkit.entity.Player`` into a ``com.sk89q.worldedit.entity.Player`` like so

.. code-block:: java

    org.bukkit.entity.Player player = /* get a player */;
    Player wePlayer = BukkitAdapter.adapt(player);

Nearly every other WorldEdit type has a similar conversion from the platform type. These are best discovered by
looking at the methods in the adapter classes in your IDE.
