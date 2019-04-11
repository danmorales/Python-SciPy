from scipy.integrate import quad

def funcao(x,a,b):
	f = a*(x**2) + b*x
	return f

def funcao2(xmax,xmin,a,b):
	f = ((a/3.0)*(xmax**3.0) + (b/2.0)*(xmax**2.0)) - ((a/3.0)*(xmin**3.0) + (b/2.0)*(xmin**2.0))
	return f
	
a = 2.0
b = 1.0

xmin = 0.0
xmax = 5.0

integral = quad(funcao,xmin,xmax,args=(a,b))[0]

print("Integral numérica")
print(integral)

print("\n")

integral2 = funcao2(xmax,xmin,a,b)

print("Integral da função")
print(integral2)

diff = integral2 - integral

print("\n")
print("Diferença= ",diff)


