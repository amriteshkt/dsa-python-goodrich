from linked_binary_tree import LinkedBinaryTree

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