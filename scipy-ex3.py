from scipy.integrate import quad
import numpy as np

def f1(x):
	y = 1.0/(1.0+x*x)
	return y
	

def int_f1(x):
	return quad(f1, 0, np.inf)[0]

def f2(x):
	y = np.exp(-1.0*x)
	return y
	
def int_f2(x):
	return quad(f2, 0, np.inf)[0]

	
integral1 = int_f1(0)

print("Integral 1 (numérica) = ",integral1)
print("Integral 1 (analítica) = ",np.pi/2.0)

print("\n")

integral2 = int_f2(0)

print("Integral 2 (numérica) = ",integral2)
print("Integral 2 (analítica) = ",1.0)

