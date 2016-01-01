# Exercise 7.12: Spring_nonlinear.py

class Integral:
    def __init__(self, f, a, n):
        self.f, self.a, self.n = f, a, n
    
    def __call__(self, x):
        from scitools.std import iseq
        #from scitools.StringFunction import StringFunction
        f, a, n = self.f, self.a, self.n 
        #f = StringFunction(f)
        h = (x-a)/float(n)
        I = 0.5*f(a)
        for i in iseq(1, n-1):
            I += f(a + i*h)
        I += 0.5*f(x)
        I *= h
        return I
        

class Spring2:
    def __init__(self, f, x):
        self.f, self.x = f, x
    def force(self):
        
        f, x = self.f, self.x
        return f(x)
    def energy(self):
        #from math import *
        f, x = self.f, self.x
        m = Integral(f, a=0, n=200)
        return m(x)

class W:
    def __init__(self, k):
        self.k = k
    def __call__(self, x):
        return self.k*x


class G:
    def __init__(self, a):
        self.a = a
    def __call__(self, x):
        #from math import *
        a = self.a
        return a*(sin(x))


# LINEAR SPRING
#w = W(157.3)            # k-value given 
#l = Spring2(w, 0.5)     # x-value given 
#print l.force()
#print l.energy()

# NON LINEAR SPRING
from math import *
g = G(300.2)             # a-value given
nl = Spring2(g, 0.5)     # x-value given
print nl.force()
print nl.energy()

