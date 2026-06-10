name=input("Enter student's name: ")
s1=int(input("Enter marks of subject 1: "))
s2=int(input("Enter marks of subject 2: "))
s3=int(input("Enter marks of subject 3: "))

firstLine=""
with open("stuRecord.csv","a+") as stFile:
    firstLine=stFile.readline()
    if(firstLine==" "):
        stFile.write(f"Name,Subject 1,Subject 2,Subject 3\n")
    stFile.write(f"{name},{s1},{s2},{s3}\n")

