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

add = lambda num1,num2: num1+num2
squared = lambda n: n*n
print(add(80,20))
print(squared(9))