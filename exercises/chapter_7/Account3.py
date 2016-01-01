# Exercise 7.13: Account3.py

class Account3:
    def __init__(self, name, account_number,amount):
        self.name = name
        self.no = account_number
        self.balance = amount

    def __iadd__(self, other):
        self.balance += other.balance
        return self
    
    def __isub__(self, other):
        self.balance -= other.balance
        return self

    def __str__(self):
        s = '%s, %s, balance: %s' % \
            (self.name, self.no, self.balance)
        return s
    
    def __repr__(self):
        s = '%s, %s, balance: %s' % \
        (self.name, self.no, self.balance)
        return s 


# code snippet for testing

a = Account3('Jim', '79978985448', 100000)
b = Account3('Jim', '79978985448', 30000)
c = Account3('Jim', '79978985448', 70000)
a+=b                       # 100000 + 30000 = 130000
a-=c                       # 130000 - 70000 = 60000
print a
