# Exercise 7.14: Central.py

class Central:
    
    def __init__(self, f, h=None):
        self.f, self.h = f, h
    
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/2*h




if __name__ == '__main__':
    def f(x):
        return 0.25*x**4
    
    df = Central(f, h=0.1)
    
    for x in (1, 5, 10):
        df_value = df(x)
        exact = x**3
        print "f'(%d)=%g      (error=%.2E)" % (x, df_value, exact-df_value)
    
    
    def g(x):
        from math import log
        return log(x)
    
    for h in (1,0.5, 0.1, 1e-3, 1e-5, 1e-7, 1e-9, 1e-11):
        dg = Central(g, h)
        dg_value = dg(10.)
        exact = 1/10.0
        print "for h=%.6g: g'(%d)=%5.5g      (error=%g)" % (h,10, dg_value, exact-dg_value)
    

