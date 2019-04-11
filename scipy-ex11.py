import numpy as np
from scipy import linalg

A = np.array([[1,4,6],[2,5,4],[7,3,5]])

print("Matriz A")
print(A)

print("Determinando auto-valores e auto-vetores")

lambdas, v = linalg.eig(A)

l1,l2,l3 = lambdas

print("\n")
print("Auto-valores")

for i in range(len(lambdas)):
	print(i+1," ",lambdas[i])

print("\n")	
print("Auto-vetores")	

v[:, 0]

for i in range(len(lambdas)):
	print(i+1," ",v[:,i])
	
