try:
    with open("abc.txt","r") as file:
        firstLine=file.readline()
except FileNotFoundError:
    print("This file does not exist!!")