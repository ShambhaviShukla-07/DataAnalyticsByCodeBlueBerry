n1=int(input("Enter the 1st number: "))
op=input("Choose and enter an operator form this list -> add , sub , mul , div : ")
n2=int(input("Enter the 2nd number: "))

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return float(n1/n2)


try:
    if op=="add":
        print("Result of ",n1,op,n2,"is : ",add(n1,n2))
    elif op=="sub":
        print("Result of ",n1,op,n2,"is : ",sub(n1,n2))
    elif op=="mul":
        print("Result of ",n1,op,n2,"is : ",mul(n1,n2))
    elif op=="div":
        print("Result of ",n1,op,n2,"is : ",div(n1,n2))
    else:
        print("Invalid input")
except ZeroDivisionError:
    print("Denominator can't be zero")
