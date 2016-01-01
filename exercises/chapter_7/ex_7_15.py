# Exercise 7.15: ex_7_15.py

from math import *

class Backward:
    def __init__(self, f, h=e-9):  # bug1: h=e-9 should be h=1e-9 because the constant e=2.718281..
        self.f, self.h = f, h
    def __call__(self, x):
        h, f = self.h, self.f
        return (f(x) - f(x-h))/h

dsin = Backward(sin)
e = dsin(0) - cos(0)
print 'error: ', e

dexp = Backward(exp, h=1e-7)   # bug2: h = e-7 should be h=1e-7
e = dexp(0) - exp(0)
print 'error: ',e

# it should be noted that e variables that represent the errors should use
# different names because firstly the e name is used by a global variable and 
# secondly the use of the same variable name to represent the errors can end to 
# side effects or erros of value assignment

