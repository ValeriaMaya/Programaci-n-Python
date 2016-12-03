import matplotlib.pyplot as plt
import numpy as np
import math
#Grafico 1
t=np.linspace(0,4*math.pi,100)
f=np.sin(3*t)*np.cos(2*t)
plt.plot(t,f,linewidth=2,color='green')
#Grafico 2
g=(1/2*np.cos(t))+(5/2*np.cos(5*t))
plt.plot(t,g,linewidth=2,color='orange')
plt.legend('fg')
plt.grid(True)
plt.title('Funciones trigonometricas')
plt.xlabel('x')
plt.ylabel('f(t),g(t)')
plt.savefig('graf2c.png')
plt.show()
