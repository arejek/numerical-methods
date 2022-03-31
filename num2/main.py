import numpy as np
from scipy.sparse import diags

# diagonale macierzy A
Aii = 1.2
Aiadd1_i = 0.2
Ai_iadd1 = [0.1/(x+1) for x in range(100)]
Ai_iadd2 = [0.4/((n+1)**2) for n in range(100)]

# znany wektor w rownaniu do obliczenia
x = [m+1 for m in range(100)]

# inicjalizacja poczatkow poszczegolnych pasm
Uii = [Aii]
Ui_iadd1 = [Ai_iadd1[0]]
Ui_iadd2 = [Ai_iadd2[0]]
Liadd1_i = [Aiadd1_i/Uii[0]]

# utworzenie poszczegolnych pasm
for i in range(99):
    Uii.append(Aii - (Liadd1_i[i] * Ui_iadd1[i]))
    Liadd1_i.append(Aiadd1_i / Uii[i + 1])
    Ui_iadd2.append(Ai_iadd2[i + 1])
    Ui_iadd1.append(Ai_iadd1[i + 1] - Liadd1_i[i] * Ui_iadd2[i])

# na tym etapie mamy obliczony rozklad L U,

# licze wyznacznik macierzy A
# korzystajac z detA = detL * detU = 1 * detU = detU
detA = 1
for el in Uii:
    detA = detA * el

# licze rozwiazanie rownania Lb = x
b = list()
b.append(x[0])  # na samej gorze L jest 1
for i in range(99):
    b.append(x[i+1] - Liadd1_i[i] * b[i])

# licze rozwiazanie rownania Ub = y
yT = [x for x in range(100)]
yT[99] = (b[99]/Uii[99])
for i in reversed(range(99)):
    if i == 98:
        yT[i] = (b[i] - yT[i+1] * Ui_iadd1[i]) / Uii[i]
    else:
        yT[i] = (b[i]-yT[i+1]*Ui_iadd1[i]-yT[i+2]*Ui_iadd2[i])/Uii[i]

y = np.transpose(np.array([yT]))

# -------------------------------------------------------------------------------
# sprawdzenie przy uzyciu numpy i scipy
diagonals = [[1.2 for x in range(100)], [0.2 for x in range(99)],
             [0.1/(x+1) for x in range(99)], [0.4/(n+1)**2 for n in range(98)]]
A_for_check = diags(diagonals, [0, -1, 1, 2]).toarray()
x_for_check = np.transpose(np.array([[x+1 for x in range(100)]]))
y_for_check = np.linalg.solve(A_for_check, x_for_check)
detA_for_check = np.linalg.det(A_for_check)
# -------------------------------------------------------------------------------

diff = np.subtract(y_for_check, y)

print("Moje rozwiazanie zadanego rownania:")
print(y)
print("Rozwiazanie NumPy:")
print(y_for_check)
print("Roznica w wektorach poszczegolnych rozwiazan:")
print(diff)
print("Wspolczynnik wyliczony przez moj program: ", end="")
print(detA)
print("Wspolczynnik wyliczony przez NumPy: ", end="")
print(detA_for_check)
print("Roznica wyniku: ", end="")
print(detA_for_check - detA)
