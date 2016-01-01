# Exercise 7.32: Vec.py

from scitools.std import *

class Vec:
    def __init__(self, *args):
        if len(args) == 1:
            v = asarray(args)
            self.v = v 
        else:
            v = array(args)
            self.v = v
    
    def __add__(self, other):
        return Vec(self.v + other.v)
    
    def __sub__(self, other):
        return Vec(self.v - other.v)
    
    def __mul__(self, other):
        return Vec(self.v*other.v)
    
    def __eq__(self, other):
        return float_eq(self.v, other.v)
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return '%s' % self.v

        


a = array([1, -1, 4], float)
v1 = Vec(a)
v2 = Vec([1, -1, 4])
v3 = Vec((5.2, -8.2))
v4 = Vec(3.9, 8.1)
print v2 + v1, '\n', v3 + v4, '\n', 30*'-'
print v1 - v2, '\n', v4 - v3, '\n', 30*'-'
print v1*v2, '\n', v4*v3, '\n', 30*'-'
print v1 == v2, '\n', v4 == v3, '\n', 30*'-'
print v1 != v2, '\n', v4 != v3, '\n', 30*'-'

