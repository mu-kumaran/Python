#Importing modules

# Simple import method
import math
print(math.factorial(5))

# rename method
import math as m
print(m.factorial(5))

# importing just the factorial function
from math import factorial 
print(factorial(5))

# custom module

import calculator as calc

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("Addition is", calc.add(a,b))

from calculator import sub

print("Subtraction is", sub(a,b))