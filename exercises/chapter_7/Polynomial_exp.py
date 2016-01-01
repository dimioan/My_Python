# Exercise 7.23: Polynomial_exp.py

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
            #print s
        return s

    def __add__(self, other):
        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result_coeff = self.coeff[:]  # copy!
            for i in range(len(other.coeff)):
                result_coeff[i] += other.coeff[i]
        else:
            result_coeff = other.coeff[:] # copy!
            for i in range(len(self.coeff)):
                result_coeff[i] += self.coeff[i]
        return Polynomial(result_coeff)


def coeff(N):
    from math import factorial
    clist = []
    for i in range(N+1):
        c = 1.0/factorial(i)
        clist.append(c)
    return clist



import sys
from math import *

x = float(sys.argv[1])
Nlist = sys.argv[2:]

for el in Nlist:
    N = int(el)
    coefficient_list = coeff(N)
    p = Polynomial(coefficient_list)
    print 'for N= %2.d ---------> p(%.2f) = %f' % (N, x, p(x))
print 'The exact value is exp(%.2f) = %f' % (x,exp(x)) 


        
        
