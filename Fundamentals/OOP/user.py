class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
    	# the specific user's account increases by the amount of the value received
    	self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(self.account_balance)
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jaden = User("Jaden Willeiksen", "email@email.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(20)
print(guido.account_balance) #320

monty.make_deposit(700)
monty.make_deposit(50)
monty.make_withdrawal(50)
print(monty.account_balance) #700

jaden.make_deposit(5000)
jaden.make_withdrawal(1000)
jaden.make_withdrawal(1000)
jaden.make_withdrawal(1000)
print(jaden.account_balance) #2000

guido.transfer_money(jaden, 100)
print(guido.account_balance) #220
print(jaden.account_balance) #2100