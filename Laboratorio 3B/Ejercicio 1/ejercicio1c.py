import matplotlib.pyplot as plt
import numpy as np
import math as m
t=np.linspace(-1,5,100)
f=t*(m.e**(-2*t))
plt.plot(t,f,linewidth=3,color='purple')
plt.legend()
plt.title('f(t)=te^-2t')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True)
plt.savefig('graf1c.png')
plt.show()
