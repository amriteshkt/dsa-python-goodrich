from doubly_linked_base import _DoublyLinkedBase, Empty

class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._header._next._element
    
    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty("Deque is empty!")
        return self._trailer._prev.element
    
    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)
    
    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque.

        Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Remove and return the element from the back of the deque.

        Raise Empty exception if the deque is empty.
        """ 
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._delete_node(self._trailer._prev)

    # we need to print the list to see the result. It is not given in the book.
    def __str__(self):
        strng = ''
        cursor = self._header._next
        while cursor is not self._trailer:
            strng += f'{cursor._element}, '
            cursor = cursor._next
        return strng

"""Below are some tests for the methods of LinkedDeque and _DoubleLinkedBase.

Note that attributes starting with _ are nonpublic. They should not be accessed by user.
"""
if __name__ == "__main__":
    """Create an empty deque."""
    ldq = LinkedDeque()

    """As soon as we create a deque object, we have a header and a trailer."""
    print("The header element is:",ldq._header._element)
    print("The trailer element is:",ldq._trailer._element)

    """Now we add two elements to the deque."""
    ldq.insert_first('first')
    ldq.insert_last('last')
    print("The next element of header is:", ldq._header._next._element)
    print("The previous element of trailer is:", ldq._trailer._prev._element)
    print("The length of deque is:", len(ldq))

    """Now we traverse the deque from header to trailer."""
    print(ldq._header._element)     # header element
    print(ldq._header._next._element)
    print(ldq._header._next._next._element)
    print(ldq._header._next._next._next._element)   # trailer element

    """The elements of the deque can be printed by:"""
    cursor = ldq._header._next
    while cursor is not ldq._trailer:
        print(f'{cursor._element}', end=", ")
        cursor = cursor._next
    
    print('-------------------')

    """using __str__ method of LinkedDeque class, we can print the elements."""
    print(ldq)
