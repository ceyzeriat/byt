Byt
===

Version-independent bytes-chains

Built by `Guillaume Schworer <https://github.com/ceyzeriat>`_. Licensed under
the GNU General Public License v3 or later (GPLv3+) license (see ``LICENSE``).


Installation
------------

Just run

::

    pip install byt

to get the most recent stable version.


Usage
-----

The only entry point is the ``byt.Byt`` class which automatically loads
depending on the python version you're running. You'll just use it like this:

::

    from byt import Byt

    b = Byt('hello world!')
    print(b)
    >> Byt('hello world!')
    print(b.hex())
    >> '68 65 6c 6c 6f 20 77 6f 72 6c 64 21'
    print(byt.Byt('str1') + 'str2')
    >> TypeError: can't concat Byt to str
    byt.Byt('str1')[2:].ints()
    >> [114, 49]


Documentation
-------------

All the options are documented in the docstrings for the ``Byt`` class. These can be viewed in a Python shell using:

::

    from byt import Byt
    print(Byt.__doc__)

or, in IPython using:

::

    from byt import Byt
    Byt?


License
-------

Copyright 2017 Guillaume Schworer

patiencebar is free software made available under the GNU General
Public License v3 or later (GPLv3+) license (see ``LICENSE``).
