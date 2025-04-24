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

# Accessing and updating list inside dictionaries

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

studEnroll = {
    'john':['java','python'],
    'mano':['c++','web tech'],
    'ganesh':['ruby','MySQL']
}

print(studEnroll)
studEnroll['mano'].remove('web tech')
print(studEnroll)
studEnroll['mano'].append('mern stack')
print(studEnroll)

print(studEnroll['john'][0])
studEnroll['john'][1] = 'dotnet'
print(studEnroll['john'])

# Accessing and updating nested dictionaries

stud_profile = {
    1001 : {
        'name':'manoj',
        'std':'10th',
        'marks':989
    }
}

print(stud_profile)
print(stud_profile[1001])
print(stud_profile[1001]['name'])
stud_profile[1001]['name'] = 'sudhan'
print(stud_profile[1001])

student = {
    'manoj':{
        'rno':1001,
        'std':'2nd',
        'grade':'A+',
        'result':'pass'
    },
    'hari':{
        'rno':1002,
        'std':'3rd',
        'grade':'A',
        'result':'pass'
    }
}

print(student)
print(student.keys())
print(student.values())
print(student.items())

del student['manoj']['result']

print(student.get('manoj'))

student.get('manoj').update({'result':'pass'})

print(student.get('manoj'))