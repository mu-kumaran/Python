class Employee_0:
    name = "john"
    age = 35
    designation = "Manager"
    
emp0 = Employee_0()
print(emp0.name)
print(emp0.age)
print(emp0.designation)

# using constructors (__init__)
class Employee_1:
    def __init__(self):
        self.name = "John"
        self.age = 35
        self.designation = "Manager"

emp1 = Employee_1()
print(emp1.name,emp1.age,emp1.designation)

# using parameterized constructors
class Employee_2:
    def __init__(self,name,age,designation):
        self.name = name
        self.age = age
        self.designation = designation

emp_1 = Employee_2('Hari',45,'Sr.Manager')
emp_2 = Employee_2('Vinoth',30,'Manager')
print(emp_1.name,emp_1.age,emp_1.designation)
print(emp_2.name,emp_2.age,emp_2.designation)

# adding methods and behaviours

class Employee:
    totalEmployees = 0

    def __init__(self,name,age,designation,salary):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary
        Employee.totalEmployees += 1

    def getEmployeeDetails(self):
        return self.name,self.age,self.designation,self.salary
    
    def updateSalary(self,newSalary):
        self.salary = newSalary
        print("Salary updated")
        return self.salary

class InternOne(Employee):
    pass

class Intern(Employee):
    def __init__(self, name, age, designation, salary,internPeriod):
        self.internPeriod = internPeriod
        # super().__init__(name, age, designation, salary)
        Employee.__init__(self,name,age,designation,salary)
    
    def getPeriod(self):
        return 'Internship period (in months) is', self.internPeriod
    
empOne = Employee('Srinivasan',28,'Jr.developer',25000)
print(empOne.getEmployeeDetails())
empTwo = Employee('Nagulan',38,'Manager',40000)
print(empTwo.getEmployeeDetails())
empOne.updateSalary(30000)
print(empOne.getEmployeeDetails())
print(Employee.totalEmployees)

internOne = InternOne('Tom',22,'Marketing Intern',120000)
print(internOne.getEmployeeDetails())        

intern1 = Intern('Manoj',32,'Python developer intern',450000,6)
print(intern1.getEmployeeDetails())  
print(intern1.getPeriod())  

# Method overriding
class Baseclass():
    def method(self):
        print("Base class method called")

class DerivedClass(Baseclass):
    def method(self):
        print("Derived class method is called")

obj1 = DerivedClass()
obj1.method()

class father():
    def name(self):
        print("Name of the father: Murugesan")

class son(father):
    def name(self):
        print("Name of the son: Thangappan")

obj_dad = father()
obj_son = son()
obj_dad.name()
obj_son.name()


