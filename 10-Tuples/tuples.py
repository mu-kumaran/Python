#tuples

tup1 = (1,2,3,"manoj",98.3,45.6,True)
tup2 = (15,34,65,78)
tup3 = ()
print(tup1)
print(tup1,tup2,tup3)
print(tup1+tup2+tup3)

employees_birth_years = (1989,1991,1995,1998,1976)
print(employees_birth_years)

# Manipulating tuples
languages = ('python','ruby','java','php')
print(languages)
#accessing elements
print(languages[0])
print(languages[2])
#slicing tuples
print(languages[1:4])
# updating tuples - not allowed
# languages[3] = 'lisp'  throws an error
# Deleting tuple elements - not allowed
# del languages[3] throws an error
# Deleting entire tuple
del languages

# Tuple operations
#concatenation and repetition
tup1 = (1,2,3)
tup2 = (4,5,6)
print(tup1+tup2)
print(tup1*3)

#membership
names = ('sam','mike','kane','nick')
print('sam' in names)
print('samuel' in names)

# Tuple iterations
cities = ("London","New york","Paris","Texas")
for x in cities:
    print(x)

#built-in functions
numbers = (23,56,78,13,98,33)
print(len(numbers))
print(min(numbers))
print(max(numbers))

#built-in methods
age = (18,67,45,18,35,23,18,22)
print(age.count(18))
print(age.index(45))