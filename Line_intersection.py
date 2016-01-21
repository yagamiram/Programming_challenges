#!/usr/bin/python
'''
Notes:
The solution involves determining if three points are listed in a counterclockwise order. 
So say you have three points A, B and C. 
If the slope of the line AB is less than the slope of the line AC then the three points are listed in a counterclockwise order.

This is equivalent to:

def ccw(A,B,C):
    return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)
You might be wondering how does this help? Think of two line segments AB, and CD. 
These intersect if and only if points A and B are separated by segment CD and points C and D are separated by segment AB. 
If points A and B are separated by segment CD then ACD and BCD 
should have opposite orientation meaning either ACD or BCD is counterclockwise but not both. 
Therefore calculating if two line segments AB and CD intersect is as follows:

def intersect(A,B,C,D):
        return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
        
Links for computational geometry;
http://www.toptal.com/python/computational-geometry-in-python-from-theory-to-implementation
http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
http://debian.fmi.uni-sofia.bg/~sergei/cgsr/docs/clockwise.htm
http://stackoverflow.com/questions/1165647/how-to-determine-if-a-list-of-polygon-points-are-in-clockwise-order
http://blancosilva.github.io/post/2014/10/28/Computational-Geometry-in-Python.html
'''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def ccw(A,B,C):
    return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def ccw2(A,B,C):
    value = (B.x - A.x)*(B.y + A.y) + (C.x - B.x)*(C.y + B.y) + (A.x - C.x) * (A.y + C.y)
    if value > 0:
        return True
    else:
        return False

def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


'''a = Point(3.4,2.8)
b = Point(5.4, 8.2)
c = Point(2.3,8.1)
d = Point(8.3,0.9)'''

a = Point(0,0)
b = Point(0,1)
c = Point(1,1)
d = Point(1,0)

#print ccw2(a,b,c)

print intersect(a,b,c,d)
print intersect(a,c,b,d)
print intersect(a,d,c,d)
