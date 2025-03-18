# dictionaries

dict1 = {}

dict2 = {
    1: "Sam",
    2: "John"
}

studentsEnrolled= {
    "John": "Python",
    "Sam": "Java",
    "Nick": ["Python","Javascript"]
}

print(studentsEnrolled)

#Manipulating dictionaries

# Accessing elements
example = {
    1:"John",
    2:"Nick"
}

print(example[1])
print(example.get(2))

# Updating elements
names = {
    1:"Sam",
    2:"Helen"
}
print(names)
names[1] = "mano"
names[2] = "sudhan"
names[3] = "dinesh"
print(names)

#deleting elements

del names[3]
print(names)

# Dictionary functions
empData = {
    101: "Bravo",
    102: "Asten",
    103: "Kerry"
}

print(empData.keys())
print(empData.values())
print(empData.items())
empData.update({104:"Curan",105:"Elly"})
print(empData)
print(empData.get(104))

continent = {
    "Asia":["India","UAE","China"]
}

continent["Asia"].append("Japan")
print(continent)
continent["Asia"].remove("China")
print(continent)

pizza = {
    "Toppings":['Onions','Mushrooms','Cucumber']
}
pizza.get("Toppings").remove('Cucumber')
print(pizza)
pizza.get("Toppings").append('Pepperoni')
print(pizza)

# Iterating over dictionaries
empData = {
    101: "Bravo",
    102: "Asten",
    103: "Kerry"
}
for i in empData:
    print(i)        # returns keys

for i in empData.values():
    print(i)        # returns values

for i in empData.items():
    print(i)        # returns both keys and values in tuple form
    print(i[0])     # returns keys
    print(i[1])     # returns values

