from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

def funcao(x):
	
	fx = np.sin(5.0*(x**3.0)) - np.cos((x**2)/2.0)
	return fx
	
xmin = 0.0
xmax = 6.0

size = (xmax - xmin) * 10
size2 = (xmax - xmin) * 50

x = np.linspace(xmin,xmax,size,endpoint=True)
y = np.zeros(len(x))

for i in range(len(x)):
	y[i] = funcao(x[i])
	
f1 = interp1d(x, y, kind='linear')
f2 = interp1d(x, y, kind='cubic')	

xnew = np.linspace(xmin, xmax, size2, endpoint=True)
y1new = f1(xnew)
y2new = f2(xnew)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(x,y)
plt.plot(xnew,y1new,color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolação Linear')

plt.subplot(2,1,2)
plt.plot(x,y)
plt.plot(xnew,y2new,color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolação Cubica')
plt.tight_layout()
plt.show()