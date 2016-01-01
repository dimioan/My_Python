# Exercise 7.24: Polynomial_error.py


class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients
    
    def __call__(self, x):
        return sum([c*x**i for i, c in enumerate(self.coeff)])
    
    def __add__(self, other):
        #maxlength = max(len(self), len(other))  # here is the error in the initial code
        maxlength = max(len(self.coeff), len(other.coeff)) # and thi is the solution
        self.coeff += [0]*(maxlength - len(self.coeff))
        other.coeff += [0]*(maxlength - len(other.coeff))
        result_coeff = self.coeff
        for i in range(maxlength):
            result_coeff[i] += other.coeff[i]
        return Polynomial(result_coeff)

p1 = Polynomial([1,2,6,8])
p2 = Polynomial([3,8])
addition = p1 + p2
print addition(8.3)

        