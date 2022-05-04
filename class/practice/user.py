class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0


    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print (self.name)
        print (self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User('Monty Python', 'monty@python.com')


guido.make_deposit(1000)
guido .transfer_money(monty, 500)
monty.display_user_balance()



