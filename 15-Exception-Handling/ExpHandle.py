# Exception handling

# NameError exception
name = "pythonx"
try:
    print(name)
except NameError:
    print("Some error occurred. Please contact the developer")

try:
    print(name)
except NameError as err:
    print("Some error occurred. Please contact the developer:",err)

# ZeroDivisionError exception

try:
    num1 = int(input("Enter the number1:"))
    num2 = int(input("Enter the number2:"))
    print("Division is:",num1/num2)
except ZeroDivisionError as err:
    print("Oops, You cannot divide the number by zero:",err)
except Exception as err:
    print("Error:",err)


# IOError
try:
    fp = open('data.txt','r')
    fp.read()
except IOError as err:
    print("File not found:",err)
except Exception as err:
    print("Error:",err)

#finally block
try:
    num1 = int(input("Enter the number1:"))
    num2 = int(input("Enter the number2:"))
    print("Division is:",num1/num2)
except ZeroDivisionError as err:
    print("Oops, You cannot divide the number by zero:",err)
except Exception as err:
    print("Error:",err)
finally:
    print("Thank you for using our calculator")

# using raise keyword
try:
    a = int(input("Enter a positive integer:"))
    if a<=0:
        raise ValueError("It is not a positive number")
except ValueError as err:
    print("Error:",err)

