# Exercise 7.28: Polynomial_dict1.py

class Polynomial:
    def __init__(self, coefficients):
        self.coeff = coefficients

    def __call__(self, x):
        """Evaluate the polynomial."""
        s = 0
        for power in self.coeff:
            s += self.coeff[power]*x**power
        return s

    def __add__(self, other):
        # Start with the longest list and add in the other
        if len(self.coeff) > len(other.coeff):
            result = self.coeff.copy()     # copy of the dict
            for key in other.coeff.keys():
                if key not in result.keys():
                    result[key] = other.coeff[key]
                else:
                    v = result[key] + other.coeff[key]
                    result[key] = v
                    if result[key] == 0:
                        del result[key]
                    print result
        else:
            result = other.coeff.copy() # copy of the dict
            #print result
            for key in self.coeff.keys():
                if key not in result.keys():
                    result[key] = self.coeff[key]
                else:
                    v = result[key] + self.coeff[key]
                    result[key] = v
                    if result[key] == 0:
                        del result[key]
            print result
        return Polynomial(result)



# code snippet for testing
d2 = {1: 1, 100: -3}
d1 = {1: -1, 20: 1, 100: 4}
d3 = {1: 1, 100: -3}


p1 = Polynomial(d1)
p2 = Polynomial(d2)
p3 = Polynomial(d3)
p = p1+p2
print p(0.8)

