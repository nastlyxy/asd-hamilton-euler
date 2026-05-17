import copy

def find_eulerian_cycle(graph):
    
    for vertex, neighbors in graph.adj_list.items():
        if len(neighbors) % 2 != 0:
            return None  
    adj_list_copy = copy.deepcopy(graph.adj_list)

    start_vertex = 0
    for v in range(graph.num_vertices):
        if len(adj_list_copy[v]) > 0:
            start_vertex = v
            break

    if not adj_list_copy[start_vertex]:
        return []
    
    stack = [start_vertex]
    cycle = []

    while stack:
        current_vertex = stack[-1]

        if adj_list_copy[current_vertex]:
            next_vertex = adj_list_copy[current_vertex].pop()
            adj_list_copy[next_vertex].remove(current_vertex)
            stack.append(next_vertex)
        else:
            cycle.append(stack.pop())

    return cycle[::-1]