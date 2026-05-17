import sys
from generator import generate_full_hamiltonian, generate_non_hamiltonian
from algorithms.hamilton import find_hamilton_cycle
from algorithms.euler import find_eulerian_cycle
from export import export_all_to_tikz

def main():
    """
    Główna funkcja programu obsługująca interfejs wiersza poleceń.
    """
    if len(sys.argv) < 2:
        print("Użycie: python3 main.py --hamilton LUB python main.py --non-hamilton")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "--hamilton":
        try:
            # pobieranie danych od użytkownika
            nodes_str = input("nodes> ")
            nodes = int(nodes_str)
            sat_str = input("saturation> ")
            saturation = int(sat_str)
            
            # Generowanie i wypisywanie grafu
            graph = generate_full_hamiltonian(nodes, saturation)
            print("\nWygenerowany graf Hamiltona:")
            graph.print_graph()
            
            # Szukanie i wypisywanie cyklu Hamiltona oraz Eulera dla grafu hamiltonowskiego
            print("\nSzukanie cyklu Hamiltona...")
            hamilton_path = find_hamilton_cycle(graph)
            if hamilton_path:
                print("Cykl Hamiltona:", " -> ".join(str(v + 1) for v in hamilton_path))
            else:
                print("Cykl Hamiltona: Nie znaleziono")

            print("\nSzukanie cyklu Eulera...")
            euler_path = find_eulerian_cycle(graph)
            if euler_path:
                print("Cykl Eulera:", " -> ".join(str(v + 1) for v in euler_path))
            else:
                print("Cykl Eulera: Nie znaleziono")

            # === KOD EKSPORTU ===
            print("\nGenerowanie pliku TikZ dla LaTeXa...")
            
            # Jedna funkcja pakuje wszystkie wyniki do jednego pliku!
            export_all_to_tikz(graph, "wykresy_grafow.tex", hamilton_cycle=hamilton_path, euler_cycle=euler_path)
                
            print("Zapisano! Skopiuj zawartość pliku 'wykresy_grafow.tex' do Overleafa.")
            # =========================

        except ValueError as e:
            print(f"Błąd wartości: {e}")
            
    elif mode == "--non-hamilton":
        try:
            nodes_str = input("nodes> ")
            nodes = int(nodes_str)
            
            # Generowanie i wypisywanie grafu nie-hamiltonowskiego
            graph = generate_non_hamiltonian(nodes)
            print("\nWygenerowany graf nie-hamiltonowski:")
            graph.print_graph()

            # Szukanie i wypisywanie cyklu Hamiltona oraz Eulera dla grafu nie-hamiltonowskiego
            print("\nSzukanie cyklu Hamiltona...")
            hamilton_path = find_hamilton_cycle(graph)
            if hamilton_path:
                print("Cykl Hamiltona:", " -> ".join(str(v + 1) for v in hamilton_path))
            else:
                print("Cykl Hamiltona: Nie znaleziono")

            print("\nSzukanie cyklu Eulera...")
            euler_path = find_eulerian_cycle(graph)
            if euler_path:
                print("Cykl Eulera:", " -> ".join(str(v + 1) for v in euler_path))
            else:
                print("Cykl Eulera: Nie znaleziono")

            # === NOWY KOD EKSPORTU ===
            print("\nGenerowanie pliku TikZ dla LaTeXa...")
            
            # Jedna funkcja pakuje wszystkie wyniki do jednego pliku!
            export_all_to_tikz(graph, "wykresy_grafow.tex", hamilton_cycle=hamilton_path, euler_cycle=euler_path)
                
            print("Zapisano! Skopiuj zawartość pliku 'wykresy_grafow.tex' do Overleafa.")
            # =========================
            
        except ValueError as e:
            print(f"Błąd wartości: {e}")
            
    else:
        print("Nieznany argument. Użyj flagi --hamilton lub --non-hamilton")

if __name__ == "__main__":
    main()