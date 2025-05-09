import numpy as np

# Basic Array creation
a = np.array([1,2,3,4])
b = np.array([1.1,2.64,3.92,210.56])
print(a)
print(type(a))
print(a.dtype)
print(a.ndim)
print(a.shape)
print(type(b))
print(b.dtype)

# Indexing and slicing
c = np.array([20,1,2,3,4])
print(c)
c[0] = 100
c[4] = 0
print(c)
d = c[1:3]
print(d)
c[3:5] = 300,400
print(c)

x = np.array(list(range(1,11)))
print(x)

index = [2,4,6,8]
print(index)

y = x[index]
print(y)

x[index] = 100
print(x)

# Basic operations
# Vector addition and subtraction
# Through list operations
u = [1,0]
v = [0,1]
z = [] 
j = []
for n,m in zip(u,v):
    z.append(n+m)
    j.append(n-m)
print(z,j)

# Through numpy operation

u = np.array([0,1])
v = np.array([1,0])
z = u+v
j = u-v
print(z,j)

# Array multiplication with scalar
x = [0,1]
y = [1,0]
u = np.array(x)
v = np.array(y)
z = 2*u
j = 2*v
print(z,j)

l = [] # --> Through list operation
for n in x:
    l.append(2*n)
print(l)

# Hadamard product
x = [1,2]
y = [3,2]
u = np.array(x)
v = np.array(y)
z = u*v
print(z)

l= []
for n,m in zip(x,y):
    l.append(n*m)

print(l)

# Dot product
x = [1,2]
y = [3,2]
u = np.array(x)
v = np.array(y)
z = np.dot(u,v)
print(z)

l = 0
for n,m in zip(x,y):
    l = l + (n*m)
    
print(l)

# Adding constant to numpy array
u = np.array([1,2,3,-1])
z = u+1
print(z)

# universal functions
# mean()
u = np.array([1,2,3,-1])
z = u.mean()

print(z)

# max()
u = np.array([1,2,3,5])
z = u.max()

print(z)

# pi and sin()
x = np.array([0,np.pi/2,np.pi])
y = np.sin(x)
print(y)

# linspace()
x = np.linspace(-2,2,num=5)
y = np.linspace(-2,2,num=9)
print(x)
print(y)

# matplotlib library

import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,num=100)
y = np.sin(x)

# %matplotlib inline --> for jupyter notebook
plt.plot(x,y)
plt.title("Sin(x) function")
plt.xlabel("X")
plt.ylabel("Sin(X)")
plt.show()

