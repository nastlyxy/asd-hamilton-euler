import random
from graph import Graph

def generate_hamiltonian_cycle(n):
    graph = Graph(n)
    vertices = list(range(n))
    random.shuffle(vertices)
    
    for i in range(n):
        u = vertices[i]
        v = vertices[(i + 1) % n]
        graph.add_edge(u, v)
        
    return graph

def get_max_edges(n):
    return n * (n - 1) // 2

def saturate_graph(graph, target_saturation):
    n = graph.num_vertices
    max_edges = get_max_edges(n)
    target_edges = int(max_edges * target_saturation)
    
    current_edges = n 
    
    while current_edges < target_edges:
        v1, v2, v3 = random.sample(range(n), 3)

        if (v2 not in graph.adj_list[v1] and 
            v3 not in graph.adj_list[v2] and 
            v1 not in graph.adj_list[v3]):
            
            graph.add_edge(v1, v2)
            graph.add_edge(v2, v3)
            graph.add_edge(v3, v1)

            current_edges += 3

def generate_full_hamiltonian(n, saturation_percent):
    if n <= 10:
        raise ValueError("Ilość wierzchołków musi być większa niż 10")
        
    graph = generate_hamiltonian_cycle(n)
    saturate_graph(graph, saturation_percent / 100.0)
    return graph

def generate_non_hamiltonian(n):
    graph = generate_full_hamiltonian(n - 1, 50) 
    
    final_graph = Graph(n)
    final_graph.adj_list.update(graph.adj_list)
    final_graph.adj_list[n - 1] = set()
    
    return final_graph