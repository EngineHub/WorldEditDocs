Actors
======

An ``Actor`` is anything that uses WorldEdit commands or certain APIs. Typically, an actor is a player, but they can
also be a command block, the console, or perhaps an entity. As should be clear, an actor does not need a location
in the world, although many actors also implement ``Locatable`` to provide this. A mod/plugin does not usually need
to provide an actor to use the WorldEdit API, but actors may be provided in certain hooks such as
``EditSessionEvent``, allowing for customization based on who/what an actor is.
