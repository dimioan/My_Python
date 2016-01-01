x = 1.2
n = 25
k = 1
s = x
sign = 1.

import math
while k<n:
    sign = - sign
    k = k + 2
    term = sign*x**k/math.factorial(k)
    s = s + term
print '------------------------------------------------------\n'
print 'sin(%g) = %g (approximation with %d terms)' % (x, s, n)
print '\n------------------------------------------------------'
