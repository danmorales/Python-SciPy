from scipy import integrate
import numpy as np

def f1(x,y):
	z = x*(y**2)
	return z

integral1 = integrate.nquad(f1, [[0,1], [0,1]])

print("Integral1 (numérica) ",integral1[0])
print("Integral1 (analítica) ",1.0/6.0)

print("\n")

def bounds_y(x):
	 return [0, (1-x*x)**0.5]
	 
def bounds_x():
	return [0, 1.0]

integral2 = integrate.nquad(f1, [bounds_y, bounds_x])

print("Integral2 (numérica) ",integral2[0])
print("Integral2 (analítica) ",1.0/15.0)