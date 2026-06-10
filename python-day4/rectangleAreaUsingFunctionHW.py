area=0
def rectArea(l,b):
    area=l*b
    return area
length=float(input("Enter length of the rectangle: "))
breadth=float(input("Enter breadth of the rectangle: "))
print("Area of rectangle with length=",length," and breadth=",breadth," is ",rectArea(length,breadth))
