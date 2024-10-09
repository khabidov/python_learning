class BankAccount:
    def __init__(self,name, balance=0):
        self.name=name
        self.balance=balance

    def deposit(self, cash_amount):
        self.balance+= cash_amount

    def cash(self, cash_amount):
        self.balance-=cash_amount

    def my_balance(self):
        return (self.balance)

sasha=BankAccount('Sasha')
print(sasha.my_balance())
sasha.deposit(10)
print(sasha.my_balance())
sasha.cash(4)
print(sasha.my_balance())