from tree_adt import Tree

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