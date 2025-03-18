#Finding marks of the student

marks = {
    "mano": 89,
    "john": 91,
    "peter": 87
}
stud = input("Enter the student name: ")
if stud in marks.keys():
    print("Student found")
    print(stud,"mark is",marks.get(stud))
else:
    print("Student not found")