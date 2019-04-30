import numpy as np
from scipy import linalg

A = np.mat('[[1 3; 2 5]]')
print("Matriz A")
print(A)

print("\n")

invA = A.I 
print("Matriz inversa de A")
print(invA)

print("\n")

transpA = A.T
print("Matriz transposta de A")
print(transpA)

print("\n")

identidade = A * invA
print("Multiplicando matriz A com a sua inversa")
print(identidade)

print("\n")

print("Utilizando a biblioteca linalg")

B = np.array([[2,5],[3,8]])

print("Matriz B")
print(B)

print("\n")

linvB = linalg.inv(B)
print("Matriz inversa de B")
print(linvB)

print("\n")

mulAB = A.dot(B.T)

print("Multiplicando matriz A com a matriz B")
print(mulAB)

print("\n")

detA = linalg.det(A)
detB = linalg.det(B)

print("Determinante A= ",detA)
print("Determinante B= ",detB)

