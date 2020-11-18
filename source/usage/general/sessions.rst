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
Some of the data in a session is _persistent_, or stored offline. This includes the following:

    * Your selection wand binding
    * Your navigation wand binding
    * If CUI is currently on
    * The last script you used
    * Your default selector

The first two are particularly important. Because of how it is stored currently, changing the default wand bindings
in the configuration **will not** affect existing sessions. This means you must either wipe the ``sessions`` folder
(located inside WorldEdit's configuration folder), or change it for yourself in-game using ``/tool selwand`` or
``/tool navwand``. Note that the latter option **does not** affect other people.
