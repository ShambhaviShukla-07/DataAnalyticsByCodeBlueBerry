def largest(n,m):
    if(n>m):
        return n
    elif(n==m):
        return "none"
    return m
n1=int(input("Enter the 1st number: "))
n2=int(input("Enter the 2nd number: "))
print("The largest of the two numbers is ",largest(n1,n2))