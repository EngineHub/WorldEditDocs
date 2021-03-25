Local Sessions
==============
A ``LocalSession`` handles the :doc:`session data </usage/general/sessions>` of :doc:`actors <./actors>`.

That means you'll need to access a player's LocalSession if you want to use their selection, clipboard, history, etc.

To retrieve a player's (or other actor's) session, the ``WorldEdit`` class provides access to the ``SessionManager`` via the ``getSessionManager()`` method. The ``SessionManager`` allows you to retrieve sessions via the ``get(SessionOwner)`` and ``getIfPresent(SessionOwner)`` methods - the latter may return null (for example if that player has logged off and their session expired).

Using LocalSession
~~~~~~~~~~~~~~~~~~

Once you have a session object, the various methods on it will allow you to access the various session data mentioned above.

It is important to not make assumptions about the state or availability of various things held in a session. For example, the ``getClipboard()`` and ``getSelection(World)`` methods will throw exceptions if the user hasn't copied anything to their clipboard or hasn't made a selection in the provided world. If you want to require these, make sure you catch the exception and display a message to the user.

Regarding selections, note that WorldEdit allows selecting and editing cross-world (i.e. it is not bound to the world the player is in). You can check the current selection world via the ``getSelectionWorld()`` method. If you would like to limit the selection to the current world, pass the player's world to the ``getSelection(World)`` method.

Also note that a ``RegionSelector`` (``getRegionSelector(World)``) is not the same as a ``Region``. If you only need read-only access to the player's selected region, stick to ``getSelection(World)``. Selectors are only needed if you need to work with selection points, even if the region is not fully defined, or if you want to actually change the selection. Likewise, you should not mutate the ``Region`` object returned from ``getSelection(World)`` unless you subsequently update the player's selector via ``learnChanges()`` and re-send necessary information to the player via ``explainRegionAdjust(Actor player, LocalSession session)``.

For a concrete example of getting a player's selection, see the :doc:`examples page <../examples/local-sessions>`.

The other common use of a ``LocalSession`` is accessing the player's :doc:`history </usage/general/history>`. If you perform some operation on behalf a player via an :doc:`edit session <./edit-sessions>`, you can use the player's ``LocalSession`` to ``remember`` the ``EditSession``, which will allow them to ``//undo`` that operation. You can also manually ``undo`` and ``redo`` via the ``LocalSession``.

.. note::
    History manipulation via ``LocalSession`` is only for changes caused by or attributed directly to a player (i.e. the session owner). If you store an ``EditSession`` outside of player history (e.g. for an automated operation that runs independently of player action), you can undo those changes directly via the ``EditSession#undo(EditSession)`` method.