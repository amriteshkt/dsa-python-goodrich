class Empty(Exception):
    pass

class LinkedQueue:
    """FIFO queue implementation using a single linked list for storage."""
    #--------------nested _Node class---------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
    #------------queue methods----------------------

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return (but do not remove the element) at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty!')
        return self._head._element
    
    def dequeue(self):
        """Remove and return the first element of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)  # None because tail always points to None. 
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def __str__(self):
        strng = ""
        cursor = self._head
        while cursor:
            strng += f"{cursor._element},"
            cursor = cursor._next
        return strng
