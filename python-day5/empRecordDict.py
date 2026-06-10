emp1={
    "Name":"Aman",
    "Salary":50000,
    "Dept":"R&D",
    "EmpID":"RD:23"
}
emp2={
    "Name":"Mina",
    "Salary":60000,
    "Dept":"Managment",
    "EmpID":"M:19"
}
emp3={
    "Name":"Neha",
    "Salary":55000,
    "Dept":"IT",
    "EmpID":"IT:55"
}
print(emp1.keys()," : ",emp1.values())
print("\n\n")

for key,value in emp1.items():
    print(key,value)
print("\n")
for key,value in emp2.items():
    print(key,value)
print("\n")
for key,value in emp3.items():
    print(key,value)
print("\n")
emp1["Salary"]=58000
emp1["Incentive"]=5000
for key,value in emp1.items():
    print(key,value)