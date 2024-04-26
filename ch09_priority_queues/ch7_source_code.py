class Empty(Exception):
    pass
#-----------------------------------------------------

class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage."""

    #--------------nested _Node class---------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    #-----------stack methods------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e,self._head)
        self._size += 1
    
    def top(self):
        """Return the element at the top of the stack.(Don't remove).

        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty!')
        return self._head._element
    
    def pop(self):
        """Remove and return the element from the top of the stack.

        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty!')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

#-----------------------------------------------------


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


#-----------------------------------------------------


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    #--------------nested _Node class---------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
    #------------circular queue methods----------------
    
    def __init__(self):
        """Create an empty queue."""
        self._tail = None  # we only need tail for circular queue. 
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty!')
        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove and return the first element of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty!')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element
    
    def enqueue(self, e):
        """Add an element to the back of the queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail._next  # old head becomes new tail


#-----------------------------------------------------


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


#-----------------------------------------------------

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


#-----------------------------------------------------

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    #------------nested Position class-----------------
    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # we can use == since we have defined __eq__
        
    #--------------utility method----------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    #--------------accessors--------------------------
    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    #------------mutators--------------------
    # override inherited version to return Position, rather than Node.
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p.
        """ 
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    # we add __str__ special method to print the elements of list
    def __str__(self):
        strng = ''
        node = self.first()._node
        while node is not self._trailer:
            strng += f'{node._element}, '
            node = node._next
        return 'Positional List: ' + strng


if __name__ == "__main__":

    # create an empty list
    lst = PositionalList()

    lst.add_first("first")  # it also returns the position of node containing element 'first'
    lst.add_last("last")    # it also returns the position of node containing element 'last'

    print(lst.first())  # lst.first() returns just position (Position class object) 
                        # of first element
    
    print(lst.first().element())  # use element() method of Position class to return element

    print(lst.last().element())

    print(lst.before(lst.last()).element())
    print(lst.after(lst.first()).element())

    # let's test one of the conditions of _validate method.
    print(isinstance(lst.first() , lst.Position))


    lst.add_after(lst.first(), "added after first element")
    lst.add_before(lst.last(), "added before last element")


    print(lst)

#-----------------------------------------------------
class FavoriteList:
    """List of elements ordered from most frequently accessed to least."""

    #-----------nested _Item class----------------
    class _Item:
        __slots__ = '_value', '_count'
        def __init__(self, e):
            self._value = e
            self._count = 0
    
    #---------nonpublic utilities-------------
    def _find_position(self, e):
        """Search for element e and return its Position (or None if not found)"""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk
    
    def _move_up(self, p):
        """Move item at Positoin p earlier in the list based on access count."""
        if p != self._data.first():
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count:
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p))

    #--------public methods--------------------
    def __init__(self):
        """Create an empty list of favorites."""
        self._data = PositionalList()

    def __len__(self):
        """Return number of entries of favorite list."""
        return len(self._data)
    
    def is_empty(self):
        """R3turn True if list is empty."""
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count."""
        p = self._find_position(e)
        if p is None:
            p = self._data.add_last(self._Item(e))
        p.element()._count += 1
        self._move_up(p)

    def remove(self, e):
        """Remove element e from the list of favorites."""
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)
    
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for j in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)

    def __str__(self):
        strng = ''
        walk = self._data.first()
        while walk:
            strng += f'{walk.element()._value}, '
            walk = self._data.after(walk)
        if strng != '':
            return strng
        return 'Empty List'

#----------------------------------------------------------
class FavoriteListMTF(FavoriteList):
    """List of elements ordered with move-to-front heuristic."""

    # we override _move_up to provide move-to-front semantics
    def _move_up(self, p):
        """Move accessed item at Position p to front of list."""
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    # we override top because list is no longer sorted
    def top(self, k):
        """Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
    
        #we begin by making a copy of the original list
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)

        # we repeatedly find, report, and remove element with largest count
        for j in range(k):
            # find and report next highest from temp
            highPos = temp.first()
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            # we have found element with highest count
            yield highPos.element()._value  # report element to user
            temp.delete(highPos)            # remove from temp list
