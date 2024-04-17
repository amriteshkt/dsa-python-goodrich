from map_base import MapBase

class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create and empty map."""
        self._table = list()        # list of _Item objects

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))  # repr() returns a pritanble 
                                                # representation of an object
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        # did not find match for key
        self._table.append(self._Item(k,v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key

if __name__ == "__main__":
    unsortedmap = UnsortedTableMap()

    print('length of empyt map: ', len(unsortedmap))
    
    # print(unsortedmap['key'])  # raises KeyError  # testing getitem method
    unsortedmap["key"] = 45     # testing setitem method
    print(unsortedmap["key"])

    for i in [('a', 3), ('b', 5), ('c', 7)]:
        unsortedmap[i[0]] = i[1]

    for i in unsortedmap:   # testing __iter__ method
        print(i)
    
    del unsortedmap["key"]  # testing __delitem__ method

    for i in unsortedmap:   # element with ('key', 45) has been deleted
        print(i)

    print('length of map after adding some elements: ', len(unsortedmap))

    # below is inherited from MutableMapping class from collections module
    for k,v in unsortedmap.items():
        print(k,v)
