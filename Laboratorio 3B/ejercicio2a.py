import matplotlib.pyplot as plt
import numpy as np
import math
#Grafico 1
x=np.linspace(0,4*math.pi,100)
s=np.cos(2*x)+np.sin(3*x)
plt.plot(x,s,linewidth=3,color='brown')
#Grafico 2
n=np.linspace(0,4*math.pi,100)
v=-2*(np.sin(2*n))+3*(np.cos(3*n))
plt.plot(n,v,linewidth=3,color='gold')
plt.legend('sv')
plt.grid(True)
plt.title('Funciones trigonometricas')
plt.xlabel('x')
plt.ylabel('s(x),v(x)')
plt.savefig('graf2a.png')
plt.show()
