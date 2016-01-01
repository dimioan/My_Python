# Exercise 7.3: Account2.py

class Account:
    def __init__(self, name, account_number, initial_amount, transactions):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = transactions

    def deposit(self, amount):
        self.balance += amount
        self.transactions += 1

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions += 1

    def dump(self):
        s = '%s, %s, balance: %s, transactions number: %s' % \
            (self.name, self.no, self.balance, self.transactions)
        print s


a = Account('Dimitris', '1234455', 100000, 400)
a.deposit(70000)
a.deposit(10000)
a.withdraw(20000)
a.withdraw(50000)
a.deposit(10000)
print a.dump()
