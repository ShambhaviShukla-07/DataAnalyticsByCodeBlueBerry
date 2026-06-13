import numpy as np

sales=np.array([1000,2000,3000,4000])
print(sales*1.10)
print(sales+100)
print(sales-100)
print(sales*2)
print(sales/2)

num=np.array([2,3,4])
print(num**3)

oct_sales=np.array([1000,2000,3000,4000])
nov_sales=np.array([90,23,43,65])
print(oct_sales+nov_sales)

#Comparision
marks=np.array([90,23,43,65,57,87,88])
print(marks>33)      #gives answer in the form of true or false array
print(marks==88)     

#Filtering
print(marks[marks>33])
print(marks[marks<33])

#aggregate function
#min max sum mean

#finds the standard deviation of an array
print(np.std(marks))

arr=np.array([1,2,3,4,5,6])

#reshapes or changes the dimension of an array
newArr=np.reshape(arr,(2,3))
print(newArr)

#converts any dimensional array into 1D array
print(newArr.flatten())

num=np.array([2,5,5,2,2,7,3,8,7,8])
print(np.sort(num))
print(np.unique(num))


