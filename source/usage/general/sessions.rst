Sessions
========

When you select a region or change your preferences in-game, your information will be put into a session that
will be kept active as long as you stay logged in. Upon disconnecting, your session will be discarded in 10 minutes,
allowing you to log back in and retain your session. Each person's session is separate when connected to a server.

Sessions contain various things such as the following:

    * Your current selection
    * Your history
    * Your block change limit
    * Your selected snapshot to restore from
    * Your clipboard
    * Any currently bound tools/brushes

.. warning:: WorldEdit drops `all` sessions in single-player when leaving a world, so it is not possible to
             directly copy between worlds or retain most tool bindings after logging out in single-player.

Persistent Data
~~~~~~~~~~~~~~~
Some of the data in a session is `persistent`, or stored offline in the server files. This includes the following:

    * Your selection wand binding
    * Your navigation wand binding
    * If server-side CUI is currently on
    * The last script you used
    * Your default selector
