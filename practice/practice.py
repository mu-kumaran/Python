# print("Prime number check")
# num = int(input("Enter the number:"))
# if(num <= 1):
#     print("Its not a prime")
# else:
#     for i in range(2,int(num**0.5)+1):
#             print(i)
#             if(num%i==0):
#                 print(f"Its not a prime. It is divisible by {i}")
#                 break
#     else:
#         print("Its a prime number")

num = 8
print(num**0.5)
print(int(num**0.5))

def add(a=2,b=30):
    return a+b

def iseven(a):
    if a%2==0:
        return True
    
print(add(5,2))
print(add())

square = lambda n=3:n*n
addi = lambda a=2,b=3: a+b

print("lambda functions")
print(square(4))
print(square(4.5))
print(square())
print(addi(10,50))
print(addi())

print("map,filter,reduce functions")

from functools import reduce
num = list(range(1,11))
print(num)

A = list(map(square,num))
print("squared numbers:",A)

B = list(filter(iseven,num))
print("Even numbers:",B)

C = reduce(addi,num)
print("Summation:",C)