#sets

data = set()
print(data)
print(type(data))

set1 = {1,2,3}
set2 = {6,8.9,"james"}
print(set1)
print(set2)

#Accessing elements in sets
days = {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"}
print(days)

for day in days:
    print(day)

#Set operations

A = {1,2,3,4,5}
B = {4,5,6,7,8}

#union of sets
print(A|B)
print(A.union(B))

# Intersection of sets
print(A&B)
print(A.intersection(B))

# Set difference
print("A-B = ",A-B)
print("B-A = ",B-A)
print("A-B = ",A.difference(B))
print("B-A = ",B.difference(A))

# Built-in functions
age = {23,22,34,36,24,41}

print(len(age))
print(min(age))
print(max(age))
print(sorted(age))
print(sum(age))

# Built-in methods
age.add(56)
print(age)
age.remove(22)
print(age)
age.pop()
print(age)
age.clear()
print(age)

A = {1,2,3}
B = {1,2,3,4,5}
C = {100,101,102}
print(A.issubset(B))
print(B.issuperset(A))
print(A.isdisjoint(B))
print(A.isdisjoint(C))

bricsNations = {'B','R','I','C','S'}
bricsNations.discard('Z')
print(bricsNations)
# bricsNations.remove('Z') --> throws an error

