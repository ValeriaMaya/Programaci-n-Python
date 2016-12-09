import matplotlib.pyplot as plt
import numpy as np
import math as m
t=np.linspace(0,24,100)
h=(m.e**(-0.1*t))*np.sin(2*t)
plt.plot(t,h,linewidth=3,color='green')
plt.legend()
plt.title('h(t)=e^-0.1t*sen(2t)')
plt.xlabel('t')
plt.ylabel('h(t)')
plt.grid(True)
plt.savefig('graf1d.png')
plt.show()
