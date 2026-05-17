import math

def export_all_to_tikz(graph, filename, hamilton_cycle=None, euler_cycle=None):
    """
    Eksportuje 3 wersje grafu (podstawowy, Hamilton, Euler) do JEDNEGO pliku .tex.
    Wyróżnia wierzchołek startowy dla każdego cyklu jasnym, zielonym kolorem.
    """
    n = graph.num_vertices
    radius = max(3.0, n * 0.5)

    with open(filename, 'w', encoding='utf-8') as f:
        # Używamy klasy article, aby grafy wyświetlały się ładnie jeden pod drugim z tytułami
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage{tikz}\n")
        f.write("\\usepackage[margin=1in]{geometry}\n")
        f.write("\\begin{document}\n")
        f.write("\\begin{center}\n")

        # Funkcja wewnętrzna rysująca pojedynczy graf (żeby nie powtarzać kodu 3 razy)
        def draw_single_graph(title, cycle, cycle_color):
            f.write(f"\\section*{{{title}}}\n")
            # Definiujemy style: 'main' dla zwykłych wierzchołków, 'startnode' dla początkowego
            f.write(f"\\begin{{tikzpicture}}[node distance={radius}cm, "
                    f"main/.style = {{draw, circle, thick, minimum size=0.8cm, fill=white}}, "
                    f"startnode/.style = {{draw, circle, ultra thick, minimum size=0.8cm, fill=green!20}}]\n\n")

            # Ustalanie wierzchołka startowego
            start_vertex = cycle[0] if cycle else None

            f.write("    % 1. Rozmieszczenie wierzchołków na planie okręgu\n")
            for i in range(n):
                angle = 360 / n * i
                # Etykieta wierzchołka to i+1. Zaznaczamy na zielono wierzchołek startowy.
                if i == start_vertex:
                    f.write(f"    \\node[startnode] ({i}) at ({angle}:{radius}) {{{i+1}}};\n")
                else:
                    f.write(f"    \\node[main] ({i}) at ({angle}:{radius}) {{{i+1}}};\n")

            f.write("\n    % 2. Rysowanie wszystkich krawędzi (na jasnoszaro)\n")
            seen_edges = set()
            for u in range(n):
                for v in graph.adj_list[u]:
                    edge = tuple(sorted((u, v)))
                    if edge not in seen_edges:
                        f.write(f"    \\draw[gray!40, thin] ({u}) -- ({v});\n")
                        seen_edges.add(edge)

            f.write("\n    % 3. Nakładanie cyklu (pogrubione, kolorowe strzałki)\n")
            if cycle:
                for i in range(len(cycle) - 1):
                    u = cycle[i]
                    v = cycle[i+1]
                    f.write(f"    \\draw[{cycle_color}, ultra thick, ->, >=stealth] ({u}) -- ({v});\n")

            f.write("\\end{tikzpicture}\n\\vspace{1.5cm}\n\n")

        # Generowanie kolejnych grafów do pliku
        draw_single_graph("Graf Podstawowy", None, "black")
        
        if hamilton_cycle:
            draw_single_graph("Cykl Hamiltona (niebieski)", hamilton_cycle, "blue")
            
        if euler_cycle:
            draw_single_graph("Cykl Eulera (czerwony)", euler_cycle, "red")

        f.write("\\end{center}\n")
        f.write("\\end{document}\n")