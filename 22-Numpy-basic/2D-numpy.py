# 2D numpy array

import numpy as np 

# Basics and array Creation in 2D
a = [[1,2,3],[4,5,6],[7,8,9]]
x = np.array(a)
print(a)
print(type(a))
print(x)
print(type(x))
print(x.shape)
print(x.ndim)
print(x.size)

# Indexing and slicing in 2D

print(x[0,0])
print(x[1,2])

x[1,1] = 45

print(x)

print(x[0,0:2])
print(x[0:2,2])

# Basic operations in 2D

# Matrix addition and subtraction
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
x = np.array(a)
y = np.array(b)

z = x+y
z_sub = x-y
print(z)
print(z_sub)

# Hadamard product
z_prod = x*y
print(z_prod)

# Matrix multiplication (dot product)
z_mult = np.dot(x,y)
print(z_mult)

# multiply by scalar
z1 = 2*x
z2 = 5*y
print(z1)
print(z2)

# Matrix transformation
A = np.array([[1,2,3],[4,5,6]])
ATrans = A.T
print(A)
print(A.shape)
print(ATrans)
print(ATrans.shape)