def userName(name="user"):
    print("Hello",name)
    return 0

userName()
userName("manoj")

def add(a='hello',b='world'):
    c = a+b
    return c

print(sum := add(5,6))
print(name:= add("manoj","kumar"))

import math
sum = lambda num1,num2: num1+num2
sqrt = lambda n: math.sqrt(n)

print(sum(78,95.6))
print(sqrt(8))