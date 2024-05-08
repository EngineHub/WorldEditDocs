============
Installation
============

.. contents::
    :local:
    :backlinks: none

Requirements
============

WorldEdit runs on the Java edition of Minecraft, either on your single player/local game or a dedicated server.

**WorldEdit can't be used on Realms, Windows 10 Edition, Bedrock Edition, or Pocket Edition versions.** These versions of Minecraft have limited or no mod support. Note that "Windows 10 Edition" refers to a specific Edition of Minecraft, not the Java Edition running on a Windows 10 computer.

Before you install WorldEdit, you will first have to install a "mod loader" like NeoForge, Fabric, Spigot, Bukkit, or Sponge. We'll advise you to choosing your mod loader below.

Choosing a Mod Loader
~~~~~~~~~~~~~~~~~~~~~

If you want to use WorldEdit on your single-player/local game, we recommend one of two choices:

* `NeoForge <https://https://neoforged.net/>`_ 
* Or alternatively, `Fabric <https://fabricmc.net/>`_

On the other hand, if you are running a Minecraft server, you can use

* `Paper <https://papermc.io/>`_ (recommended over Spigot because it has improvements WorldEdit can use)
* `Spigot <https://www.spigotmc.org/>`_
* NeoForge (recommended if you are using other NeoForge mods)
* `Sponge <https://www.spongepowered.org/>`_ (also compatible with Forge mods)

Note: Paper and Spigot use its own set of mods (commonly called "plugins") that are mostly incompatible with mods for NeoForge, Fabric, and Sponge. You *may* want to research what other mods/plugins that you may want (generally, Paper and Spigot have much more server administration/"server-ready gameplay mods" - which run completely on the server - and NeoForge, Fabric, and Sponge have more major gameplay mods - which generally require client installation). Regardless, WorldEdit is extremely unique in that it works as a mod for both 😊, so you can just pick the one that seems the easiest and roll with it. 🤙

Installation Step-by-step
=========================

Bukkit / Spigot / Paper
~~~~~~~~~~~~~~~~~~~~~~~

Once you've set up your Bukkit-based server (instructions can be found on the respective Paper/Spigot sites), `download WorldEdit from Modrinth <https://modrinth.com/plugin/worldedit/versions?l=bukkit>`_. Make sure you get the right WorldEdit download for your Minecraft version.

1. In your server folder, create a "plugins" folder if one does not yet exist. (It should be created when you first run the server).
2. Move the WorldEdit .jar file into the plugins folder.
3. Start your server.

Check your server log for errors. If you encounter errors, see the :doc:`FAQ <faq>` page.

NeoForge Single-Player
~~~~~~~~~~~~~~~~~~~

First, you'll have to install NeoForge. There are many third-party launchers designed to easily install modpacks. If you're using one of those, you can add WorldEdit as a mod through the launcher interface. Otherwise, NeoForge will install a profile available through the official Minecraft Launcher. After installing NeoForge one way or the other, `download WorldEdit from Modrinth <https://modrinth.com/plugin/worldedit/versions?l=neoforge>`_. Make sure you get the right WorldEdit download for your Minecraft version and platform.

1. If you've installed NeoForge as a profile in the official Minecraft launcher, follow `Mojang's instructions <https://help.minecraft.net/hc/en-us/articles/360035131551-Where-are-Minecraft-files-stored->`_ for finding where your ".minecraft" folder is. If you're using a third-party launcher, this might be in a different location (consult the launcher's docs).
2. Create a "mods" folder inside the ".minecraft" folder if it doesn't yet exist (it should be created if you've run NeoForge once already).
3. Place the WorldEdit .jar file inside the mods folder. Start NeoForge from your launcher. WorldEdit should show up in the mods list.

If you encounter any errors, see the :doc:`FAQ <faq>` page.

Fabric Single-Player or Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, you'll have to install Fabric. They have instructions on `their website <https://fabricmc.net/wiki/install>`_ depending on how you'd like to install. The MultiMC instructions are recommended for single-player.

Then, `download WorldEdit from Modrinth <https://modrinth.com/plugin/worldedit/versions?l=fabric>`_. Make sure you get the right WorldEdit download for your Minecraft version and platform (Forge builds are also there - make sure you grab the right one).

On Minecraft 1.14.x versions, you will also need to install the `Fabric API mod <https://modrinth.com/mod/fabric-api/versions>`_. This is not required for 1.15+.

Add the WorldEdit .jar to the "loader mods" section of your MultiMC instance and check to enable it, or add the jar to your mods folder (see NeoForge instructions above) if you're installing in the official Mojang launcher.

NeoForge Server / Sponge
~~~~~~~~~~~~~~~~~~~~~

First, you'll have to install your server software of choice. For NeoForge, you can download the installer and run ``java -jar neoforge-installer.jar --installServer`` from a terminal or command prompt (search online for more comprehensive instructions). Sponge has `documentation on setting up a server <https://docs.spongepowered.org/stable/en/server/quickstart.html>`_. After installing your server software, download WorldEdit from `Curseforge, if using NeoForge <https://www.curseforge.com/minecraft/mc-mods/worldedit/files>`_ or `Ore, if using Sponge <https://ore.spongepowered.org/EngineHub/WorldEdit>`_. 

1. Create a "mods" folder if it doesn't exist (it will be created automatically after running the server once).
2. Add the WorldEdit .jar file to the mods folder.
3. Start the server.

Check your server log for errors. If you encounter errors, see the :doc:`FAQ <faq>` page.

.. include:: cuitip.rst
