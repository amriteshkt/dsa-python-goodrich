from map_base import MapBase
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
