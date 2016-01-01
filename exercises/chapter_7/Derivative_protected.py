# Exercise 7.17: Derivative_protected.py

class Derivative_p:
    def __init__(self, f, h):
        self._f = f
        self._h = float(h)
    def __call__(self, x):
        f, h = self._f, self._h
        return (f(x+h) - f(x))/h
    def get_precision(self):
        return self._h
    def set_precision(self, h):
        self._h = float(h)
        return self._h

def f(x):
    from math import log
    return log(x)


# generat a list with k-values
klist = [1]
i = klist[0]
for el in xrange(11):
    i += 4
    klist.append(i)

# loop for computin and printing the table
print ' k            dg            exact          error'
for k in klist:
    dg = Derivative_p(f, 2**(-k))
    dg(1)
    exact = 1
    print '%2g    %.15f     %.2f     %.15f' % (k, dg(1), exact, exact-dg(1))