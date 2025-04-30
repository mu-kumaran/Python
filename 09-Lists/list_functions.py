# built-in functions

numbers = [23,56,78,13,98,33]
print(len(numbers))
print(min(numbers))
print(max(numbers))

#built-in methods
names = ['James','Sam','Nick']
print(names)
names.append("Barry")
print(names)
print(names.index('Sam'))
names.insert(1,"Ron")
print(names)
names.remove('Nick')
print(names)
names.extend(['manoj','Vivek','Helen'])
print(names)

age = [18,67,45,18,35,23,18,22]
print(age.count(18))

# Smart lists - list comprehension
#general program
even = []
for x in range(1,11):
    if x%2 == 0:
        even.append(x)

print(even)

#using list comprehension
even1 = [x for x in range(1,11) if x%2==0]
print(even1)

str = "Hello, List"
char_list = [x for x in str]
print(char_list)

# String to list conversion
"Hard Rock".split() # output: ['Hard','Rock']
"A,B,C,D,E".split(",") # output: ['A','B','C','D','E'] 