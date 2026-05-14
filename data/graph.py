class Graph:
    
    #Klasa reprezentująca graf nieskierowany.
    #Wykorzystano listę sąsiedztwa opartą na słowniku i zbiorach (hash sets).
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: set() for i in range(num_vertices)}

    def add_edge(self, u, v):
        #Dodaje nieskierowaną krawędź między u i v
        if u != v:
            self.adj_list[u].add(v)
            self.adj_list[v].add(u)

    def print_graph(self):
        for vertex, neighbors in self.adj_list.items():
            readable_neighbors = [n + 1 for n in neighbors]
            print(f"{vertex + 1}: {readable_neighbors}")