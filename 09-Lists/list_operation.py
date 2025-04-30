 # Operations on lists

# Concatenation  and repetition

list1 = [1,2,3,"manoj"]
list2 = [4,5,6,"Kumar"]
list_add = list1+list2
list_repeat = list1*3

print(list_add)
print(list_repeat)

# Membership operator

enrolledList = ['Sam','Mike','Kane','Nick']
print('Sam' in  enrolledList)
print('sam' in  enrolledList)
print('Samuel' in  enrolledList)
print('Samuel' not in  enrolledList)

#list iteration
fruits = ['Apple','Mango','Cherry','Banana']
for i in fruits:
    print(i)

for i in fruits:
    if i=="Mango":
        print("Mango found")
        break
else:
    print("Mango not found")

eurC = ['Ireland','Poland','Finland','France','Iceland','Spain']
for country in eurC:
    if 'land' not in country:
        print(country)

# List Aliasing
A = [1,2,3,4,5]
B = A
B[0] = 9
print(B)
print(A)

# List Cloning


    