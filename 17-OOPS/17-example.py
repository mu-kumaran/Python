class School:
    def __init__(self,name,city,student_strength,staff_strength,year):
        self.name = name
        self.year = year
        self.city = city
        self.staff_strength = staff_strength
        self.student_strength = student_strength

    def schoolDetails(self):
        print("Schoolname:",self.name)
        print("Year of Opening:",self.year)
        print("City:",self.city)
        print("No of staffs:",self.staff_strength)
        print("No of students:",self.student_strength)
        print("")
        

    def updateStaffStrength(self,newStaffStrength):
        self.staff_strength = newStaffStrength
        print("No of staffs updated as",self.staff_strength,"in",self.name)
        return self.staff_strength
    
    def updateStudentStrength(self,newStudentStrength):
        self.student_strength = newStudentStrength
        print("No of students updated as",self.student_strength,"in",self.name)
        return self.student_strength
    

kvv = School("Karur Vetri Vinayaka Higher Secondary School","Karur",3500,85,2014)
kvv.schoolDetails()

cheran = School("Cheran Matric Higher Secondary School","Karur",4000,80,1985)
cheran.schoolDetails()

kvv.updateStudentStrength(4500)
kvv.updateStaffStrength(90)

print("")
kvv.schoolDetails()

