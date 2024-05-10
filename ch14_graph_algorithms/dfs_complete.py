# an extension of DFS algorithm
from adjacency_map import Graph
from dfs_recursive import DFS

def DFS_complete(g):
    """Perform DFS for entire graph and return forest as a dictionary.
    
    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are the roots of a DFS tree are mapped to None.)
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None    # u will be the root of a tree
            DFS(g, u, forest)
    return forest
