import copy

def find_eulerian_cycle(graph):
    """Znajduje cykl Eulera (przechodzi przez każdą krawędź dokładnie raz) algorytmem Hierholzera."""
    
    # Warunek konieczny: wszystkie wierzchołki muszą mieć parzysty stopień
    for vertex, neighbors in graph.adj_list.items():
        if len(neighbors) % 2 != 0:
            return None  
        
    # Tworzymy kopię, ponieważ algorytm dynamicznie usuwa odwiedzone krawędzie
    adj_list_copy = copy.deepcopy(graph.adj_list)

    # Szukamy pierwszego wierzchołka, który posiada jakiekolwiek krawędzie
    start_vertex = 0
    for v in range(graph.num_vertices):
        if len(adj_list_copy[v]) > 0:
            start_vertex = v
            break

    if not adj_list_copy[start_vertex]:
        return []
    
    stack = [start_vertex]
    cycle = []

    # Główna pętla algorytmu Hierholzera
    while stack:
        current_vertex = stack[-1]

        if adj_list_copy[current_vertex]:
            # Są jeszcze nieodwiedzone krawędzie: przechodzimy dalej i usuwamy krawędź (w obie strony)
            next_vertex = adj_list_copy[current_vertex].pop()
            adj_list_copy[next_vertex].remove(current_vertex)
            stack.append(next_vertex)
        else:
            # Brak krawędzi (ślepy zaułek): zdejmujemy wierzchołek ze stosu do ostatecznego cyklu
            cycle.append(stack.pop())
    # Stos buduje ścieżkę od końca, dlatego przed zwróceniem odwracamy wynik
    return cycle[::-1]