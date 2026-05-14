import sys
from generator import generate_full_hamiltonian, generate_non_hamiltonian

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
            
        except ValueError as e:
            print(f"Błąd wartości: {e}")
            
    else:
        print("Nieznany argument. Użyj flagi --hamilton lub --non-hamilton")

if __name__ == "__main__":
    main()