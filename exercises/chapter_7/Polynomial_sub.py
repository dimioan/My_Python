# Exercise 7.25: Polynomial_sub.py

class Polynomial_sub:
    def __init__(self, coefficients):
        self.coeff = coefficients
    
    def __call__(self, x):
        s = 0
        for i in range(len(self.coeff)):
            s += self.coeff[i]*x**i
        return s
    
    def __sub__(self, other):
        if len(self.coeff) >= len(other.coeff) and \
        self.coeff[-len(other.coeff):] == other.coeff:
            result_coeff = self.coeff[:-len(other.coeff)]
        elif len(self.coeff) <= len(other.coeff) and \
        other.coeff[-len(self.coeff):] == self.coeff:
            print 'The second list is larger than the first! p1 - p2 became p2-p1'
            result_coeff = other.coeff[:-len(self.coeff)]
        else:
            print 'No list to subtract!'
        return Polynomial_sub(result_coeff)

# code snippet for testing
p2 = Polynomial_sub([79,2,3])
p1 = Polynomial_sub([45,783,323,67,79,2,3])
p = p1 - p2
print p(6.9)
            