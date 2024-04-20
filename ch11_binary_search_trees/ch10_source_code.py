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

#-----------------------------------------------


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
#----------------------------------------------------------
from random import randrange

class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self._table = cap*[None]
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
        # [(a*i + b) mod p] mod N
        # here i is hash(k) which generates hash code
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)    # concrete implementation pending

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:         # keep load factor <= 0.5
            self._resize(2*len(self._table) - 1)    # 2^x -1 is often prime
    
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1
    
    def _resize(self, c):           # same as dynamic array implementation
        old = list(self.items())
        self._table = c*[None]
        self._n = 0
        for (k,v) in old:
            self[k] = v
#----------------------------------------------------------


class ChainHashMap(HashMapBase):
    """Hash map implementation with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]        # bucket is an UnsortedTableMap instance
    
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()  # create a new bucket at j in table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:   # key was new to the table
            self._n += 1
        
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key

if __name__ == '__main__':
    
    chainhashmap = ChainHashMap()
    chainhashmap['a'] = 1
    print(chainhashmap['a'])

    for i in [('b', 2), ('c', 3), ('d', 4), ('e', 5)]:
        chainhashmap[i[0]] = i[1]
    
    for k,v in chainhashmap.items():
        print(k,v)

    del chainhashmap['b']
    print('after deleting "b" we have: ')
    for k,v in chainhashmap.items():
        print(k,v)
    
    # notice how the elements in chainmap.items() print in different order every
    # time we run this program.
    # Why? Because we use random a, b in __init__ of HashMapBase(), which gives
    # random values of j = _hash_function which is the index of hash map table.
    print('\nvisualise how the table(python list) \
stores buckets(UnsortedTableMap objects)\n')
    for bucket in chainhashmap._table:  # bucket is an UnsortedTableMap instance
        if bucket is not None:
            print(list(bucket.items()))
            if len(bucket.items()) > 1:
                print('\tcollision has happened!')
        else:
            print(bucket)
    # an empty [] represents the key 'b' that was deleted.
    print('\nlength of chainhashmap is: ', len(chainhashmap))

    # test __iter__ method
    for key in chainhashmap:
        print(key)

#----------------------------------------------

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    _AVAIL = object()  # sentinal marks locations of previous deletions.

    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.

        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j
                if self._table[j] is None:
                    return (False, firstAvail)
            elif k == self._table[j]._key:
                return (True, j)                # found a match
            j = (j+1) % len(self._table)        # keep looking (cyclically)
    
    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[s]._value
    
    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k,v)    # insert new item
            self._n += 1
        else:
            self._table[s]._value = v           # override existing
    
    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Erro: ' + repr(k))
        self._table[s] = ProbeHashMap._AVAIL    # mark as vacated

    def __iter__(self):
        for j in range(len(self._table)):       # scan entire table
            if not self._is_available(j):
                yield self._table[j]._key

if __name__ == '__main__':
    probehashmap = ProbeHashMap()
    print(probehashmap._table)

    for i in [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5)]:
        probehashmap[i[0]] = i[1]

    print(probehashmap._table)
    print(list(probehashmap.items()))

    for item in probehashmap._table:   # _Item object has been stored in hash table
        if item is not None and item is not probehashmap._AVAIL:
            print(item._key, item._value)
        else:
            print(item)
    
    del probehashmap['C']
    # after deleting an _Item with key = 'C', we have an object() object at that place
    for item in probehashmap._table:   # _Item object has been stored in hash table
        if item is not None and item is not probehashmap._AVAIL:
            print(item._key, item._value)
        else:
            print(item)
#-------------------------------------------------

class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""

    #-------------nonpublic behaviors-----------------
    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k.

        Return high + 1 if no such item qualifies.

        That is, j will be returned such that:
            all items of slice table[low:j] have key < k
            all items of slice table[j:high+1] have key >= k
        """
        if high < low:
            return high + 1         # no element qualifies
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid          # foudn exact match
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)

    #-------------public behaviors-------------
    def __init__(self):
        """Create an empty map."""
        self._table = list()

    def __len__(self):
        """Return number of items in the map."""
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyErro if not found)."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v                   # reassign value
        else:
            self._table.insert(j, self._Item(k,v))      # adds new item

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum."""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate keys of the map ordered from maximum to minimum."""
        for item in reversed(self._table):
            yield item._key
    
    def find_min(self):
        """Return (key, value) pair with minimum key (or None if empty)."""
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """Return (key, value) pair with maximum key (or None if empty)."""
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """Return (key, value) pair with least key greater than or equal to k."""
        j = self._find_index(k, 0, len(self._table) - 1)    # j's key >= k
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        """Return (key, value) pair with greatest key strictly less than k."""
        j = self._find_index(k, 0, len(self._table) - 1)    # j's key >= k
        if j > 0:
            return (self._table[j-1]._key, self._table[j-1]._value)
        else:
            return None

    def find_gt(self, k):
        """Return (key, value) pair with least key strictly greater than k."""
        j = self._find_index(k, 0, len(self._table) - 1)    # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all (key, value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)    # find first result
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1

#----------------------------------------------------------


class CostPerformanceDatabase:
    """Maintain a database of maximal (cost, performance) pairs."""

    def __init__(self):
        """Create an empty database."""
        self._M = SortedTableMap()      # or a more efficient sorted map

    def best(self, c):                  # O(log n)
        """Return (cost, performance) pair with largest cost not exceeding c.

        Return None if there is no such pair.
        """
        return self._M.find_le(c)

    def add(self, c, p):                # O(n)
        """Add new entry with cost c and performance p."""
        # determine if (c,p) is dominated by an existing pair
        other = self._M.find_le(c)      # other is at least as cheap as c
        if other is not None and other[1] >= p:  # if its performance is as good
            return                      # (c,p) is dominated by other, so ignore
        self._M[c] = p                  # else, add (c,p) to database
        # and now remove any pair that are dominated by (c,p)
        other = self._M.find_gt(c)      # other more expensive than c
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)
#---------------------------------------------------------

class MultiMap:
    """A multimap class built upon use of an underlying map for storage."""
    _MapType = dict             # Map type; can be redefined by subclass

    def __init__(self):
        """Create a new empty multimap instance."""
        self._map = self._MapType()     # create map instance for storage
        self._n = 0

    def __iter__(self):
        """Iterate through all (k,v) pairs in multimap."""
        for k,secondary in self._map.item():
            for v in secondary:
                yield (k,v)

    def add(self, k, v):
        """Add pair (k,v) to multimap."""
        container = self._map.setdefault(k, [])
        # setdefault(k,d): if k is present in D, return its existing  v
        # if k is not in D, set D[k] = d, and return d
        container.append(v)
        self._n += 1

    def pop(self, k):
        """Remove and return arbitrary (k,v) with key k (or raise KeyError)."""
        secondary = self._map[k]        # may raise KeyError
        v = secondary.pop()
        if len(secondary) == 0:
            del self._map[k]            # no pairs left
        self._n -= 1
        return (k,v)

    def find(self, k):
        """Return arbitrary (k,v) pair with given key (or raise KeyError)."""
        secondary = self._map[k]        # may raise KeyError
        return (k, secondary[0])
    
    def find_all(self, k):
        """Generate iteration of all (k,v) pairs with given key."""
        secondary = self._map.get(k, [])    # empty list by default
        for v in secondary:
            yield (k,v)

#-------------------------------------------------------
