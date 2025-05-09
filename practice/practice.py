import numpy as np
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
x = np.array(a)
y = np.array(b)

z = x+y
z_sub = x-y
print(z)
print(z_sub)

z_prod = x*y
print(z_prod)

z_mult = np.dot(x,y)
print(z_mult)

z1 = 2*x
z2 = 5*y
print(z1)
print(z2)

A = np.array([[1,2,3],[4,5,6]])
ATrans = A.T
print(A)
print(A.shape)
print(ATrans)
print(ATrans.shape)


