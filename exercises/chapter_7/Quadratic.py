# Exercise 7.7: Quadratic.py


class Quadratic:
    def __init__(self, a, b,c):
        self.a, self.b, self.c = a, b, c
    
    def value(self, x):
        a, b, c = self.a, self.b, self.c
        y = a*x**2 + b*x + c
        return y
    
    def table(self, n, interval):
        step = 0
        x = interval[0]
        print 'For %d x-values in the interval [%g, %g]' % (n, interval[0], interval[1])
        print '  x       f(x)'
        for i in range(n):
            x += step
            f = self.value(x)
            step = (interval[1] - interval[0])/(n-1)
            print '%5.3f    %5.3f' % (x, f)
    
    def roots(self):
        from math import sqrt
        a, b, c = self.a, self.b, self.c
        if (b**2) - 4*a*c >= 0:
            r1 = -b + ((sqrt((b**2) - 4*a*c)))/(2*a)
            r2 = -b - ((sqrt((b**2) - 4*a*c)))/(2*a)
            return 'root 1 = %f\nroot 2 = %f' %(r1, r2)
        else:
            print 'Negative Delta' 
            

                  # code snippet for testing
f = Quadratic(3.3, 26.3, 6)
print f.value(76.45)
#f.table(5, (3.3, 7.5))
#print f.roots()