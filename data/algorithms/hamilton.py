def find_hamilton_cycle(graph):
    """
    Funkcja sprawdzająca, czy dany graf zawiera cykl Hamiltona.
    Zwraca listę wierzchołków tworzących cykl lub None, jeśli taki nie istnieje.
    """
    num_vertices = graph.num_vertices
    path = [-1]*num_vertices  # -1 oznacza nieodwiedzony wierzchołek

    path[0] = 0  # Startujemy zawsze od wierzchołka 0, by unikać duplikatów cykli 

    def is_valid_vertex(v, pos):
        """Sprawdza, czy wierzchołek 'v' można legalnie dodać do ścieżki."""
        # 1. Czy istnieje krawędź z poprzednim wierzchołkiem w ścieżce?
        if v not in graph.adj_list[path[pos - 1]]:
            return False
       # 2. Czy wierzchołek nie był już wcześniej odwiedzony?
        if v in path:
            return False
        return True

    def backtrack(pos):
        # Baza rekurencji: wszystkie wierzchołki odwiedzone. Sprawdzamy zamknięcie cyklu.
        if pos == num_vertices:
            return path[0] in graph.adj_list[path[pos - 1]]

        for v in range(1, num_vertices):
            if is_valid_vertex(v, pos):
                path[pos] = v  # Zaznaczamy wybór
                if backtrack(pos + 1):  # Schodzimy poziom głębiej
                    return True
                path[pos] = -1  # Backtracking: ślepy zaułek, cofamy wybór   
        return False

    if backtrack(1):
        return path + [path[0]]  # Zwracamy cykl z zamknięciem na końcu
    return None