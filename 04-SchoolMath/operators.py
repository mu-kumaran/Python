# operators

# Arithmetic operators
a=35
b=18
res1=a+b 
print("a = ",a," b = ",b)
print("Addition is ",res1)
print("Subtraction is ",a-b)
print("Multiplication is ",a*b)
print("a/b = ",a/b)
print("a modulus b = ",a%b)
print("Floor division is ",a//b)
print("Exponential is ",a**b)

# Comparison operators

age = 18
reqd_age = 36
print(age>reqd_age)
print(age<reqd_age)
print(age == reqd_age)
print(age != reqd_age)

# Logical operators

x = True
y = False
print('x = ',x,' y = ',y)
print('x and y is ',x and y)
print('x or y is ',x or y)
print('not x is ', not x)
print('not y is ', not y)

num1 = 5
num2 = 8
print(num1>num2 or num1<num2)

# Membership operator
name = 'manoj'
print('a' in name)
print('x' in name)
print('m' not in name)
print('y' not in name)

# Identity  operator
num1 = 5
num2 = 5
num3 = 6
print(id(num1))
print(id(num2))
print(id(num3))
print(num1 is num2)
print(num1 is not num3)

# Walrus operator
name = 'manoj'
print(name)
print(name1:='ganesh')
print(name1+name)