#list - ordered, changable/mutable, and can store duplicate values
list1=[1,2,3,1,5]
print(list1[0])

l=len(list1)    #len() is used to find the length of the list
print(l)

for i in range(l):
    print(list1[i])

for num in list1:         #looping through lists  ("in" keyword is used for looping through lists)
    print(num)

list1[3]=56         #mutable/changeable
for num in list1:
    print(num)

print(list1[-1])

#methods of list
list2=["Rishi","riya",68,34]
list1.append(7)
list2.insert(3,"Madhu")
print(list2)
list2.pop(2)

numbers=[5,3,8,1,9]
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)