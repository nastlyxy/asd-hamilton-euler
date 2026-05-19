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
            # Interaktywne pobieranie danych od użytkownika
            nodes_str = input("nodes> ")
            nodes = int(nodes_str)
            
            sat_str = input("saturation> ")
            saturation = int(sat_str)
            
            if not (0 <= saturation <= 80):
                # Ograniczamy do 80%, ponieważ przy >85% losowe szukanie wolnych trójkątów
                # zaczyna drastycznie zwalniać, a dla >100% powoduje nieskończoną pętlę.
                # Wymagane w zadaniu to 30% i 70%.
                raise ValueError("Nasycenie musi być w przedziale od 0 do 80%")

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

            print("\nGenerowanie pliku TikZ dla LaTeXa...")
            
            # Jedna funkcja pakuje wszystkie wyniki do jednego pliku
            export_all_to_tikz(graph, "wykresy_grafow.tex", hamilton_cycle=hamilton_path, euler_cycle=euler_path)
                
            print("Zapisano! Skopiuj zawartość pliku 'wykresy_grafow.tex' do Overleafa.")
            
        except ValueError as e:
            print(f"Błąd wartości: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nPrzerwano działanie programu przez użytkownika.")
            sys.exit(0)
            
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

            print("\nGenerowanie pliku TikZ dla LaTeXa...")
            
            # Jedna funkcja pakuje wszystkie wyniki do jednego pliku
            export_all_to_tikz(graph, "wykresy_grafow.tex", hamilton_cycle=hamilton_path, euler_cycle=euler_path)
                
            print("Zapisano! Skopiuj zawartość pliku 'wykresy_grafow.tex' do Overleafa.")
            
        except ValueError as e:
            print(f"Błąd wartości: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nPrzerwano działanie programu przez użytkownika.")
            sys.exit(0)
            
    else:
        print("Nieznany argument. Użyj flagi --hamilton lub --non-hamilton")

if __name__ == "__main__":
    main()