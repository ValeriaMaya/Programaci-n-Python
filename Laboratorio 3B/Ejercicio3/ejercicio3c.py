import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,2*math.pi,100)
x=np.sin(3*t)
plt.plot(t,x,linewidth=3,color='navy')
y=np.sin(4*t)
plt.plot(t,y,linewidth=3,color='olive')
plt.legend('XY')
plt.grid(True)
plt.title('Funciones trigonometricas')
plt.xlabel('x')
plt.ylabel('X(t),Y(T)')
plt.savefig('graf3c.png')
plt.show()
