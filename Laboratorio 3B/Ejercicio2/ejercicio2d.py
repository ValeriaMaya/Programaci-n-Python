import matplotlib.pyplot as plt
import numpy as np
import math
#Grafico 1
t=np.linspace(0,2*math.pi,100)
x=(1+2*np.sin(t))*np.cos(t)
plt.plot(t,x,linewidth=3,color='black')
#Grafico 2
y=(1+2*np.sin(t))*np.sin(t)
plt.plot(t,y,linewidth=2,color='yellow')
plt.legend('XY')
plt.grid(True)
plt.title('Funciones trigonometricas')
plt.xlabel('x')
plt.ylabel('X(t),Y(T)')
plt.savefig('graf2d.png')
plt.show()
