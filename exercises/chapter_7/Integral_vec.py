# Exercise 7.21: Integral_vec.py

class Integral_scalar:
    def __init__(self, f, a, n):
        self.f, self.a, self.n = f, a, n
    def __call__(self, x):
        from scitools.std import iseq
        f, a, n = self.f, self.a, self.n
        h = (x-a)/float(n)
        I = 0.5*f(a)
        for i in iseq(1, n-1):
            I += f(a + i*h)
        I += 0.5*f(x)
        I *= h
        return I


class Integral_vec_builtin:
    def __init__(self, f, a, n):
        self.f, self.a, self.n = f, a, n
    def __call__(self, x):
        from scitools.std import iseq
        f, a, n = self.f, self.a, self.n
        h = (x-a)/float(n)
        I = 0.5*f(a)
        l = []
        for i in iseq(1, n-1):
            I = f(a + i*h)
            l.append(I)
        I = sum(l)
        I += 0.5*f(x)
        I *= h
        return I
    
    
class Integral_vec_numpy:
    def __init__(self, f, a, n):
        self.f, self.a, self.n = f, a, n
    def __call__(self, x):
        from scitools.std import linspace, sum, zeros,iseq
        f, a, n = self.f, self.a, self.n
        h = (x-a)/float(n)
        I = 0.5*f(a)
        ar = zeros(len(linspace(1,n-1, n-1)))
        for i in iseq(1, n-1):
            ar[i-1] = f(a + i*h)
        I = sum(ar)
        I += 0.5*f(x)
        I *= h
        return I


from math import sin, pi
import time

start_time1 = time.time()
f = Integral_scalar(sin, 0, 200)
print '\nscalar value:', f(1)
elapsed_time1 = time.time() - start_time1
print 'scalar time: %.10f' % elapsed_time1, '\n'

start_time2 = time.time()
g = Integral_vec_builtin(sin, 0, 200)
print 'buit-in value:', g(1)
elapsed_time2 = time.time() - start_time2
print 'built-in time: %.10f' % elapsed_time2, '\n'

start_time3 = time.time()
w = Integral_vec_numpy(sin, 0, 200)
print 'numpy value:', w(1)
elapsed_time3 = time.time() - start_time3
print 'numpy time: %.10f' % elapsed_time3, '\n'


