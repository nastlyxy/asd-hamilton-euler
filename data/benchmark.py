import time
import csv
from generator import generate_full_hamiltonian, generate_non_hamiltonian
from algorithms.hamilton import find_hamilton_cycle
from algorithms.euler import find_eulerian_cycle

def run_benchmarks():
    """
    Automatyczny skrypt do przeprowadzania pomiarów czasu (benchmarking).
    Zapisuje wyniki do pliku CSV zgodnie z wymaganiami zadania 4.
    """
    with open('benchmark_results.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Mode', 'N', 'Saturation', 'Algorithm', 'Time'])

        # --- Grafy hamiltonowskie (30% i 70%) ---
        hamiltonian_sizes =[12, 14, 16, 18, 20, 22, 24, 26, 28]
        saturations = [30, 70]

        print("Uruchamianie testów dla grafów hamiltonowskich...")
        for sat in saturations:
            for n in hamiltonian_sizes:
                graph = generate_full_hamiltonian(n, sat)
                
                # Pomiar czasu dla algorytmu Eulera
                start = time.perf_counter()
                find_eulerian_cycle(graph)
                t_euler = time.perf_counter() - start
                writer.writerow(['Hamiltonian', n, sat, 'Euler', t_euler])

                # Pomiar czasu dla algorytmu Hamiltona
                start = time.perf_counter()
                find_hamilton_cycle(graph)
                t_hamilton = time.perf_counter() - start
                writer.writerow(['Hamiltonian', n, sat, 'Hamilton', t_hamilton])
                
                print(f"Graf hamiltonowski N={n}, Nasycenie={sat}% -> Zakończono")

        # --- Grafy nie-hamiltonowskie (50%) ---
        non_hamiltonian_sizes = [12, 13, 14, 15, 16, 17]
        
        print("\nUruchamianie testów dla grafów nie-hamiltonowskich (Złożoność wykładnicza)...")
        for n in non_hamiltonian_sizes:
            graph = generate_non_hamiltonian(n)
            
            start = time.perf_counter()
            find_hamilton_cycle(graph)
            t_hamilton = time.perf_counter() - start
            writer.writerow(['Non-Hamiltonian', n, 50, 'Hamilton', t_hamilton])
            
            print(f"Graf nie-hamiltonowski N={n} -> Czas: {t_hamilton:.4f} s")
            
            # Zabezpieczenie przed zbyt długim oczekiwaniem (NP-zupełność)
            if t_hamilton > 180:
                print("Przerwano dalsze testy: osiągnięto limit czasu dla problemu NP-zupełnego.")
                break

    print("\nWszystkie pomiary zostały pomyślnie zapisane w pliku 'benchmark_results.csv'!")

if __name__ == "__main__":
    run_benchmarks()