n1=int(input("Enter the 1st number: "))
op=input("Choose and enter an operator form this list -> add , sub , mul , div , mod : ")
n2=int(input("Enter the 1st number: "))

if op=="add":
    result=n1+n2
elif op=="sub":
    result=n1-n2
elif op=="mul":
    result=n1*n2
elif op=="div" and n2!=0 :
    result=float(n1/n2)
elif op=="mod" :
    result=n1%n2
else:
    print("Invalid input")

print("Result of ",n1,op,n2,"is : ",result)