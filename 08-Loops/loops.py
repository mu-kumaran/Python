#range()
# syntax : range(start,stop,step)

print(list(range(5)))
print(list(range(1,5)))
print(list(range(1,10,2)))
print(list(range(70,100,5)))

#for loop
# syntax:
# for val in sequence:
#     statements
print("for loop:")

for i in range(5):
    print(i)

for i in range(5):
    print("PythonX")

for i in "PythonX":
    print(i)

# while loop
# syntax:
# while boolean_expression:
#     statements

print("while loop:")
i=0
while(i<3):
    print("I love python")
    i = i+1

# break statement
print("break statement:")
str = "Goodmorning"
print(str)
for i in str:
    if(i=='m'):
        break
    else:
        print(i)
    
 # for-else statement
print(str)
letter = input("Enter the character you want to find in the given string:") 
for i in str:
    if(i==letter):
        print(letter,"found")
        break
else:
    print("letter not found")

# enumerate() function
squares = ['red','blue','green','yellow','white']

for (index,value) in enumerate(squares):
    print(index,value)