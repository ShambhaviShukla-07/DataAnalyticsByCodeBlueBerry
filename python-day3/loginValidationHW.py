username=input("Enter your username: ")
password=int(input("Enter your password: "))

if(username=="shambhavi" and password==230525):
    print("Login Successful!")
elif(username!="shambhavi" and password==230525):
    print("Wrong username")
elif(username=="shambhavi" and password!=230525):
    print("Wrong password")
else:
    print("Both credentials are wrong!")