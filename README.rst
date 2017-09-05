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

The two entry points are the ``byt.Byt`` and ``byt.DByt`` classes which automatically
load depending on the python version you're running.

The only difference between ``Byt`` and ``DByt`` is that ``str(Byt)`` will print the ASCII
representation of the string while ``str(DByt)`` -- D like display -- will print its
corresponding hexadecimal values. These classes are full inter-operable.

You'll just use it like this:

::

    from byt import Byt

    >> b = Byt('hello world!')
    >> print(b)
    Byt('hello world!')
    >> print(b.hex())
    68 65 6c 6c 6f 20 77 6f 72 6c 64 21
    >> eval(repr(b)) == b
    True
    >> print(Byt('str1') + 'str2')
    TypeError: can't concat Byt to str
    >> byt.Byt('str1')[2:].ints()
    [114, 49]
    
    
    from byt import DByt
    
    >> b = DByt('hello world!')
    >> print(b)
    68 65 6c 6c 6f 20 77 6f 72 6c 64 21
    >> eval(repr(b)) == b
    True
    
    # inter-compatibility
    
    >> DByt('yes') == Byt('yes')
    True
    >> DByt('yes') + Byt('no')
    DByt('yesno')
    >> print(DByt('yes') + Byt('no'))
    79 65 73 6e 6f


Documentation
-------------

All the options are documented in the docstrings for the classes. These can be viewed in a Python shell using:

::

    >> from byt import Byt, DByt
    >> print(Byt.__doc__)
    >> print(DByt.__doc__)

or, in IPython using:

::

    >> from byt import Byt
    >> Byt?
    >> DByt?


License
-------

Copyright 2017 Guillaume Schworer

patiencebar is free software made available under the GNU General
Public License v3 or later (GPLv3+) license (see ``LICENSE``).
