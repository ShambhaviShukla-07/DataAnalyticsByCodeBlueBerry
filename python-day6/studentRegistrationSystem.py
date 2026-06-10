name=input("Enter your name:")
age=int(input("Enter your age: "))
course=input("Enter the course you want to register into: ")
phone=int(input("Enter your phone number: "))
def count(number):
    digit=0
    while number!=0:
        number //= 10
        digit+=1
    return digit

def validatePhone(ph):
    if count(ph)!=10:
        raise ValueError("Invalid phone number! It must be exactly 10 digits!!!")

firstLine=""
try:
    with open("studentRecord.csv","r") as stRecord:
        firstLine=stRecord.readline()
except FileNotFoundError:
    print("File does not exist")

try:
    validatePhone(phone)
    with open("studentRecord.csv","a") as stRecord:
        if(firstLine==" "):
            stRecord.write("Name,Age,Course,Phone\n")
        stRecord.write(f"{name},{age},{course},{phone}\n")
except ValueError as e:
    print("Registration Failed : ",e)

