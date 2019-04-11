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
	
f1 = interp1d(x, y, kind='nearest')
f2 = interp1d(x, y, kind='previous')
f3 = interp1d(x, y, kind='next')	

xnew = np.linspace(xmin, xmax, size2, endpoint=True)
y1new = f1(xnew)
y2new = f2(xnew)
y3new = f3(xnew)

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(x,y)
plt.plot(xnew,y1new,color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolação nearest')

plt.subplot(3,1,2)
plt.plot(x,y)
plt.plot(xnew,y2new,color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolação previous')

plt.subplot(3,1,3)
plt.plot(x,y)
plt.plot(xnew,y3new,color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolação next')
plt.tight_layout()
plt.show()