class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = 0 + float(int_rate)
        self.balance = 0 + float(balance)
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Interest Rate: " + str(self.int_rate) + "%")
        print("Balance: $" + str(self.balance))
        #NOT returning self because the object instance ID will be printed, use this method LAST in a chain

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(account)

class User:
    def __init__(self, name, email, AccountNum):
        self.name = name
        self.email = email
        self.accounts = []
        for i in range(AccountNum):
            self.accounts.append(BankAccount(0.02, 0))

    def make_deposit(self, amount, accountid):
        self.accounts[accountid].balance += amount
        return self

    def make_withdrawal(self, amount, accountid):
        self.accounts[accountid].balance -= amount
        return self

    def display_user_balance(self, accountid):
        print("Account " + str(accountid) + ":")
        print(self.accounts[accountid].display_account_info())
        return self
    
    def display_all_balances(self):
        for i in range(len(self.accounts)):
            print("Account " + str(i) + ":")
            print(self.accounts[i].display_account_info())

    def transfer_money(self, other_user, amount, accountid, theiraccountid):
        self.accounts[accountid].balance -= amount
        other_user.accounts[theiraccountid].balance += amount
        return self


monty = User("Monty Python", "monty@python.com", 3)
jaden = User("Jaden Willeiksen", "email@email.com", 6)

print("Monty's Accounts")

monty.make_deposit(100, 0).make_deposit(50, 1).make_deposit(100, 2).make_withdrawal(100, 0).transfer_money(jaden, 50, 2, 0).accounts[1].yield_interest()
monty.display_all_balances()

print("Jaden's Accounts")

jaden.make_deposit(1000, 4).make_deposit(500, 3).make_withdrawal(100, 4).make_withdrawal(100, 3).make_withdrawal(100, 4).make_withdrawal(100, 4).accounts[4].yield_interest()
jaden.display_all_balances()

print("All Account Instances")

BankAccount.display_all_accounts()
