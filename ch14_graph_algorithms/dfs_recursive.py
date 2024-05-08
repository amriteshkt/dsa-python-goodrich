from adjacency_map import Graph

# discovered = {u: None}  # u should be trivially discovered
def DFS(g, u, discovered):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be 'discovered' prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in g.incident_edges(u):   # for every outgoing edge from u
        v = e.opposite(u)
        if v not in discovered:     # v is an unvisited vertex
            discovered[v] = e       # e is the tree edge that discovered v
            DFS(g, v, discovered)   # recursively explore from v

# for better understanding modify above algorithm to store just elements
def DFS_print_elements(g, u, discovered):
    """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the DFS. (u should be 'discovered' prior to the call.)
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in g.incident_edges(u):   # for every outgoing edge from u
        v = e.opposite(u)
        if v.element() not in discovered:     # v is an unvisited vertex
            discovered[v.element()] = e.element()       # e is the tree edge that discovered v
            DFS_print_elements(g, v, discovered)   # recursively explore from v

if __name__ == '__main__':
    # creating graph as in Fig 14.9 page no. 641 
    graph = Graph()
    v_a = graph.insert_vertex('A')
    v_b = graph.insert_vertex('B')
    v_c = graph.insert_vertex('C')
    v_d = graph.insert_vertex('D')
    v_e = graph.insert_vertex('E')
    v_f = graph.insert_vertex('F')
    v_g = graph.insert_vertex('G')
    v_h = graph.insert_vertex('H')
    v_i = graph.insert_vertex('I')
    v_j = graph.insert_vertex('J')
    v_k = graph.insert_vertex('K')
    v_l = graph.insert_vertex('L')
    v_m = graph.insert_vertex('M')
    v_n = graph.insert_vertex('N')
    v_o = graph.insert_vertex('O')
    v_p = graph.insert_vertex('P')

    graph.insert_edge(v_a, v_b, 'a_to_b')
    graph.insert_edge(v_a, v_f, 'a_to_f')
    graph.insert_edge(v_a, v_e, 'a_to_e')
    graph.insert_edge(v_b, v_c, 'b_to_c')
    graph.insert_edge(v_b, v_f, 'b_to_f')
    graph.insert_edge(v_c, v_d, 'c_to_d')
    graph.insert_edge(v_c, v_g, 'c_to_g')
    graph.insert_edge(v_d, v_h, 'd_to_h')
    graph.insert_edge(v_d, v_g, 'd_to_g')
    graph.insert_edge(v_e, v_f, 'e_to_f')
    graph.insert_edge(v_e, v_i, 'e_to_i')
    graph.insert_edge(v_f, v_i, 'f_to_i')
    graph.insert_edge(v_g, v_j, 'g_to_j')
    graph.insert_edge(v_g, v_k, 'g_to_k')
    graph.insert_edge(v_g, v_l, 'g_to_l')
    graph.insert_edge(v_h, v_l, 'h_to_l')
    graph.insert_edge(v_i, v_m, 'i_to_m')
    graph.insert_edge(v_i, v_n, 'i_to_n')
    graph.insert_edge(v_k, v_n, 'k_to_n')
    graph.insert_edge(v_k, v_o, 'k_to_o')
    graph.insert_edge(v_l, v_p, 'l_to_p')
    graph.insert_edge(v_m, v_n, 'm_to_n')

    # we must first create a dictionary containing starting vertex
    discovered = {v_a.element(): None}
    DFS_print_elements(graph, v_a, discovered)
    print(discovered)

    # print degree of vertex F, result should be 4
    print(graph.degree(v_f))

    # print incident edges of vertex F
    for edge in graph.incident_edges(v_f):
        print(edge.element())
