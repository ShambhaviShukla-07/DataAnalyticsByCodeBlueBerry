str="Shambhavi"
print(str[-2])         #negative index

name="CodeBlueBerry"
print(name[0:4])          #slicing
l=len(name)       #length of string
print(l)

#concatenation
first="Hey"
second="guys"
concat=first+" "+second
print(concat)

#Repetition
print("Hello "*5)

#Methods
company="taTa"

print(company.upper())   #to upper case
print(company.lower())   #to lower case

course="data analytics internship"
print(course.title())      #first letter of every word becomes capital
print(course.capitalize())  #first letter of first word becomes capital

firstName="   Preety "
print(len(firstName))
print(firstName[0])
afterStrip=firstName.strip()    #removes extra space from both sides
print(afterStrip)
print(len(afterStrip))
leftStrip=firstName.lstrip()
print(leftStrip)
rightStrip=firstName.rstrip()
print(rightStrip)
print(len(leftStrip))
print(len(rightStrip))

#Replacing



#Splitting - converts data by default into list
data="Rahul,Aman,Priya,,Rahul,"
print(data[0])
print(type(data))
students=data.split(",")

print(type(students))
print(students)
print(students[0][0])

#Joining- Converts data in list into string
student=["Priya","Aman","Madhavi"]
print(type(student))
result="#".join(student)
print(type(result))
print(result)

#searching string - finds the index of the first letter of the word to be found
text="Data Analytics"
print(text.find("Analytics"))
print(text.find("Analytix"))

email="rahulgupta00@gmail.com"
print(email.startswith("rahul"))   #returns true if input starts with rahul else false

web="www.code.com"
print(web.endswith(".in"))   ##returns true if input starts with rahul else false


if(email.endswith("gmail.com")):
    print("Valid")
else:
    print("Invalid")

print("Rahul".isalpha())
print("74674".isdigit())
print("4o4hsd".isalnum())

#formatting string literals - use f" {}"