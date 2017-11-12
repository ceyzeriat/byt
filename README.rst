.. joystick

.. image:: https://travis-ci.org/ceyzeriat/byt.svg?branch=master
    :target: https://travis-ci.org/ceyzeriat/byt
.. image:: https://coveralls.io/repos/github/ceyzeriat/byt/badge.svg
    :target: https://coveralls.io/github/ceyzeriat/byt
.. image:: http://img.shields.io/badge/license-GPLv3-blue.svg?style=flat
    :target: https://github.com/ceyzeriat/byt/blob/master/LICENSE

:Name: byt
:Website: https://github.com/ceyzeriat/byt
:Author: Guillaume Schworer
:Version: 1.1


Although the new python3 strings/bytes-chains are arguably neater than that of python2, writing code using them, and which is compatible with both versions, is nearly a nightmare. This package attempts to gap the major discontinuity in the management of strings and bytes-chains between the two major python versions, 2.7+ and 3.5+.

Byt is a package subclassing ``str`` in python2 and ``bytes`` in python3. Its main design focus is to behaves exactly the same way, no matter the python version used. To achieve such behaviour, byt is extremely conservative: Byt objects will only work with other Byt objects (concatenate, find, replace, etc). This was (unfortunately?) necessary to ensure the somewhat lax python2 strings and bytes-chains mix-up work the same way as those of python3.

This packages also fixes some strange behaviors of python3 ``bytes`` (try ``b'test'[0:1] == b'test'[0]``) and provides new convenient methods or properties.


It is built by `Guillaume Schworer <https://github.com/ceyzeriat>`_ and licensed under
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
    >> (Byt(1,2) + Byt("\x01\x02") + Byt([1,2])).hex()
    '01 02 01 02 01 02'
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
