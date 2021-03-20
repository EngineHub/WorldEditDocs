Selection Examples
==================

.. note::
    This documentation covers the API for using selections.
    See :doc:`/usage/regions/selections` for in-game usage.

Concepts used in these examples: :doc:`../concepts/regions`, :doc:`../concepts/local-sessions`.

Getting a player's selection
----------------------------

.. code-block:: java

    Region region = null;
    SessionManager manager = WorldEdit.getInstance().getSessionManager();
    LocalSession localSession = sessionManager.get(actor);
    // note: as explained above, not necessarily the player's  current world
    World selectionWorld = localSession.getSelectionWorld();
    try {
        if (selectionWorld == null) {
            throw new IncompleteRegionException();
        }
        region = localSession.getSelection(selectionWorld);
    } catch (IncompleteRegionException ex) {
        actor.printError(TextComponent.of("Please make a region selection first."));
        return;
    }
