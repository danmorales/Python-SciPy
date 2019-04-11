import numpy as np
from scipy.integrate import simps

def f1n(x,a):
	return a*(x*x) + 2.0
	
def f1a(a,xmax,xmin):
	return (a/3.0)*(xmax**3.0 - xmin**3.0) +2.0*(xmax - xmin)
	
def f2n(x,a):
	return (a+2.0)*(x**3.0) + 2.0
	
def f2a(a,xmax,xmin):
	return ((a+2.0)/4.0)*(xmax**4.0 - xmin**4.0) + 2.0*(xmax - xmin)

a=2.0
size = 1000

xmax = 1.0
xmin = 0.0

x = np.linspace(xmin,xmax,size,endpoint=False)

y1 = f1n(x,a)

I1n = simps(y1, x)

I1a = f1a(a,xmax,xmin)

diff1 = I1a - I1n

print("Integral numérica ",I1n)
print("Integral analítica ",I1a)
print("Diferença ",diff1)

y2 = f2n(x,a)

I2n = simps(y2, x)

I2a = f2a(a,xmax,xmin)

diff2 = I2a - I2n

print("Integral numérica ",I2n)
print("Integral analítica ",I2a)
print("Diferença ",diff2)