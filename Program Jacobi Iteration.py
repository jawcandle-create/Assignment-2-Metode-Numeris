import numpy as np

# ==========================================
# SISTEM PERSAMAAN
# ==========================================

A = np.array([
    [41, -20, 0],
    [-20, 41, -20],
    [0, -20, 41]
], dtype=float)

b = np.array([737.5, 37.5, 717.5], dtype=float)

# ==========================================
# PARAMETER ITERASI
# ==========================================

x = np.array([37.0, 37.0, 37.0])

tolerance = 1e-6
max_iterations = 100

# ==========================================
# METODE JACOBI
# ==========================================

print("==========================================")
print("      METODE JACOBI ITERATION")
print("==========================================")

print("\nIterasi       T1           T2           T3          Error")

for iteration in range(1, max_iterations + 1):

    # Menggunakan nilai iterasi sebelumnya
    x_new = np.zeros(3)

    x_new[0] = (737.5 + 20*x[1]) / 41

    x_new[1] = (37.5 + 20*x[0] + 20*x[2]) / 41

    x_new[2] = (717.5 + 20*x[1]) / 41

    # Menghitung error
    error = np.max(np.abs(x_new - x))

    print(f"{iteration:5d}   "
          f"{x_new[0]:10.6f} "
          f"{x_new[1]:10.6f} "
          f"{x_new[2]:10.6f} "
          f"{error:.6e}")

    # Update nilai
    x = x_new.copy()

    # Cek konvergensi
    if error < tolerance:
        break

# ==========================================
# HASIL AKHIR
# ==========================================

print("\n==========================================")
print("HASIL AKHIR JACOBI")
print("==========================================")

print(f"T1 = {x[0]:.8f} °C")
print(f"T2 = {x[1]:.8f} °C")
print(f"T3 = {x[2]:.8f} °C")
print(f"Jumlah iterasi = {iteration}")
print(f"Error akhir = {error:.6e}")