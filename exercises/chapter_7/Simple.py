# Exercise 7.2: Simple.py

class Simple:
    def __init__(self, i):
        self.i = i
    
    def double(self):
        i = self.i
        r = i + i 
        return r


# code snippet for testing the above class

s1 = Simple(4)
for i in range(4):
    s1.double()
print s1.i


s2 = Simple('Hello')
s2.double(); s2.double()
print s2.i
s2.i = 100
print s2.i


