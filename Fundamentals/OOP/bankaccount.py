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
        print("Interest Rate: " + str(self.int_rate))
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(account)


monty = BankAccount(0.05, 100)
jaden = BankAccount(0.03, 0)

monty.deposit(100).deposit(50).deposit(100).withdraw(100).yield_interest().display_account_info()
jaden.deposit(1000).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

BankAccount.display_all_accounts()
