# Exercise 7.5: Line.py

class Line:
    """
    Compute the coefficients a and b in the mathematical expression
    for a straight line y = a*x + b that goes through two point p1 and p2.
    And the y coordinate for a given x coordinate.
    
    p1, p2: tuples that contain the coordinates for the first and second point
    x ; given coordinate 
    
    Example:
    >>> from Line import Line
    >>> line = Line((0,-1), (2,4))
    >>> print line.value(0.5)
    0.25 
    """
    
    
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2
        
    def value(self, x):
        p1, p2 = self.p1, self.p2
        a = (p2[1] - p1[1])/float(p2[0] - p1[0])
        b = p1[1] - a*p1[0]
        y = a*x + b 
        return y 

# test block

line = Line((43,23.3), (-25.4,4.7))
print line.value(567.3232), line.value(0), line.value(1)
