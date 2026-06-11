#class Abc(self) - default constructor   
#name of class will start with capital letter

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    def getSalary(self):
        print(f"Hii!! {self.name}, your salary is {self.salary}")

obj1=Employee("Rahul",30000)
obj2=Employee("Abhay",40000)

print(obj1.name, "-", obj1.salary)
obj1.getSalary()

print(obj2.name,"-",obj2.salary)
obj2.getSalary()

