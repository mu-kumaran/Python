class employee:
    def __init__(self,name,age,designation,salary):    
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary

    def getEmployeeDetails(self):
        print(self.name)
        print(self.age)
        print(self.designation)
        print(self.salary)
        return (self.name,self.age,self.designation,self.salary)
    
    def updateSalary(self,newsalary):
        self.salary = newsalary
        print("salary updated")
        return self.salary
    
class intern(employee):
    def __init__(self, name, age, designation, salary,period):
        self.period = period
        super().__init__(name, age, designation, salary)

    def getInternDetails(self):
        return self.name,self.age,self.designation,self.salary,self.period

    def getInternPeriod(self):
        return "Internship period is: "+str(self.period)+" months"
emp1 = employee("john",35,"sr.developer",35000)
intern1 = intern("manoj",28,"python intern",10000,6)

emp1.getEmployeeDetails()
print(intern1.getInternDetails())
print(intern1.getInternPeriod())