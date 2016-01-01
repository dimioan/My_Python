# Exercise 7.4: geometric_shapes.py

class Rectangle:
    def __init__(self, width, height, lower_left_corner_coordinates = None):
        self.w, self.h = width, height
        self.corner = lower_left_corner_coordinates
    
    def area(self):
        a = self.w*self.h
        return a
    
    def circumference(self):
        c = 2*(self.w + self.h)
        return c 


class Triangle:
    def __init__(self, v0, v1, v2):
        self.v0, self.v1, self.v2 = v0, v1, v2
    
    #def area(self):
     #   x0,y0,x1,y1,x2,y2 = self.x0, self.y0, self.x1, self.y1, self.x2, self.y2
      #  a = 0.5*abs(x1*y2 - x2*y1 - x0*y2 + x2*y0 + x0*y1 -x1*y0)
       # return a 
    
    def area_tuple(self):
        v0, v1, v2 = self.v0, self.v1, self.v2
        a = 0.5*abs(v1[0]*v2[1] - v2[0]*v1[1] - v0[0]*v2[1] + v2[0]*v0[1] + v0[0]*v1[1] - v1[0]*v0[1])
        return a 
    
    def circumference_tuple(self):
        from math import *
        v0, v1, v2 = self.v0, self.v1, self.v2
        c = sqrt(((v1[0] - v0[0])**2) + (v1[1] - v0[1])**2) + \
        sqrt(((v2[0] - v1[0])**2) + (v2[1] - v1[1])**2) +\
         sqrt(((v2[0] - v0[0])**2) + (v2[1] - v0[1])**2) 
        return c 

    
      
test_R = Rectangle(8.6, 3.7)
print 'RECTANGLE:\narea = %g\ncircumference = %g\n' %(test_R.area(), test_R.circumference())

test_T = Triangle((18, 11), (46, 17), (29, 31.1))
print 'TRIANGLE:\narea = %g\ncircumference = %g' %(test_T.area_tuple(), test_T.circumference_tuple())


#test_T = Triangle(18, 11, 46, 17, 29, 31.1)
#print 'area = %g\n' %(test_T.area())
