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