# Exercise 7.1: F.py

class F:
    def __init__(self, a, w):
        self.a, self.w = a, w
    
    def value(self, x):
        a, w = self.a, self.w
        r = (exp(-a*x))*sin(w*x)
        return r


# code snippet to test the above class

from math import *
f = F(a=1.0, w=0.1)
print f.value(x=pi)

f.a = 2
print f.value(pi)
