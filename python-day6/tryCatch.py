try:
    file=open("stud.txt","r")
    print(file.read())
except FileNotFoundError:
    print("ye file exist nhi krti")
