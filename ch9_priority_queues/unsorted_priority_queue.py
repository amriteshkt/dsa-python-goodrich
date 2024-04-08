from ch7_source_code import PositionalList, Empty
from priority_queue_base import PriorityQueueBase

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):
        """Return Position of item with minimum key."""
        if self.is_empty():     # inherited from base class
            raise Empty('Priority queue is empty!')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:     #  walk is None when we hit trailer node
            if walk.element() < small.element():  # __le__ defined for _Item class
                small = walk
            walk = self._data.after(walk)
        return small        # small is a Position object of PositionalList class
    
    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)
    
    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))
    
    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        """Remove and return (k,v) tuplw with minimum key."""
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
    
    def __str__(self):
        """Print the key-value pair of Priority Queue."""
        strng = ''
        walk = self._data.first()
        while walk:
            strng += f'({walk.element()._key}, {walk.element()._value}), '
            walk = self._data.after(walk)
        return strng

if __name__ == "__main__":
    
    pq = UnsortedPriorityQueue()

    for i in [(3,'A'), (5,'B'), (21, 'V'), (7, 'D'), (11, 'F'), (2, 'Z')]:
        pq.add(i[0], i[1])
    
    print(pq)

    print(pq.min())

    print(pq.remove_min())

    print(pq)
