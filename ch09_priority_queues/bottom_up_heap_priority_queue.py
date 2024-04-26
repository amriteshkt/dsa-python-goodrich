from priority_queue_base import PriorityQueueBase
from ch7_source_code import Empty
from heap_priority_queue import HeapPriorityQueue

class HeapPriorityQueueBottomUp(HeapPriorityQueue):
    """A min-oriented priority queue implemented with a binary heap.
    
    It uses Bottom-Up Heap Construction. O(n) for adding n elements.
    _heapify method was added and __init__ method was replaced in """
    
    #---------------- new nonpublic behaviors-------------------
    
    def _heapify(self):
        start = self._parent(len(self) - 1)  # start at parent of last leaf
        for j in range(start, -1, -1):  # going to and including the root
            self._downheap(j)

    #---------------public behaviours--------------------
    # override the init method
    def __init__(self, contents=()):
        """Create a new priority queue.
    
        By default, queue will be empty. It contents is given, it should be as
        an iterable sequence of (k,v) tuples specifying the initial contents.
        """
        self._data = [self._Item(k,v) for k,v in contents]  # empty by default
        if len(self._data) > 1:
            self._heapify()

    
if __name__ == "__main__":
    
    C = [(3,'A'), (5,'B'), (21, 'V'), 
    (7, 'D'), (11, 'F'), (2, 'Z')]
    pq = HeapPriorityQueueBottomUp(C)
    print(pq)
    print(pq.min())
    print(pq.remove_min())
    print(pq)

    # now we try to store the value with maximum key at the root of heap
    # we can do this by making the keys negative.
    # 2 < 21, but -21 < -2
    C = [(-k, v) for k,v in C]
    pq = HeapPriorityQueueBottomUp(C)
    print(pq)
    print(pq.min())
    print(pq.remove_min())
    print(pq)

