import matplotlib.pyplot as plt
import numpy as np
import math
#Grafico 1
x=np.linspace(0,2,100)
f=x*math.e**(-3*x)
plt.plot(x,f,linewidth=3,color='purple')
#Grafico 2
g=(math.e**(-3*x))*(1-3*x)
plt.plot(x,g,linewidth=3,color='blue')
plt.legend('fg')
plt.grid(True)
plt.title('Funciones Exponenciales')
plt.xlabel('x')
plt.ylabel('f(x),g(x)')
plt.savefig('graf2b.png')
plt.show()
