#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  
#  byt - Version-independent bytes-chains
#  Copyright (C) 2016-2017  Guillaume Schworer
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  
#  For any information, bug report, idea, donation, hug, beer, please contact
#    guillaume.schworer@gmail.com
#
###############################################################################


from binascii import hexlify
from binascii import unhexlify
from sys import version_info
PYTHON3 = version_info > (3,)


__all__ = ["Byt", "DByt", "__version__", "__major__", "__minor__", "__micro__",
           "__author__", "__copyright__", "__contributors__"]
__version__ = "1.1.0"
__major__, __minor__, __micro__ = list(map(int, __version__.split('.')))
__author__ = "Guillaume Schworer (guillaume.schworer@gmail.com)"
__copyright__ = "Copyright 2017 Guillaume Schworer"
__contributors__ = [
    # Alphabetical by first name.
]


if PYTHON3:

    class Byt(bytes):
        """Python version-independent bytes-chains object, displayed as bytes

        >>> b = Byt([33,34,35,36])
        >>> b
        Byt('!"#$')
        >>> str(b)
        '!"#$'
        """
        def __new__(cls, *args):
            l = len(args)
            if l > 1:  # many args in
                value = args
            elif l == 1:  # one arg
                value = args[0]
            else:  # empty input
                value = ''
            if isinstance(value, Byt):
                value = value.str().encode('ISO-8859-1')
            elif isinstance(value, str):
                # It's a unicode, force ascii/latin-1 encoding
                value = value.encode('ISO-8859-1')
            elif isinstance(value, int):
                value = chr(value).encode('ISO-8859-1')
            return super().__new__(cls, value)

        def __getitem__(self, pos):
            return type(self)(super().__getitem__(pos))

        def __eq__(self, other):
            if not isinstance(other, Byt):
                if isinstance(other, (str, bytes)):
                    raise TypeError("can't compare {} and {}"\
                            .format(type(self).__name__, type(other).__name__))
                else:
                    return False
            else:
                return super().__eq__(other)

        @classmethod
        def fromHex(cls, hexes):
            """
            Creates a Byt instance from a, e.g., '12 ab 34 cd' string,
            equivalent to Byt.hex() method output
            """
            return cls(unhexlify(hexes.replace(" ", "")))

        def __ne__(self, other):
            if not isinstance(other, Byt):
                if isinstance(other, (str, bytes)):
                    raise TypeError("can't compare {} and {}"\
                        .format(type(self).__name__, type(other).__name__))
                else:
                    return True
            else:
                return super().__ne__(other)

        def __str__(self):
            return self.decode('ISO-8859-1')

        def str(self):
            """
            Returns an ISO-8859-1/ASCII representation of the octets
            """
            return self.decode('ISO-8859-1')

        def __hash__(self):
            return super().__hash__()

        def __repr__(self):
            return "{}({})".format(self.__class__.__name__,
                                   repr(self.str()))

        def __iter__(self):
            for ch in super().__iter__():
                yield type(self)(ch)

        def __add__(self, txt):
            if not isinstance(txt, Byt):
                raise TypeError("can't concat {} to {}"\
                        .format(type(self).__name__, type(txt).__name__))
            return type(self)(super().__add__(txt))

        def __radd__(self, txt):
            if not isinstance(txt, Byt):
                raise TypeError("can't concat {} to {}"\
                        .format(type(self).__name__, type(txt).__name__))
            return type(self)(txt.__add__(self))

        def __mul__(self, other):
            return type(self)(super().__mul__(other))

        def __rmul__(self, other):
            return type(self)(super().__rmul__(other))

        def __contains__(self, other):
            if not isinstance(other, Byt):
                if not isinstance(other, int):
                    raise TypeError("can't compare {} to {}"\
                            .format(type(self).__name__, type(other).__name__))
                else:
                    return other in self.ints()
            else:
                return super().__contains__(other)

        def iterInts(self):
            """
            Returns the iterator of ASCII integers-codes
            """
            for ch in super().__iter__():
                yield ch

        def ints(self):
            """
            Returns the list of ASCII integers-codes
            """
            return list(self.iterInts())

        def hex(self):
            """
            Returns a hexadecimal representation of the bytes-chain
            """
            return ' '.join(super(Byt, ch).hex() for ch in self)

        def split(self, sep=None, maxsplit=-1):
            if not isinstance(sep, Byt) and sep is not None:
                raise TypeError("can't split {} with {}"\
                        .format(type(self).__name__, type(sep).__name__))
            return list(map(type(self), super().split(sep, maxsplit)))

        def rsplit(self, sep=None, maxsplit=-1):
            if not isinstance(sep, Byt) and sep is not None:
                raise TypeError("can't rsplit {} with {}"\
                        .format(type(self).__name__, type(sep).__name__))
            return list(map(type(self), super().rsplit(sep, maxsplit)))

        def replace(self, old, new, count=-1):
            if not isinstance(old, Byt) or not isinstance(new, Byt):
                raise TypeError("can't replace with non-Byt characters")
            return type(self)(super().replace(old, new, count))

        def zfill(self, width):
            return type(self)(super().zfill(width))

        def strip(self, bytes=None):
            if not isinstance(bytes, Byt) and bytes is not None:
                raise TypeError("can't strip {} in {}"\
                        .format(type(bytes).__name__, type(self).__name__))
            return type(self)(super().strip(bytes))

        def lstrip(self, bytes=None):
            if not isinstance(bytes, Byt) and bytes is not None:
                raise TypeError("can't lstrip {} in {}"\
                        .format(type(bytes).__name__, type(self).__name__))
            return type(self)(super().lstrip(bytes))

        def rstrip(self, bytes=None):
            if not isinstance(bytes, Byt) and bytes is not None:
                raise TypeError("can't rstrip {} in {}"\
                        .format(type(bytes).__name__, type(self).__name__))
            return type(self)(super().rstrip(bytes))

        def join(self, iterable_of_bytes):
            if len(iterable_of_bytes) == 0:
                return type(self)()
            for item in iterable_of_bytes:
                if not isinstance(item, Byt):
                    raise TypeError("can't join non-Byt characters")
            else:
                return type(self)(super().join(iterable_of_bytes))

        def find(self, sub, start=None, end=None):
            if not isinstance(sub, Byt):
                raise TypeError("can't find {} in {}"\
                    .format(type(sub).__name__, type(self).__name__))
            else:
                return super().find(sub, start, end)

        def count(self, sub, start=None, end=None):
            if not isinstance(sub, Byt):
                raise TypeError("can't count {} in {}"\
                        .format(type(sub).__name__, type(self).__name__))
            else:
                return super().count(sub, start, end)

        def endswith(self, suffix, start=None, end=None):
            if not isinstance(suffix, Byt):
                raise TypeError("can't search {} in {}"\
                        .format(type(suffix).__name__, type(self).__name__))
            else:
                return super().endswith(suffix, start, end)

        def startswith(self, prefix, start=None, end=None):
            if not isinstance(prefix, Byt):
                raise TypeError("can't search {} in {}"\
                        .format(type(prefix).__name__, type(self).__name__))
            else:
                return super().startswith(prefix, start, end)

else:

    from types import GeneratorType

    class Byt(str):
        """Python version-independent bytes-chains object, displayed as bytes

            >>> b = Byt([33,34,35,36])
            >>> b
            Byt('!"#$')
            >>> str(b)
            '!"#$'
            """
        def __new__(cls, *args):
            l = len(args)
            if l > 1:  # many args in
                value = args
            elif l == 1:  # one arg
                value = args[0]
                if isinstance(value, int):
                    value = chr(value)
                elif isinstance(value, Byt):
                    value = value.str()
                elif isinstance(value, GeneratorType):
                    value = list(value)
            else:  # empty input
                value = ''
            if hasattr(value, "__iter__"):
                if len(value) > 0:
                    if isinstance(value[0], int):
                        # It's a list of integers
                        value = ''.join(chr(item) for item in value)
                else:
                    value = ''
            return super(Byt, cls).__new__(cls, value)

        def __getitem__(self, pos):
            return type(self)(super(Byt, self).__getitem__(pos))

        def __getslice__(self, deb, fin):
            return type(self)(super(Byt, self).__getslice__(deb, fin))

        def __eq__(self, other):
            if not isinstance(other, Byt):
                if isinstance(other, (str, unicode)):
                    raise TypeError("can't compare {} and {}"\
                            .format(type(self).__name__, type(other).__name__))
                else:
                    return False
            else:
                return super(Byt, self).__eq__(other)

        @classmethod
        def fromHex(cls, hexes):
            """
            Creates a Byt instance from a '12 ab 34 cd' string,
            equivalent to Byt.hex() method output
            """
            return cls(unhexlify(hexes.replace(" ", "")))

        def __ne__(self, other):
            if not isinstance(other, Byt):
                if isinstance(other, (str, unicode)):
                    raise TypeError("can't compare {} and {}"\
                            .format(type(self).__name__, type(other).__name__))
                else:
                    return True
            else:
                return super(Byt, self).__ne__(other)

        def __str__(self):
            return super(Byt, self).__str__()

        def str(self):
            """
            Returns an ISO-8859-1/ASCII representation of the octets
            """
            return super(Byt, self).__str__()

        def __hash__(self):
            return super(Byt, self).__hash__()

        def __repr__(self):
            return "{}({})".format(self.__class__.__name__,
                                   repr(self.str()))

        def __iter__(self):
            for ch in super(Byt, self).__str__():
                yield type(self)(ch)

        def __add__(self, txt):
            if not isinstance(txt, Byt):
                raise TypeError("can't concat {} to {}"\
                        .format(type(self).__name__, type(txt).__name__))
            return type(self)(super(Byt, self).__add__(txt))

        def __radd__(self, txt):
            if not isinstance(txt, Byt):
                raise TypeError("can't concat {} to {}"\
                        .format(type(self).__name__, type(txt).__name__))
            return txt.__add__(self)

        def __mul__(self, other):
            return type(self)(super(Byt, self).__mul__(other))

        def __rmul__(self, other):
            return type(self)(super(Byt, self).__rmul__(other))

        def __contains__(self, other):
            if not isinstance(other, Byt):
                if not isinstance(other, int):
                    raise TypeError("can't compare {} to {}"\
                            .format(type(self).__name__, type(other).__name__))
                else:
                    return other in self.ints()
            else:
                return super(Byt, self).__contains__(other)

        def iterInts(self):
            """
            Returns the iterator of ASCII integers-codes
            """
            for ch in self.__iter__():
                yield ord(ch)

        def ints(self):
            """
            Returns the list of ASCII integers-codes
            """
            return list(self.iterInts())

        def hex(self):
            """
            Returns a hexadecimal representation of the bytes-chain
            """
            return ' '.join(hexlify(ch) for ch in self)

        def split(self, sep=None, maxsplit=-1):
            if not isinstance(sep, Byt) and sep is not None:
                raise TypeError("can't split {} with {}"\
                        .format(type(self).__name__, type(sep).__name__))
            return list(map(type(self), super(Byt, self).split(sep, maxsplit)))

        def rsplit(self, sep=None, maxsplit=-1):
            if not isinstance(sep, Byt) and sep is not None:
                raise TypeError("can't rsplit {} with {}"\
                        .format(type(self).__name__, type(sep).__name__))
            return list(map(type(self),
                            super(Byt, self).rsplit(sep, maxsplit)))

        def replace(self, old, new, count=-1):
            if not isinstance(old, Byt) or not isinstance(new, Byt):
                raise TypeError("can't replace with non-Byt characters")
            return type(self)(super(Byt, self).replace(old, new, count))

        def zfill(self, width):
            return type(self)(super(Byt, self).zfill(width))

        def strip(self, bytes=None):
            if not isinstance(bytes, Byt) and bytes is not None:
                raise TypeError("can't strip {} in {}"\
                        .format(type(bytes).__name__, type(self).__name__))
            return type(self)(super(Byt, self).strip(bytes))

        def lstrip(self, bytes=None):
            if not isinstance(bytes, Byt) and bytes is not None:
                raise TypeError("can't strip {} in {}"\
                        .format(type(bytes).__name__, type(self).__name__))
            return type(self)(super(Byt, self).lstrip(bytes))

        def rstrip(self, bytes=None):
            if not isinstance(bytes, Byt) and bytes is not None:
                raise TypeError("can't strip {} in {}"\
                        .format(type(bytes).__name__, type(self).__name__))
            return type(self)(super(Byt, self).rstrip(bytes))

        def join(self, iterable_of_bytes):
            if len(iterable_of_bytes) == 0:
                return type(self)()
            for item in iterable_of_bytes:
                if not isinstance(item, Byt):
                    raise TypeError("can't join non-Byt characters")
            else:
                return type(self)(super(Byt, self).join(iterable_of_bytes))

        def find(self, sub, start=None, end=None):
            if not isinstance(sub, Byt):
                raise TypeError("can't find {} in {}"\
                        .format(type(sub).__name__, type(self).__name__))
            else:
                return super(Byt, self).find(sub, start, end)

        def count(self, sub, start=None, end=None):
            if not isinstance(sub, Byt):
                raise TypeError("can't count {} in {}"\
                        .format(type(sub).__name__, type(self).__name__))
            else:
                return super(Byt, self).count(sub, start, end)

        def endswith(self, suffix, start=None, end=None):
            if not isinstance(suffix, Byt):
                raise TypeError("can't search {} in {}"\
                        .format(type(suffix).__name__, type(self).__name__))
            else:
                return super(Byt, self).endswith(suffix, start, end)

        def startswith(self, prefix, start=None, end=None):
            if not isinstance(prefix, Byt):
                raise TypeError("can't search {} in {}"\
                        .format(type(prefix).__name__, type(self).__name__))
            else:
                return super(Byt, self).startswith(prefix, start, end)


class DByt(Byt):
    """Python version-independent bytes-chains object, displayed as hex

    >>> b = DByt([33,34,35,36])
    >>> b
    DByt('!"#$')
    >>> str(b)
    '21 22 23 24'
    """
    def __str__(self):
        return self.hex()

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__,
                               repr(super(DByt, self).__str__()))
