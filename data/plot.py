import csv
import matplotlib.pyplot as plt

def generate_plots():
    """
    Wczytuje dane z pliku CSV i generuje wykresy t=f(n) wymagane do sprawozdania.
    """
    data = []
    with open('benchmark_results.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['N'] = int(row['N'])
            row['Saturation'] = int(row['Saturation'])
            row['Time'] = float(row['Time'])
            data.append(row)

    # Podział danych na poszczególne wykresy
    n_h30_euler, t_h30_euler = [], []
    n_h30_ham, t_h30_ham = [], []
    
    n_h70_euler, t_h70_euler = [], []
    n_h70_ham, t_h70_ham = [], []
    
    n_nh50, t_nh50 = [], []

    for r in data:
        if r['Mode'] == 'Hamiltonian' and r['Saturation'] == 30:
            if r['Algorithm'] == 'Euler':
                n_h30_euler.append(r['N'])
                t_h30_euler.append(r['Time'])
            else:
                n_h30_ham.append(r['N'])
                t_h30_ham.append(r['Time'])
        elif r['Mode'] == 'Hamiltonian' and r['Saturation'] == 70:
            if r['Algorithm'] == 'Euler':
                n_h70_euler.append(r['N'])
                t_h70_euler.append(r['Time'])
            else:
                n_h70_ham.append(r['N'])
                t_h70_ham.append(r['Time'])
        elif r['Mode'] == 'Non-Hamiltonian':
            n_nh50.append(r['N'])
            t_nh50.append(r['Time'])

    # --- WYKRES Nasycenie 30% ---
    plt.figure(figsize=(8, 5))
    plt.plot(n_h30_euler, t_h30_euler, label='Euler (Hierholzer)', marker='o', color='red')
    plt.plot(n_h30_ham, t_h30_ham, label='Hamilton (Backtracking)', marker='s', color='blue')
    plt.title('Wykres t=f(n) dla nasycenia 30% (Grafy Hamiltonowskie)')
    plt.xlabel('Liczba wierzchołków (n)')
    plt.ylabel('Czas wykonania (s)')
    plt.grid(True)
    plt.legend()
    plt.savefig('wykres_30.png')
    plt.close()

    # --- WYKRES Nasycenie 70% ---
    plt.figure(figsize=(8, 5))
    plt.plot(n_h70_euler, t_h70_euler, label='Euler (Hierholzer)', marker='o', color='red')
    plt.plot(n_h70_ham, t_h70_ham, label='Hamilton (Backtracking)', marker='s', color='blue')
    plt.title('Wykres t=f(n) dla nasycenia 70% (Grafy Hamiltonowskie)')
    plt.xlabel('Liczba wierzchołków (n)')
    plt.ylabel('Czas wykonania (s)')
    plt.grid(True)
    plt.legend()
    plt.savefig('wykres_70.png')
    plt.close()

    # --- WYKRES Grafy nie-hamiltonowskie 50% ---
    plt.figure(figsize=(8, 5))
    plt.plot(n_nh50, t_nh50, label='Hamilton (Backtracking) - Przypadek pesymistyczny', marker='^', color='darkblue', linestyle='--')
    plt.title('Wykres t=f(n) dla grafów nie-hamiltonowskich (Nasycenie 50%)')
    plt.xlabel('Liczba wierzchołków (n)')
    plt.ylabel('Czas wykonania (s)')
    plt.grid(True)
    plt.legend()
    plt.savefig('wykres_nie_hamilton.png')
    plt.close()

    print("Trzy wykresy zostały pomyślnie zapisane jako 'wykres_30.png', 'wykres_70.png' i 'wykres_nie_hamilton.png'!")

if __name__ == "__main__":
    generate_plots()