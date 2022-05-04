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

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = BankAccount(.01, 0)


    def make_deposit(self, amount):
        self.account_balance.deposit(amount)
        return self

    def make_withdrawl(self, amount):
        self.account_balance.withdraw(amount)
        return self

    def display_user_balance(self):
        print (self.name)
        self.account_balance.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance.withdraw(amount)
        other_user.account_balance.deposit(amount)
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User('Monty Python', 'monty@python.com')


guido.make_deposit(1000).transfer_money(monty, 500).display_user_balance()
monty.display_user_balance()

