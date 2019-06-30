============
Installation
============

Requirements
============

WorldEdit runs on a variety of Minecraft platforms which support plugins or mods. The officially supported platforms are Bukkit, Forge, Fabric, and Sponge. You will need one of these platforms to run WorldEdit.

For single-player use, you'll need to download and install either `Minecraft Forge <https://files.minecraftforge.net/>`_ or `Fabric <https://fabricmc.net/>`_, depending on what other mods you plan on using.

If you plan on running WorldEdit on a "vanilla" server, we recommend using a Bukkit implementation such as `Paper <https://papermc.io/>`_ or optionally `Spigot <https://www.spigotmc.org/>`_. (Paper is a fork of the Spigot project which adds many improvements that WorldEdit can take advantage of.)

If you plan on running WorldEdit on a modded server, you can once again use Forge, or use `Sponge <https://www.spongepowered.org/>`_, which is generally compatible with Forge mods, and also supports a wide variety of other plugins.

Note that there are unofficial implementations of WorldEdit for other platforms. 

Installation
=============

Bukkit
~~~~~~

Once you've set up your Bukkit server (instructions can be found on the respective Paper/Spigot sites), `download WorldEdit from the Bukkit dev site <http://dev.bukkit.org/bukkit-plugins/worldedit/>`_. Make sure you get the right WorldEdit download for your Minecraft version. 

1. In your server folder, create a "plugins" folder if one does not yet exist. (It should be created when you first run the server).
2. Copy the WorldEdit .jar file into the plugins folder.
3. Start your server.

Check your server log for errors. If you encounter errors, see the :doc:`FAQ <faq>` page.

Forge Single-Player
~~~~~~~~~~~~~~~~~~~

First, you'll have to install Minecraft Forge. There are many third-party launchers designed to easily install modpacks. If you're using one of those, you can add WorldEdit as a mod through the launcher interface. Otherwise, Forge will install a profile available through the official Minecraft Launcher. After installing Forge one way or the other, `download Worldedit from the CurseForge site <https://www.curseforge.com/minecraft/mc-mods/worldedit>`_. Make sure you get the right WorldEdit download for your Minecraft version.

1. If you've installed Forge as a profile in the official Minecraft launcher, follow `Mojang's instructions <https://help.mojang.com/customer/portal/articles/1480874-where-are-minecraft-files-stored->`_ for finding where your ".minecraft" folder is. If you're using a third-party launcher, this might be in a different location (consult the launcher's docs).
2. Create a "mods" folder inside the ".minecraft" folder if it doesn't yet exist (it should be created if you've run Forge once already).
3. Place the WorldEdit .jar file inside the mods folder. Start Forge from your launcher. WorldEdit should show up in the mods list.

If you encounter any errors, see the :doc:`FAQ <faq>` page.

Fabric Single-Player or Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, you'll have to install Fabric. They have instructions on `their website <https://fabricmc.net/wiki/install>`_ depending on how you'd like to install. The MultiMC instructions are recommended for single-player.

You'll also need the `Fabric API mod <https://www.curseforge.com/minecraft/mc-mods/fabric-api>`_ and add that and the WorldEdit .jar (make sure you grab the right versions) to the "loader mods" section of your MultiMC instance and check to enable them, or add the jars to your mods folder (see Forge instructions above) if you're installing in the official Mojang launcher.


Forge Server / Sponge
~~~~~~~~~~~~~~~~~~~~~

First, you'll have to install your server software of choice. For Forge, you can download the installer and run ``java -jar forge-installer.jar --installServer`` from a terminal or command prompt (search online for more comprehensive instructions). Sponge has `documentation on setting up a server <https://docs.spongepowered.org/stable/en/server/quickstart.html>`_. After installing your server software, download WorldEdit from `Curseforge, if using Forge <https://www.curseforge.com/minecraft/mc-mods/worldedit>`_ or `Ore, if using Sponge <https://ore.spongepowered.org/EngineHub/WorldEdit>`_. If you are using SpongeForge, either version of WorldEdit will work (but don't use both) - the Forge version may perform better in some cases.

1. Create a "mods" folder if it doesn't exist (it will be created automatically after running the server once).
2. Add the WorldEdit .jar file to the mods folder.
3. Start the server.

Check your server log for errors. If you encounter errors, see the :doc:`FAQ <faq>` page.