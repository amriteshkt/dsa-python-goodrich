class Empty(Exception):
    pass

class _DoublyLinkedBase:  # nonpublic class.
    """A base class providing a doubly linked list representation.
    
    This class will be inherited by LinkedDeque class and PositionalList class.
    """

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and RETURN new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self, node):
        """Delete nonsentinel node from the list and RETURN its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None  # deprecate the node
        return element

if __name__ == "__main__":
    # create an empty doubly linked list.
    newobj = _DoublyLinkedBase()

    print("The length of empty object is:", len(newobj))
    # what is the header element of empty doubly linked list?
    print("The header element is:", newobj._header._element)
    # what is the trailer element of empty doubly linked list?
    print("The trailer element is:",newobj._trailer._element)
    # what is the element of next node of empty doubly linked list?
    print("The element of next node of header is:", newobj._header._next._element)
    # what is the element of previous node of empty doubly linked list?
    print("The element of previous node of trailer is:",newobj._trailer._prev._element)

    # now we insert an element between sentinels (header and trailer).
    newobj._insert_between('first', newobj._header, newobj._trailer)
    print("The length of object after adding an element is: ", len(newobj))
    print("The element of next node of header is:",newobj._header._next._element)
    print("The element of previous node of trailer is:", newobj._trailer._prev._element)

    # now we delete the element we just inserted.
    # we have to put the node that we want to remove as parameter.
    # node containing the 'first' element can be identified by self._header._next, or
    # self._trailer._prev as it is a single node between header and trailer.
    newobj._delete_node(newobj._header._next)

    print("The length of object after removing the element is:", len(newobj))