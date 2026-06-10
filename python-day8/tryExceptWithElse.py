try:
    num=int(input("Enter a number"))
except ValueError as ve:
    print("Error occures:",ve)
else:
    print("You entered:",num)
finally:
    print("Program Finished!!")