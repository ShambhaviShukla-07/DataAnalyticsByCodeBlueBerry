# __ is used for making a variable private
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age    #private property

    def getAge(self):
        return self.__age
    
p1=Person("Emila",21)
print(p1.name)
print(p1.getAge())