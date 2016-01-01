# Exercise 7.31: Vec3D.py


class Vec3D:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    
    def __add__(self, other):
        if isinstance(other, (float, int)):
            other = Vec3D(other, other, other)
        elif not (hasattr(other, 'x') and \
                  hasattr(other, 'y') and hasattr(other, 'z')):
            raise TypeError('other must have x, y and z attr.')
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (float, int)):
            other = Vec3D(other, other, other)
        elif not (hasattr(other, 'x') and \
                  hasattr(other, 'y') and hasattr(other, 'z')):
            raise TypeError('other must have x, y and z attr.')
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __rsub__(self, other):
        if isinstance(other, (float, int)):
            other = Vec3D(other, other, other)
        elif not (hasattr(other, 'x') and \
                  hasattr(other, 'y') and hasattr(other, 'z')):
            raise TypeError('other must have x, y and z attr.')
        return other.__sub__(self)
    
    def __mul__(self, other):
        if not isinstance(other, (float, int)):
            raise TypeError('other is a scalar, it should be a float or integer')
        return Vec3D(other*self.x, other*self.y, other*self.z)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __abs__(self):
        from math import sqrt
        if not isinstance(self, Vec3D):
            raise TypeError('other should be a Vec3D object')
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __eq__(self, other):
        from scitools.numpyutils import float_eq
        return float_eq(self.x, other.x) and float_eq(self.y, other.y) \
            and float_eq(self.z, other.z)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __cross__(self, other):
        nx = (self.y*other.z) - (self.z*other.y)
        ny = (self.z*other.x) - (self.x*other.z)
        nz = (self.x*other.y) - (self.y*other.x)
        return Vec3D(nx, ny, nz)
    
    def __str__(self):
        return '(%g, %g, %g)' %(self.x, self.y, self.z)
    



a = Vec3D(5,8,9)
b = Vec3D(2,3,4)
print a + b,'\n', a + 2.5, '\n', 1 + b, '\n', 30*'-'
print a-b,'\n',a-2,'\n', 9.5-b, '\n',30*'-'
print a*2, '\n', 5*b,'\n', 30*'-'
print abs(b),'\n', 30*'-'
print a == b, '\n', b == b,'\n', 30*'-'
print a != b,'\n', b != b,'\n', 30*'-'
print a.__cross__(b),'\n', 30*'-'
