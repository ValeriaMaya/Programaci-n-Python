import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,2*math.pi,100)
x=np.cos**3(t)
plt.plot(t,x,linewidth=3,color='grey')
y=np.sin**3(t)
plt.plot(t,y,linewidth=3,color='pink')
plt.legend('XY')
plt.grid(True)
plt.title('Funciones trigonometricas')
plt.xlabel('x')
plt.ylabel('X(t),Y(T)')
plt.savefig('graf3a.png')
plt.show()
