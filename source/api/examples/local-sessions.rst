LocalSession Examples
=====================

.. note::
    This documentation covers the API for programmatically accessing session data.
    See :doc:`/usage/general/sessions` for in-game explanations of what sessions are.
    See :doc:`../concepts/local-sessions` for the general overview of LocalSessions in API.

Concepts used in these examples: :doc:`../concepts/regions`, :doc:`../concepts/local-sessions`, :doc:`../concepts/adapters`.

Getting a LocalSession
----------------------

Before getting a LocalSession, you'll need to have the :doc:`actor <../concepts/actors>` whose session you want. Generally, actors will be obtained by adapting a platform-specific type via the :doc:`../concepts/adapters`. In the following example, we'll use a Bukkit ``org.bukkit.entity.Player`` object.

.. code-block:: java
    
    org.bukkit.entity.Player player = ...; // platform-specific player class, generally obtained from a command, event, etc.
    Player actor = BukkitAdapter.adapt(player); // WorldEdit's native Player class extends Actor
    SessionManager manager = WorldEdit.getInstance().getSessionManager();
    LocalSession localSession = sessionManager.get(actor);

Now that you have a session, there's various things you may want to do with it.

Getting a player's selection
----------------------------

.. code-block:: java

    // get a LocalSession as per the above example
    LocalSession localSession = ...;
    Region region = null; // declare the region variable
    // note: not necessarily the player's current world, see the concepts page
    World selectionWorld = localSession.getSelectionWorld();
    try {
        if (selectionWorld == null) throw new IncompleteRegionException();
        region = localSession.getSelection(selectionWorld);
    } catch (IncompleteRegionException ex) {
        actor.printError(TextComponent.of("Please make a region selection first."));
        return;
    }
    /* you can now use the region object for edits, check for a specific shape, etc. */

Accessing a player's clipboard
------------------------------

As seen in the :doc:`clipboard`, you can copy a region or load a schematic to get a clipboard, and you can paste a clipboard or save it to a schematic. For completely programmatic access, this may be enough, but sometimes you want to interact with a player's clipboard directly. In those cases, you can get or set the player's clipboard through their ``LocalSession``. 

Example 1: Setting the player's clipboard

.. code-block:: java

    LocalSession localSession = ...; // get a LocalSession as per the first example
    Clipboard clipboard = ...; // load a schematic or copy a region as in the clipboard examples
    localSession.setClipboard(new ClipboardHolder(clipboard));

Example 2: Getting the player's clipboard

.. code-block:: java

    LocalSession localSession = ...; // get a LocalSession as per the first example
    ClipboardHolder clipboard = null; // declare variable
    try {
        clipboard = localSession.getClipboard();
    } catch (EmptyClipboardException ex) {
        actor.printError(TextComponent.of("Your clipboard is empty."))
        return;
    }
    /* you can now paste the clipboard somewhere, save it to a schematic, etc. */
    // bonus example: applying rotation to the player's clipboard
    AffineTransform transform = new AffineTransform();
    clipboard.setTransform(clipboard.getTransform().combine(transform.rotateY(90)));

Storing an EditSession in history
---------------------------------    

After programmatically creating and using an :doc:`EditSession <../concepts/edit-sessions>` to change some blocks, you may want to store that edit in the player's history so that they can later use ``//undo``.

.. code-block:: java

    LocalSession localSession = ...; // get a LocalSession as per the first example
    EditSession editSession = ...; // previously used edit
    localSession.remember(editSession);
