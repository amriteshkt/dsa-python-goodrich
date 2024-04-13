from hash_map_base import HashMapBase
from unsorted_table_map import UnsortedTableMap  # this will be used as bucket

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
