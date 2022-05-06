class BankAccount:
    def __init__(self, int_rate, balance): 
        self.intrest_rate = 0.01
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
    def display_account_info(self):
        print (f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if (self.balance > 0):
            self.balance *= self.intrest_rate

account1=BankAccount(.01, 0)
account1.deposit(100).display_account_info()

