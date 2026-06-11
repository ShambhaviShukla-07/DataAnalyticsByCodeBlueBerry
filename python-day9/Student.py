# __init__(self) is used to create constructor
# constructor automatically runs when an object is created
#self acts as the current object or reference to the specific object being created
# __init__

# class (Name in Capital)
class Student:
    print("I am Alice")

    def  __init__(self):
        self.name="Rahul"

    
stud=Student()
print(stud.name)

#Dynamic value using constructor
class Students:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    #function inside a class is called method
    def getMarks(self):
        num=self.marks/100*100
        print(f"You got {num} percent")

    def getAge(self):
        age=self.age
        print(f"Your age is {age}")

studentss=Students("Rahul",21,90)
studentss2=Students("Pinky",23,87)
studentss3=Students("Madhu",22,89)
print(studentss.name)
print(studentss.age)
print(studentss.marks)
print(studentss2.name)
print(studentss2.age)
print(studentss2.marks)
print(studentss3.name)
print(studentss3.age)
print(studentss3.marks)

#method access
studentss.getMarks()
studentss.getAge()

studentss2.getMarks()
studentss2.getAge()

studentss3.getMarks()
studentss3.getAge()
