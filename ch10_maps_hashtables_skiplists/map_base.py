from collections.abc import MutableMapping

class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class."""

    #----------------nested _Item class-----------------------
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __eq__(self, other):
            return self._key == other._key      # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)          # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key       # compare items based on their keys

if __name__ == '__main__':
    mapbase = MapBase()     # cannot instantiate MapBase because abstract methods
    # like __delitem__, __getitem__, __iter__, __len__, __setitem__ 
    # need to be defined here.