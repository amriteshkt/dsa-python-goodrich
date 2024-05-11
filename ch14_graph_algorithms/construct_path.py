# extension of DFS algorithm
from adjacency_map import Graph
from dfs_recursive import DFS

def construct_path(u, v, discovered):
    """Returns an ordered list of vertices on the path."""
    path = []           # empty path by default
    if v in discovered:
        # we build list from v to u and then reverse it at the end
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]  # find edge leading to walk
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()            # reorient path from u to v
    return path
