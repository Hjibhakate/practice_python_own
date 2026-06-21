class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposite(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def show_balance(self):
        print(f"{self.balance}")

p1 = BankAccount("harshad",500000)

p1.deposite(500)
p1.withdraw(100)

p1.show_balance()
        