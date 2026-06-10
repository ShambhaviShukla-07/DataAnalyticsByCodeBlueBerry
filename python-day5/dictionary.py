#Disctionary - {}    ordered, mutable, only duplicate keys not values (prints only 1 key if duplicate)

stu={
    "name":"Pihu",
    "age":20,
    "roll":25
}

print(stu)
print(stu["name"])    #key is used to access value

stuAll={
    "stu1":{
        "name":"Pihu",
        "age":20,
        "roll":25
    },
    "stu2":{
        "name":"Priya",
        "age":20,
        "roll":50
    }
}

print(stuAll["stu1"]["name"])
stu["name"]
stu["college"]="BIT"
print(stu.values())
print(stu.keys())
print(stu.items())

print(stu.get("name"))    #print(stu["name"])

#for key, value in stu.items()

for key,value in stu.items():
    print(key,value)