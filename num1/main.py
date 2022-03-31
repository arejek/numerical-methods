import numpy as np
import math

A1 = np.array([[2.40827208, -0.36066254, 0.80575445, 0.46309511, 1.20708553],
               [-0.36066254, 1.14839502, 0.02576113, 0.02672584, -1.03949556],
               [0.80575445, 0.02576113, 2.45964907, 0.13824088, 0.0472749],
               [0.46309511, 0.02672584, 0.13824088, 2.05614464, -0.9434493],
               [1.20708553, -1.03949556, 0.0472749, -0.9434493, 1.92753926]])

A2 = np.array([[2.61370745, -0.6334453, 0.76061329, 0.24938964, 0.82783473],
               [-0.6334453, 1.51060349, 0.08570081, 0.31048984, -0.53591589],
               [0.76061329, 0.08570081, 2.46956812, 0.18519926, 0.13060923],
               [0.24938964, 0.31048984, 0.18519926, 2.27845311, -0.54893124],
               [0.82783473, -0.53591589, 0.13060923, -0.54893124, 2.6276678]])

b = np.transpose(np.array([[5.40780228, 3.67008677, 3.12306266, -1.11187948, 0.54437218]]))

bPrim = b + np.transpose(np.array([[0.00001, 0, 0, 0, 0]]))

ADiff = np.subtract(A1, A2)
print("Roznice we wspolczynnkiach macierzy A1 i A2:")
print(ADiff)

y1 = np.linalg.solve(A1, b)
y1Prim = np.linalg.solve(A1, bPrim)
y2 = np.linalg.solve(A2, b)
y2Prim = np.linalg.solve(A2, bPrim)

print("y1 i y1Prim:")
print(y1)
print(y1Prim)
print("y2 i y2Prim:")
print(y2)
print(y2Prim)

y1Diff = y1 - y1Prim
y2Diff = y2 - y2Prim

s1 = 0
for x in y1Diff:
    s1 = s1 + x ** 2
delta1 = math.sqrt(s1)

s2 = 0
for x in y2Diff:
    s2 = s2 + x ** 2
delta2 = math.sqrt(s2)

print("delta1: ", end=" ")
print(delta1)
print("delta2: ", end=" ")
print(delta2)
