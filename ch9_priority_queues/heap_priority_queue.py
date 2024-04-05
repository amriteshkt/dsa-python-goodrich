from priority_queue_base import PriorityQueueBase
from ch7_source_code import Empty

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""
    
    #----------------nonpublic behaviors-------------------
    def _parent(self, j):
        return (j-1) // 2
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of list?
    
    def _has_right(self, j):
        return self._right(j) < len(self._data) # index beyond end of list?
    
    def _swap(self, i, j):
        """Swap the elements at indices i and j of array."""
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)        # recursion, trace it for better understanding

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left      # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)     # recursion, trace it

    #---------------public behaviours--------------------
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = list()     # use python list for storage

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)  # len(self._data) - 1 is index of new element
    
    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
        
        Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty('Heap Priority Queue is empty!')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        
        Raise Emtpy exception if empty.
        """
        if self.is_empty():
            raise Empty('Heap Priority Queue is empty!')
        self._swap(0, len(self._data) - 1)  # put min at end and last item at root
        item = self._data.pop()  # remove the min element
        self._downheap(0)  # so that root again stores the min
        return (item._key, item._value)

    def __str__(self):
        strng = ''
        for i in self._data:
            strng += f'({i._key}, {i._value}), '
        return strng

    
if __name__ == "__main__":
    
    pq = HeapPriorityQueue()

    for i in [(3,'A'), (5,'B'), (21, 'V'), (7, 'D'), (11, 'F'), (2, 'Z')]:
        pq.add(i[0], i[1])
    
    print(pq)

    print(pq.min())

    print(pq.remove_min())

    print(pq)
