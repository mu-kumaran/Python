student = {
    'manoj':{
        'rno':1001,
        'std':'2nd',
        'grade':'A+',
        'result':'pass'
    },
    'sharmila':{
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

print(student.get('manoj').update({'result':'pass'}))

print(student.get('manoj'))