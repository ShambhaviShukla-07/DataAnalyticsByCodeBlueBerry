import numpy as np
#Python List
sale=[100,200,"Ram",300]
#NumPy Array - ndarry (nth D array)
sales=np.array([100,200,300,400])
d2array=np.array([
    [200,300],
    [100,500],
    [600,400]
    ])
print(type(sales))
print(sales)
print(type(sale))
print(sale)

data=np.array([
    [[1,2,3]],
    [[4,5,6]],
    [[7,8,9]]
])
print(data.shape)  
print(data.ndim)  #dimension of array

#using numpy
saless=np.array([100,200,300,400,500])
print(saless[1:4]) #slicing
print(saless+120)

#using normal python
num=[100,200,300,400]
for i in range(len(num)):
    num[i]+=120
print(num)