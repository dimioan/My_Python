# Exercise 7.8: Spring.py


class Spring:
    """
    Spring Force is the force exerted by a spring.
    F=kd
    d=displacement or the distance the spring is compressed or pulled/extended(m)
    k=spring constant, which depends on the material and shape of the spring(N/m)
    """
    
    def __init__(self, k):
        self.k = k
    
    def force(self, x):
        k = self.k
        return k*x
    
    def energy(self, x):
        k = self.k
        return 0.5*k*(x**2)




def table(f, a, b, n, heading=''):
    """Write out f(x) for x in [a, b] with steps h=(b-a)/n."""
    print heading
    h = (b-a)/float(n)
    for i in range(n+1):
        x = a + i*h
        print 'function value = %10.4f at x = %g' % (f.energy(x),x) # f.energy(x) or f.force(x)



       #      code snippet for testing
t = Spring(357.45)
#table(t, 0.5, 2, 5, 'Spring Force')    # f.force(x) must be used in the table function
table(t, 0.5, 2, 5, 'Spring Energy')    # f.energy(x) must be used in the table function
