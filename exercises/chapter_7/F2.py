# Exercise 7.11: F2.py

class F2:
    def __init__(self, a, w):
        self.a, self.w = a, w
    
    def __call__(self, x):
        a, w = self.a, self.w
        r = (exp(-a*x))*sin(w*x)
        return r
    
    def __str__(self):
        return 'exp(-a*x)*sin(w*x); a = %g, w = %g' %(self.a, self.w)



# code snippet for testing
from math import *
f = F2(1.0, 0.1)
print f(pi)
f.a = 2
print f(pi)
print f
