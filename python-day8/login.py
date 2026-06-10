
try:
    username=input("Enter username:")
    password=input("Enter Password:")
    if username=="":
        raise Exception("Username cannot be empty")
    if password=="":
        raise Exception("Password cannot be empty")    #raise - used to create custom exception
    print("Login Successful")
except Exception as e:
    print("Login Error: ",e)