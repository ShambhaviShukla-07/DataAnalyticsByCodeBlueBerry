sales=["1500","5300","3500"]
sales2=["1500","5300","3500","fifteen hundred"]
total=0

try:
    for sale in sales:
        total+=int(sale)
    print(total)
except ValueError:
    print("Invalid data")

total2=0

try:
    for sale2 in sales2:
        total2+=int(sale2)
    print(total2)
except ValueError:
    print("Invalid data")
