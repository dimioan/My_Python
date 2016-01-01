# Exercise 7.6: Line2.py

class Line2:
    
    def __init__(self, p1, p2):
        #self.p1, self.p2 = p1, p2
        if isinstance(p1, (tuple, list)) and isinstance(p2, (float, int)):
            self.a = p2
            self.b = p1[1] - p2*p1[0]
            #print a,'\n', b
        elif isinstance(p1, (tuple, list)) and isinstance(p2, (tuple, list)):
            self.a = (p2[1] - p1[1])/float(p2[0] - p1[0])
            self.b = p1[1] - self.a*p1[0]
        elif isinstance(p1, (float, int)) and isinstance(p2, (float, int)):
            self.a = p1
            self.b = p2
        #else:
            #s = 'ATTENTION: You must provide one of the three options: \n \
            #a point (x,y coordinates) and the slope\n\
            #two points\n\
            #the slope and a x-coordinate'
            #print s
               
    def value(self, x):
        a, b = self.a, self.b
        y = a*x + b
        return y
            
        # code snippet for testing
#l = Line2((4.3,8), 0.35)         # point and slope
#l = Line2((0.0, -1), (2,4.0))    # two points
l = Line2(0.5, 8.4)              # slope and intersection with the y-axis
#l = Line2(56,(64,55))               # wrong input
print l.value(0.5)
