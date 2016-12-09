import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-6,2,100)
y=5-(4*x)-x**2
plt.plot(x,y,linewidth=3,color='orange')
plt.legend()
plt.title('f(x)=5-4x-x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.savefig('graf1a.png')
plt.show()
