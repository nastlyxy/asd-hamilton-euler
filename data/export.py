import math

def export_to_tikz(graph, filename, cycle=None, cycle_color="blue"):
    """
    Eksportuje graf do pliku .tex zawierającego kod TikZ.
    Tworzy samodzielny plik (standalone), który można od razu skompilować w Overleaf.
    """
    n = graph.num_vertices
    # Dynamiczny promień okręgu – im więcej węzłów, tym większe koło, by uniknąć ścisku
    radius = max(3.0, n * 0.5)

    with open(filename, 'w', encoding='utf-8') as f:
        # Nagłówki wymagane przez LaTeX
        f.write("\\documentclass{standalone}\n")
        f.write("\\usepackage{tikz}\n")
        f.write("\\begin{document}\n")
        f.write(f"\\begin{{tikzpicture}}[node distance={radius}cm, main/.style = {{draw, circle, thick, minimum size=0.8cm, fill=white}}]\n\n")

        f.write("    % 1. Rozmieszczenie wierzchołków na planie okręgu\n")
        for i in range(n):
            angle = 360 / n * i
            # Etykieta wierzchołka to i+1, żeby liczyć od 1
            f.write(f"    \\node[main] ({i}) at ({angle}:{radius}) {{{i+1}}};\n")

        f.write("\n    % 2. Rysowanie wszystkich krawędzi (na jasnoszaro)\n")
        # Zbiór zapobiegający podwójnemu rysowaniu (w jedną i drugą stronę)
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

        f.write("\\end{tikzpicture}\n")
        f.write("\\end{document}\n")