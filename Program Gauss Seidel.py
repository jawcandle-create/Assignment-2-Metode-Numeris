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
# METODE GAUSS-SEIDEL
# ==========================================

print("==========================================")
print("       METODE GAUSS-SEIDEL")
print("==========================================")

print("\nIterasi       T1           T2           T3          Error")

for iteration in range(1, max_iterations + 1):

    # Simpan nilai lama untuk menghitung error
    x_old = x.copy()

    # T1 menggunakan nilai T2 lama
    x[0] = (737.5 + 20*x_old[1]) / 41

    # T2 langsung menggunakan T1 terbaru
    x[1] = (37.5 + 20*x[0] + 20*x_old[2]) / 41

    # T3 langsung menggunakan T2 terbaru
    x[2] = (717.5 + 20*x[1]) / 41

    # Menghitung error
    error = np.max(np.abs(x - x_old))

    print(f"{iteration:5d}   "
          f"{x[0]:10.6f} "
          f"{x[1]:10.6f} "
          f"{x[2]:10.6f} "
          f"{error:.6e}")

    # Cek konvergensi
    if error < tolerance:
        break

# ==========================================
# HASIL AKHIR
# ==========================================

print("\n==========================================")
print("HASIL AKHIR GAUSS-SEIDEL")
print("==========================================")

print(f"T1 = {x[0]:.8f} °C")
print(f"T2 = {x[1]:.8f} °C")
print(f"T3 = {x[2]:.8f} °C")
print(f"Jumlah iterasi = {iteration}")
print(f"Error akhir = {error:.6e}")