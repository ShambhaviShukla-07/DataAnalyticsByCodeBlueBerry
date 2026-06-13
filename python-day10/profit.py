import numpy as prof

sales=prof.array([20000,45000,30000,50000])
print(sales*1.10)  #increase all sales by 10%

#statistical operations
print(prof.sum(sales))  
print(prof.mean(sales))
print(prof.max(sales))
print(prof.min(sales))

# automatically make array with 5 zeros
zero=prof.zeros(5)
#automatically make array with 5 ones
one=prof.ones(5)
print(zero)
print(one)

#automatically make array with numbers ranging from 1 to 99
z=prof.arange(1,100)
print(z)

