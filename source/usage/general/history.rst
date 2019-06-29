History
=======

Before you dive in to using WorldEdit, you should know how to use history to undo mistakes you may make along the way.

Sessions
~~~~~~~~

When you select a region or change your preferences in-game, your information will be put into a temporary session that will be kept active as long as you stay logged in. Upon disconnecting, your session will be discarded in 10 minutes, allowing you to log back in and retain your session. Each person's session is separate when connected to a server.

Sessions contain:

    * Your current selection
    * Your history
    * Your block change limit
    * Your selected snapshot to restore from

Undo and Redo
~~~~~~~~~~~~~

Every action taken with WorldEdit, whether performed by a command or a tool, will be stored in your session's history. By default, WorldEdit stores your last 15 actions (this can be changed in the :doc:`configuration <../../config>`).

If you ever want to undo an action, you can use the ``//undo`` command. This will undo your last action. To redo it, use ``//redo``.

.. warning:: WorldEdit only records direct changes. Indirect changes such as liquids that start flowing, attached blocks (doors, signs, tall grass) popping off, and so on, will not be recorded by history. Be careful while working with these things.

As shown in the :doc:`quick start <../../quickstart>`, history commands can operate on multiple actions at once. You can use ``//undo 5``, for example, to undo your last 5 actions.

History commands also let players will permission undo or redo the actions of other players when on multiplayer. Note that thanks to the sessions described above, you can undo another player's actions for up to 10 minutes after they've logged out (and for as long as they are logged in). To do this, use ``//undo <number> <player name>``.