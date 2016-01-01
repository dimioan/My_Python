# Exercise 7.30: Vec2D_lists.py


class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        if isinstance(other, (tuple, list)):
            other = Vec2D(other[0], other[1])
        elif not (hasattr(other, 'x') and \
                  hasattr(other, 'y')):
            raise TypeError('other must have x and y attr.')
        return Vec2D(self.x + other.x, self.y + other.y)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (tuple, list)):
            other = Vec2D(other[0], other[1])
        elif not (hasattr(other, 'x') and \
                  hasattr(other, 'y')):
            raise TypeError('other must have x and y attr.')
        return Vec2D(self.x - other.x, self.y - other.y)
    
    def __rsub__(self, other):
        if isinstance(other, (tuple, list)):
            other = Vec2D(other[0], other[1])
        elif not (hasattr(other, 'x') and \
                  hasattr(other, 'y')):
            raise TypeError('other must have x and y attr.')
        return other.__sub__(self)
    
    def __str__(self):
        return '(%g, %g)' %(self.x, self.y)


a = Vec2D(5, 5)
b = Vec2D(3, 2)
print a+b
print a + (1.1, 2.2)
print [3.1, 4.] + b 
print 30*'-'
print a - b
print a - [34, 65.3]
print [3.2, 1.4] - b
print 2 - a
#d = a - 7
print c
