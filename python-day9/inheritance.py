class Person:          #inherited class
    def greet(self):
        print("Hello")

class Student(Person):      #inheriting class
    def stud(self,name):
        print(f"This is {name}")

p=Person()
p.greet()
s=Student()
s.greet()
s.stud("Sheela")