============
Localisation
============

WorldEdit has inbuilt support for localisation, sourced from community-contributed translations on CrowdIn. These translations are included within WorldEdit releases, so all languages are supported out of the box. WorldEdit uses the language set on each player's Minecraft client to handle translations, so every player will see text in the language that they've defined.

This means that on multilingual servers, every player can use their preferred language, rather than having to use a single server-defined language.

How to Contribute
-----------------

If some parts of WorldEdit aren't fully translated in your language, this usually means that no one has yet submitted a translation.

We use CrowdIn to facilitate translation submissions, with our CrowdIn page `available here <https://crowdin.com/project/worldedit-core>`_. Each time we cut a new WorldEdit release, we verify and pull in the new translations from the website.

Contributions to our CrowdIn are strongly appreciated, as everyone benefits from better translation coverage.

Caveats
~~~~~~~

At the time of writing, some lines of text relating to command descriptions cannot be translated due to limitations within the command library. Once this is resolved, we'll be sure to add that text into our translation system.

Custom translations
-------------------

WorldEdit supports loading user-provided translations, from the ``lang`` folder in the WorldEdit directory.

When loading languages, a priority system is used to ensure that all available localisation information is loaded. This means that the internal files are loaded first, and then any user provided translations are loaded on top of this. Therefore, if a user provided translation only provided a translation for one single string, it'd still load all of the missing entries from the internal translation data. That way your local copy only needs to contain translations for strings you are explicitly overriding, rather than having to keep it up to date with every WorldEdit release.

Loading priority occurs in the following order:

#. ``lang/strings.json`` within the WorldEdit jar file.
#. ``lang/i18n.zip`` within the WorldEdit jar file.
#. ``lang/i18n.zip`` within the WorldEdit folder within the game directory.
#. ``lang/[language-code]`` within the WorldEdit folder within the game directory.

Due to the way this priority system works, it's recommended to *only* include strings that you are actually intending to modify within your user directories, as that will allow you to automatically benefit from future improvements in later WorldEdit updates.

.. note::

  This system is mostly provided to allow you to fill in the gaps of common languages on your Minecraft server, not to fully customise messages. While you can customise messages this way, there are some limits to what can be changed such as an inability to change colours.

Zip method
~~~~~~~~~~

Within your WorldEdit jar file, you'll find a ``lang/i18n.zip`` file. Copying this to ``WorldEdit/lang/i18n.zip`` within your game directory will cause WorldEdit to additionally load from this file. You can modify the contents of the zip file, to have them take a higher priority than the zip file internal to the WorldEdit jar.

File method
~~~~~~~~~~~

Rather than copying the zip file into the ``lang`` folder, you can instead extract it. This would mean that Australian English would be in the ``lang/en-AU`` folder, or Greek would be in the ``lang/el`` folder. The "base" translations (``en-US``) would live in a ``lang/strings.json`` file, rather than having their own directory. This is because they don't come from CrowdIn, and instead are written by us when writing the plugin.
