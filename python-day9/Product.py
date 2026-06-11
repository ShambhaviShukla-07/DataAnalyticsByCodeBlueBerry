class Product:
    def __init__(self,pname,price):
        self.pname=pname
        self.price=price
    def getPrice(self):
        print(f"The product {self.pname} has price {self.price}")

p1=Product("Acer Laptop",50000)
p2=Product("Lenovo Laptop",49000)

p1.getPrice()
p2.getPrice()
