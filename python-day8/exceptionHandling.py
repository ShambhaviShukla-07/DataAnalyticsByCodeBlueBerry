num=10

try:   #inside try block: Code that can generate error
    print(num/0)
except:    #runs only when an error occurs
    print("An error occured")

try:
    print(num/0)
except ZeroDivisionError:
    print("Number not divisible by 0")

try:
    print(name)
except NameError:
    print("name is not defined")

# ValueError
# IndexError
# KeyError
# FileNotFoundError
try:
    age=int(input("Enter Age: "))
except ValueError:
    print("Age can't be string")

print("Hello")      #Runs normally after try catch


#handling multiple errors

try:
    num=int(input("Enter a number"))
    print(10/num)
except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Cannot be divided by zero")

