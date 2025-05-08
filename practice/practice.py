import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,num=100)
y = np.sin(x)

# %matplotlib inline
plt.plot(x,y)
plt.title("Sin(x) function")
plt.xlabel("X")
plt.ylabel("Sin(X)")
plt.show()
