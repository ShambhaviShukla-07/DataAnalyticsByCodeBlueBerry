n=int(input("Enter number of subjects: "))
marks=[]
if(n>=3):
    for i in range(0,n):
        m=int(input("Enter marks of each subject: "))
        marks.append(m)
    print(marks)
    marks[0]=89
    for mark in marks:
        print(mark)

    marks.insert(3,79)
    print(marks)
