#Formatting strings

#General method
user = "manoj"
print("Hello",user)

#using str.format with {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(("Hello, {}. You are {} years old").format(name,age))

#Format placeholders
string1 = "My name is {fname}, I am {age} years old".format(fname="manoj",age=33) 
string2 = "My name is {0}, I am {1} years old".format("manoj",33) 
string3 = "My name is {}, I am {} years old".format("manoj",33) 

print(string1)
print(string2)
print(string3)

#fstrings
print("f-strings:")
name = input("Enter your name: ")
print(f"Hello,{name}!")

num1 = 10
num2 = 5
print(f"Ten plus five equals {num1+num2}")

#Index concept - Accessing values
print("Index concept:")
appName = 'PythonX'
print(appName[0])
print(appName[1])
print(appName[2])
print(appName[3])

# Negative indexing
print("Negative indexing concept")
print(appName[-1])
print(appName[-2])
print(appName[-3])
print(appName[-4])
print(appName[-5])
print(appName[-6])
print(appName[-7])

# String slicing - getting substring

# string_name[start:end:step]
# start index - included
# end index - excluded

print("String slicing:")
appName = 'PythonX'
print(appName[:])
print(appName[::])
print(appName[:4])
print(appName[2:5])
print(appName[3:])
print(appName[::2])

# Operations on strings

# concatenation
firstname = "John"
lastname = "Doe"
fullname = firstname +" "+ lastname
message ="Welcome to Jumanji"
print(fullname) 
print(" ".join([firstname,lastname]))

print(";".join([message,"Again"]))

#Repetition
str = "python"
print(str*2)

#string methods
str = "Python"
print(str.islower())
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.replace('P','A'))

# len() method
str = "Love Python"
print(len(str))

