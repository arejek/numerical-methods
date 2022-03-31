import numpy as np
from scipy.sparse import diags

# -------------------------------------------------------------------------------
# moje wyliczenia
# -------------------------------------------------------------------------------
b = [5 for n in range(50)]
u = [1 for n in range(50)]
# diagonale macierzy APrim:
APrim_ii = 9
APrim_iadd1_i = 7

# --- --- ---
z = [0 for n in range(50)]  # inicjuje liste, zeby odwolywac sie do indeksow od [50]
# Uz=b backsubstitution
for i in reversed(range(50)):
    if i == 49:
        z[i] = b[49]/APrim_ii
    else:
        z[i] = (b[i] - APrim_iadd1_i*z[i+1])/APrim_ii

# --- --- ---
zPrim = [0 for n in range(50)]
# UzPrim=u backsubstitution
for i in reversed(range(50)):
    if i == 49:
        zPrim[i] = u[i]/APrim_ii
    else:
        zPrim[i] = (u[i] - APrim_iadd1_i*zPrim[i+1])/APrim_ii

# --- --- ---
# z obliczonymi wektorami z i zPrim przechodzimy do rownania wyliczajacego wlasciwe rozwiazanie:
# y = z - (zPrim(vTz))/1+vTzPrim
vTz = 0
for el in z:  # proste mnozenie 2 wektorow
    vTz = vTz + el
fraction_up = [0 for n in range(50)]  # fraction_up to (zPrim(vTz))
for i in range(50):
    fraction_up[i] = zPrim[i] * vTz
vTzPrim = 0
for el in zPrim:  # proste mnozenie 2 wektorow
    vTzPrim = vTzPrim + el
fraction_down = 1 + vTzPrim
for i in range(50):
    fraction_up[i] = fraction_up[i]/fraction_down
y = [0 for n in range(50)]
for i in range(50):
    y[i] = z[i] - fraction_up[i]


# -------------------------------------------------------------------------------
# sprawdzenie przy uzyciu numpy i scipy
# -------------------------------------------------------------------------------
b_for_check = np.transpose(np.array([[5 for n in range(50)]]))

# macierz rzadka z 9 i 7:
diagonals = [[9 for n in range(50)], [7 for n in range(50)]]
APrim_for_check = diags(diagonals, [0, 1]).toarray()
# chcemy otrzymac oryginalna macierz A z jedynkami i 10 i 8
# A = A' + uuT
u_for_check = np.transpose(np.array([[1 for n in range(50)]]))
uT_for_check = np.array([[1 for n in range(50)]])
A = np.dot(u_for_check, uT_for_check)  # mnozymy wektory w celu uzyskania mac wypelnionej jedynkami

A_for_check = APrim_for_check + A  # dodajemy macierze

y_for_check = np.linalg.solve(A_for_check, b_for_check)
# -------------------------------------------------------------------------------
print("==============================================")
print("--------------------NumPy---------------------")
print("Macierz A:")
print(A_for_check)
print("rozmiar A: ", end="")
print(A_for_check.shape)
print("Rozwiazanie rownania Ay=b:")
print(y_for_check)
print("==============================================")
# -------------------------------------------------------------------------------
print("Moje rozwiazanie:")
for n in y:
    print(n)

print("Roznica pomiedzy moim wektorem y a wektorem z NumPy:")

my_y_for_check = np.transpose(np.array([y]))
diff = np.subtract(y_for_check, my_y_for_check)
print(diff)
