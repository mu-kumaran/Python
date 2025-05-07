import numpy as np

a = np.array([1,2,3,4])
b = np.array([1.1,2.64,3.92,210.56])
print(a)
print(type(a))
print(a.dtype)
print(a.ndim)
print(a.shape)
print(type(b))
print(b.dtype)

c = np.array([20,1,2,3,4])
print(c)
c[0] = 100
c[4] = 0
print(c)
d = c[1:3]
print(d)
c[3:5] = 300,400
print(c)