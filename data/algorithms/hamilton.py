def find_hamilton_cycle(graph):
    """
    Funkcja sprawdzająca, czy dany graf zawiera cykl Hamiltona.
    Zwraca listę wierzchołków tworzących cykl lub None, jeśli taki nie istnieje.
    """
    num_vertices = graph.num_vertices
    path = [-1]*num_vertices

    path[0] = 0  

    def is_valid_vertex(v, pos):
        
        if v not in graph.adj_list[path[pos - 1]]:
            return False
        if v in path:
            return False
        return True

    def backtrack(pos):

        if pos == num_vertices:
            return path[0] in graph.adj_list[path[pos - 1]]

        for v in range(1, num_vertices):
            if is_valid_vertex(v, pos):
                path[pos] = v
                if backtrack(pos + 1):
                    return True
                path[pos] = -1
        return False

    if backtrack(1):
        return path + [path[0]]
    return None