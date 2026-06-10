#Tuples - () Tuples are ordered, immutable, and allows duplicate values
#Example employeeID cannot be duplicate
numbers=(1,2,3,2,5,"five")
#numbers[3]=56    #immutable
print(numbers.count(5))
print(numbers.index("five"))

#method - used after .    these are functions that are used numbers.count()
#function - used independently like len(numbers)