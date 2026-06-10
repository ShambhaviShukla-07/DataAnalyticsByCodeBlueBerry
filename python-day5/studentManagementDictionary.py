stuAll={
    "stu1":{
        "name":"Pihu",
        "age":20,
        "roll":25
    },
    "stu2":{
        "name":"Priya",
        "age":23,
        "roll":50
    },
    "stu3":{
        "name":"Vaibhav",
        "age":21,
        "roll":70
    },
    "stu4":{
        "name":"Vaibhavi",
        "age":22,
        "roll":68
    }

}
print(stuAll["stu1"]["name"])

for key,value in stuAll.items():
    print(key,value)