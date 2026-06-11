class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"You deposited {amount}. \nNew balance is {self.balance}\n")
        else:
            print("No new amount deposited!\n")
    
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(f"You withdrew {amount}. \nNew balance is {self.balance}\n")
        elif amount>self.balance:
            print("Insufficient Balance\n")
        else:
            print("No new amount widhdrawn\n")

    def checkBalance(self):
        print(f"Account-holder name: {self.name}\nAccount Balance: {self.balance}\n")

ob1=BankAccount("Bob",100)

ob1.checkBalance()
ob1.deposit(1000)
ob1.withdraw(10)
ob1.checkBalance()

