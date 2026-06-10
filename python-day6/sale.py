total=0

with open("sale.txt","r") as f:
    for line in f:
        print("line",line)
        print("total",total)
        total+=int(line)
        print("total value after calculation",total)
        print("--------------------")

print("Total",total)