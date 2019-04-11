import numpy as np
import matplotlib.pyplot as plt

#Função de Bessel  de primeira espécie de ordem real
from scipy.special import jn

#Função de Bessel  de primeira espécie de ordem real e argumento complexo
from scipy.special import jv

#Função de Bessel  de segunda espécie de ordem real e argumento real
from scipy.special import yn

#Função de Bessel  de segunda espécie de ordem real e argumento complexo
from scipy.special import yv

#Função modificada de Bessel de primeira espécie e ordem real
from scipy.special import iv

#Função modificada de Bessel de segunda espécie e ordem inteira
from scipy.special import kn

#Função modificada de Bessel de segunda espécie e ordem real
from scipy.special import kv

x = np.linspace(0,5,50)

z = np.linspace(0,5,50)*1j

ordem = 2

y_jn = jn(ordem,x)

y_jv = jv(ordem,z)

plt.figure(1)
plt.plot(x,y_jn,color='black',label='J_n')
plt.plot(x,y_jv,color='blue',label='J_v')
plt.xlabel('X')
plt.ylabel('Bessel J')
plt.legend()
plt.show()

y_yn = yn(ordem,x)

y_yv = yv(ordem,z)

plt.figure(2)
plt.plot(x,y_yn,color='black',label='Y_n')
plt.plot(x,y_yv,color='blue',label='Y_v')
plt.xlabel('X')
plt.ylabel('Bessel Y')
plt.legend()
plt.show()

y_kn = kn(ordem,x)

y_kv = kv(ordem,z)

plt.figure(3)
plt.plot(x,y_kn,color='black',label='K_n')
plt.plot(x,y_kv,color='blue',label='K_v')
plt.xlabel('X')
plt.ylabel('Bessel K')
plt.legend()
plt.show()

y_iv = iv(ordem,x)

plt.figure(4)
plt.plot(x,y_iv,color='black',label='I_v')
plt.xlabel('X')
plt.ylabel('Bessel I')
plt.legend()
plt.show()