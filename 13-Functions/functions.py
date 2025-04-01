# Functions

def sayHello(name="user"):
    print("Hello",name)
    return 0

def add(num1=10,num2=20):
    num3 = num1+num2
    return num3

def paymentStatus(status="rejected"):
    print("Payment",status)
    return 0

sayHello()
sayHello("John")
print(add())
print(add(5,6))
print(add("Manoj ","Kumar"))
paymentStatus()
paymentStatus("accepted")

# lambda functions

import math
add = lambda num1,num2: num1+num2
squared = lambda n: n*n
sqrt = lambda n: math.sqrt(n)
print(add(80,20))
print(squared(9))
print(sqrt(4))

# map() function

def square(x):
    return x*x

numbers = [1,2,3,4,5]
squared_numbers = map(square,numbers)
print(list(squared_numbers))


# filter() function 

def is_even(x):
    return x%2 == 0

numbers = [1,2,3,4,5,6]
even_numbers = filter(is_even,numbers)
print(list(even_numbers))

# reduce() function
from functools import reduce
def add(x,y):
    return x+y

numbers = [1,2,3,4,5,6,7,8,9,10]

sum = reduce(add,numbers)
print(sum)

# round() function
print(round(38.56789,3))
print(round(45.668356,1))
print(round(234.356356,0))

# range() function
even = list(range(2,10,2))
print(even)
odd = list(range(1,10,2))
print(odd)
whole_nos = list(range(10))
print(whole_nos)