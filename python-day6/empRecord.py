empName=input("Enter emp name")
empSalary=input("Enter emp salary")

firstLine=""
try:
    with open("emp.txt","r") as empRecord:
        firstLine=empRecord.readline()
except FileNotFoundError:
    print("File does not exist")


with open("emp.txt","a") as empRecord:
    if(firstLine==" "):
            empRecord.write("EmpName - Salary\n")
    empRecord.write(empName+" - "+empSalary+"\n")
