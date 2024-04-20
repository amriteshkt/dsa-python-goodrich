class Tree:
    """Abstract base class representing a tree structure."""

    #-------nested Postion class--------------
    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')
        
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not(self == other)
    
    #-------abstract methods that concrete subclass must support--------
    def root(self):
        """Return Position representing the tree's root(or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')
    
    def parent(self, p):
        """Return Position representing p's parent(or None if p is root)."""
        raise NotImplementedError('must be implemeted by subclass')
    
    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')
    
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')
    
    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')
    
    #-------concrete methods implemented in this class------------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p
    
    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0
    
    def depth(self, p):
        """Return the number of level separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))  # using recursion

    # def _height1(self):  #nonpublic
    #     """Return the height of tree."""
    #     return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    #  we won't use it because it is inefficient. O(n^2)
    
    def _height2(self, p):  #nonpublic
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))  # O(n)
        
    def height(self, p=None):   # for public
        """Return the height of the subtree rooted at Position p.\
            
        if p is None, return the height of the entire tree.
        """
        if p in None:
            p = self.root()
        return self._height2(p)

    # tree traversal algorithms
    # see the if __name__ == "__main__" of linked_binary_tree for explanantion.

    # 1. preorder traversal
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()): # this fn is defined below
                yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    # 2. postorder traversal
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    # 3. breadth-first traversal
    # commenting out because we first need to import LinkedQueue class

    # def breadthfirst(self):
    #     if not self.is_empty():
    #         fringe = LinkedQueue()   # we need to import it from ch7 notes
    #         fringe.enqueue(self.root())
    #         while not fringe.is_empty():
    #             p = fringe.dequeue()
    #             yield p
    #             for c in self.children(p):
    #                 fringe.enqueue(c)
#--------------------------------------------------------


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    #--------additional abstract methods-------------
    def left(self, p):
        """Return a Position representing p's left child.
        
        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child.
        
        Return None if p does not have a right child."""
        raise NotImplementedError('must be implemented by subclass')

    #-------concrete methods implemented in this class---------
    def sibling(self, p):
        """Return a Position representing p's sibling(or Noo=ne if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None     # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)   # can return None
            else:
                return self.left(parent)    # can return None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # binary tree traversal algorithms

    # 1. inorder traversal

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    
    def _subtree_inorder(self, p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
        
    # evaluate an expression tree 
    def evaluate(self):
        """Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())
    
    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:
                return left_val * right_val

#--------------------------------------------------------


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):  #why not inherit directly from Tree.
        """An astraction representing the location of a single element."""
        def __init__(self, container, node):  # container is the LinkedBinaryTree object
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
        
        def element(self):
            """Return the element stored at this position."""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        # this position class has only inherited __ne__ from the Positon in Tree class
        # if we didn't use inheritance for Position, then also it would be okay, we would
        # just need to add __ne__ in Position class in this script

    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # THIS IS WHAT HAPPENS WHEN WE DELETE A NODE, WE SET 
                                        # node.parent = node (convention for deprecating node)
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        """Return Position instance for given node(or None if no node)."""
        return self.Position(self, node) if node is not None else None

    #------linked binary tree constructor-----------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0
    
    #-------public accessors---------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)
    
    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        
        Raise ValueError if tree nonempty.
        """
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)  # essentially it is self._Node(e, None, None, None)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)            # node is parent
        return self._make_position(node._left)
    
    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)       # node is parent
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at Position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
        
        Return the element that had been stored at Position p.
        Raise valueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent  # child's grandparent becomes parent
        if node is self._root: 
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size += 1
        node._parent = node     # see the validate(p) method, convention for deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():   # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None     # set t1 instance to empty
            t1._size = 0
        
        if not t2.is_empty():   # attach t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None     # set t2 instance to empty
            t2._size = 0

    

if __name__ == "__main__":
    # Testing for differenct tree traversal algorithms.
    # since we have concrete implementation of BinaryTree ADT, we can test different 
    # traversal algorithms and place them in different ADTs that we have created.
    LBT = LinkedBinaryTree()
    A = LBT._add_root(1)
    B = LBT._add_left(A, 2)
    E = LBT._add_right(A, 5)
    C = LBT._add_left(B, 3)
    D = LBT._add_right(B, 4)
    F = LBT._add_left(E, 6)

    """1. Preorder Traversal Algorithm (Applicable for all trees).
    This algorithm should be placed in Tree ADT.
    """

    def subtree_preorder_print(p):
        print(p.element())
        for c in LBT.children(p): # the children method in BT ADT, lists left child first
            subtree_preorder_print(c)
    print('preorder traversal print')
    subtree_preorder_print(A)

    # Find out why one extra for loop is required for yield 
    # as compared to print statement in essentially same recursive functions 
    # defined below.

    # generator
    def _subtree_preorder_yield(p):
        yield p
        for c in LBT.children(p):
            for other in _subtree_preorder_yield(c):
                yield other
    print('preorder traversal by generator')
    for i in _subtree_preorder_yield(A):
        print(i.element())

    # the above yield statement can also be written as below
    def _subtree_preorder_yield1(p):
        yield p
        for c in LBT.children(p):
            yield from _subtree_preorder_yield1(c)
    
    """2. Postorder Traversal Algorithm (applicable for all trees).
    This algorithm should be placed in Tree ADT.
    """
    # similar to preorder, except root is traversed last.
    
    def _subtree_postorder(p):
        for c in LBT.children(p):
            for other in LBT._subtree_postorder(c):
                yield other
        yield p
    print('postorder traversal by generator')
    for i in _subtree_postorder(A):
        print(i.element())
    
    """3. Breadth-First Traversal Algorithm (applicable for all trees).
    This algorithm should be placed in Tree ADT.
    """
    # it doesn't use recursion, it uses queue.
    # def breadthfirst(self):
    #     if not self.is_empty():
    #         fringe = LinkedQueue()  # we need to import it from ch7 notes
    #         fringe.enqueue(self.root())
    #         while not fringe.is_empty():
    #             p = fringe.dequeue()
    #             yield p
    #             for c in self.children(p):
    #                 fringe.enqueue(C)

    """4. Inorder Traversal Algorithm (applicable only to Binary Trees as it uses
    notion of left child and right child of a node).
    This algorithm should be placed in BinaryTree ADT.
    """
    # generator
    def _subtree_inorder(p):
        if LBT.left(p) is not None:
            for other in LBT._subtree_inorder(LBT.left(p)):
                yield other
        yield p
        if LBT.right(p) is not None:
            for other in LBT._subtree_inorder(LBT.right(p)):
                yield other
    
    # simple printing
    def _subtree_inorder_print(p):
        if LBT.left(p) is not None:
            _subtree_inorder_print(LBT.left(p))
        print(p.element())
        if LBT.right(p) is not None:
            _subtree_inorder_print(LBT.right(p))
    print('inorder traversal of binary tree')
    _subtree_inorder_print(A)

#----------------------------------------------------------

if __name__ == '__main__':
# different ways to print the elements of trees.

    LBT = LinkedBinaryTree()
    A = LBT._add_root(1)
    B = LBT._add_left(A, 2)
    E = LBT._add_right(A, 5)
    C = LBT._add_left(B, 3)
    D = LBT._add_right(B, 4)
    F = LBT._add_left(E, 6)
    G = LBT._add_right(E, 7)

    def preorder_indent(T, p, d=0):
        """Print preorder representation of subtree of T rooted at p at depth d."""
        print(2*d*' ' + str(p.element()))
        for c in T.children(p):
            preorder_indent(T, c, d+1)

    preorder_indent(LBT, LBT.root())

    def preorder_label(T, p, d, path):
        """Print labeled representation of subtree of T rooted at p at depth d."""
        label = ".".join(str(j+1) for j in path)
        print(2*d*" " + label, p.element())
        path.append(0)
        for c in T.children(p):
            preorder_label(T, c, d+1, path)
            path[-1] += 1
        path.pop()

    preorder_label(LBT, LBT.root(), 0, [])

    def parenthesize(T, p):
        """Print parenthesized representation of subtree of T rooted at p."""
        print(p.element(), end='')
        if not T.is_leaf(p):
            first_time = True
            for c in T.children(p):
                sep = ' (' if first_time else ', '
                print(sep, end = '')
                first_time = False
                parenthesize(T, c)
            print(')', end='')

    parenthesize(LBT, LBT.root())

    #----------------------------------------------------

