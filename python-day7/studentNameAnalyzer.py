fullName=input("Enter your full name: ")
fullName=fullName.title()
cleanedFullName=fullName.strip()

if not cleanedFullName:
    print("Name cannot be empty")

name=cleanedFullName.split(" ")
firstName=name[0]
if len(name)==3:
    middleName=name[1]
    lastName=name[2]
else:
    lastName=name[1]
    middleName=""

try:
    for i in range(0,len(name)):
        for ch in name[i]:
            if not (ch.isalpha()):
                raise ValueError("Name can only contain alphabets")
except ValueError as e:
    print("Error",e)

if not ValueError:
    print(f"Your name is {firstName} {middleName} {lastName} ")
else:
    print("Give a valid name!")


