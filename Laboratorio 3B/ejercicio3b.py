import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(-2*math.pi,2*math.pi,100)
x=t+2*np.sin(2*t)
plt.plot(t,x,linewidth=3,color='violet')
y=t+2*np.cos(5*t)
plt.plot(t,y,linewidth=3,color='lime')
plt.legend('XY')
plt.grid(True)
plt.title('Funciones trigonometricas')
plt.xlabel('x')
plt.ylabel('X(t),Y(T)')
plt.savefig('graf3b.png')
plt.show()
