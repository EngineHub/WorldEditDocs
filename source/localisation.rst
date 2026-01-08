============
Localisation
============

WorldEdit has inbuilt support for localisation, sourced from community-contributed translations on CrowdIn. These translations are included within WorldEdit releases, so all languages are supported out of the box. WorldEdit uses the language set on each player's Minecraft client to handle translations, so every player will see text in the language that they've defined.

This means that on multilingual servers, every player can use their preferred language, rather than having to use a single server-defined language.

How to Contribute
-----------------

If some parts of WorldEdit aren't fully translated in your language, this usually means that no one has yet submitted a translation.

We use CrowdIn to facilitate translation submissions, with our CrowdIn page `available here <https://crowdin.com/project/worldedit-core>`_. Each time we cut a new WorldEdit release, we pull in the new translations from the website.

Contributions to our CrowdIn are strongly appreciated, as everyone benefits from better translation coverage.

.. note::

    At the time of writing, some lines of text relating to command descriptions cannot be translated due to limitations within the command library. Once this is resolved, we'll be sure to add that text into our translation system.

Custom translations
-------------------

WorldEdit supports loading user-provided translations, from the ``lang`` folder in the WorldEdit directory.

When loading languages, a priority system is used to ensure that all available localisation information is loaded. This is done on a per-string basis, so it's possible for some translations to load from the WorldEdit directory, and others to load from the jar file. Therefore, if a user provided translation only provided a translation for one single string, it'd still load all of the missing entries from the internal translation data. That way your local copy only needs to contain translations for strings you are explicitly overriding, rather than having to keep it up to date with every WorldEdit release.

The search order for strings works as follows:

#. ``lang/[language-code]/strings.json`` within the WorldEdit folder within the game directory.
#. ``[language-code]/strings.json`` in ``lang/i18n.zip`` within the WorldEdit folder within the game directory.
#. ``[language-code]/strings.json`` in ``lang/i18n.zip`` within the WorldEdit jar file.
#. ``lang/strings.json`` within the WorldEdit jar file (only for the default language).

If for whatever reason a string in that language cannot be found, it'll repeat the process with a less specific language (eg, ``fr`` instead of ``fr-CA``), and finally fall back to the default language (``en``).

Due to the way this priority system works, it's recommended to *only* include strings that you are actually intending to modify within your user directories, as that will allow you to automatically benefit from future improvements in later WorldEdit updates.

.. note::

  This system is mostly provided to allow you to fill in the gaps of common languages on your Minecraft server, not to fully customise messages. While you can customise messages this way, there are some limits to what can be changed such as an inability to change colours.

As a reference for the structure of the files, you can find the ``lang/i18n.zip`` file within the WorldEdit jar file. Any custom translations will follow this same layout, either within a zip file, or in the ``lang`` folder.

Zip method
~~~~~~~~~~

Placing a zip file at ``WorldEdit/lang/i18n.zip`` within your game directory will cause WorldEdit to load from this file. Strings from this zip file will take priority over those within the WorldEdit jar file.

File method
~~~~~~~~~~~

Rather than using a zip file, you can instead directly store the locale files within folders. This would mean that Australian English would be in the ``lang/en-AU`` folder, or Greek would be in the ``lang/el`` folder. The "base" translations (``en``) would live in a ``lang/strings.json`` file, rather than having their own directory. This is because they don't come from CrowdIn, and instead are written by us when writing the plugin.
