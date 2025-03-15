#if-else conditionals
age = int(input("Enter your age: "))
if (age>=18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


#if-elif-else conditionals

mark = int(input("Enter your mark to get grade below: "))
if(mark>=90):
    print("Grade: Excellent")
elif(mark>=75 and mark<90 ):
    print("Grade: First Class")
elif(mark>=40 and mark<75):
    print("Grade: Average")
else:
    print("Grade: Fail")

#Nested if conditionals

username = input("Enter your username: ")
if (username=="manoj"):
    password = input("Enter your password: ")
    if (password=="12345"):
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("User not found")
