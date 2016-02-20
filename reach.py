'''
Question: You are in an infinite 2D grid where you can move in any of the 8 directions :

 (x,y) to 
    (x+1, y), 
    (x - 1, y), 
    (x, y+1), 
    (x, y-1), 
    (x-1, y-1), 
    (x+1,y+1), 
    (x-1,y+1), 
    (x+1,y-1) 
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example :

Input : [(0, 0), (1, 1), (1, 2)]
Output : 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

Link: https://www.interviewbit.com/courses/programming/topics/arrays/problems/reach/

Approach:
You don't have to use the above cases.
Just find the difference between each points which is the distance from one point to another point.
'''
class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        # iterative approach
        # try out all the cases at each level for a point
        # and stop when the target is reached.
        points = len(X)-1
        idx = 0
        counter = 0
        while idx <= points-1:
            # find the number of steps to reach from source to target points
            x_steps  = abs(X[idx+1] - X[idx])
            y_steps  =  abs(Y[idx+1] - Y[idx])
            if x_steps > y_steps:
                counter += x_steps
            elif x_steps < y_steps:
                counter += y_steps
            else:
                counter += x_steps
            idx += 1
        return counter
