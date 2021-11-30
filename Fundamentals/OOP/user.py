class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit, the specific user's account increases by the amount of the value received
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(self.account_balance)
        return self
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jaden = User("Jaden Willeiksen", "email@email.com")

guido.make_deposit(100).make_deposit(200).make_deposit(20).transfer_money(jaden, 100).display_user_balance()

monty.make_deposit(700).make_deposit(50).make_withdrawal(50).display_user_balance()

jaden.make_deposit(5000).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).display_user_balance()

print(guido.account_balance) #220
print(jaden.account_balance) #2100