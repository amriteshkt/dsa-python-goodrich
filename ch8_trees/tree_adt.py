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
