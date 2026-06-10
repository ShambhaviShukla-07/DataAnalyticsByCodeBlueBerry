try:
    marks=int(input("Enter marks: "))
    name=input("Enter your name: ")

    print(f"Hi! Your name is {name} and your marks is {marks}")
except ValueError:
    print("Please enter numeric input in marks")
def sum(a,b):
    return a+b
print(sum(2,3))