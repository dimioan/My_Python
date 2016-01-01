# Exercise 7.19: VelocityProfile_deriv.py

class Derivative:
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

class Velocity:
    def __init__(self, r):
        self.r = r
    def __call__(self, n):
        r = self.r
        n = float(n)
        c = 50                 # c = b/m0                  
        R = r/0.5              # r/R = 0.5
        v = ((0.5*c)**(1/n))*(n/(n+1))*(R**(1+1/n) - r**(1+1/n))
        return v

f = Velocity(1)           # generate instance with given attribute r = 0.8
df = Derivative(f)          # generate instance with given attribute f
print df(0.5)               # compute derivative with given n = 0.9

# NEXT STEPS
# generate function of exact derivative
# evaluate exact derivative
# compute error = exact - df(0.9)
