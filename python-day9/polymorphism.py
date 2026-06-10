#more than one class with same method behaving differently

class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("Meow")

dog=Dog()
dog.sound()

cat=Cat()
cat.sound()