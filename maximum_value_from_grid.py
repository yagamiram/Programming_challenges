'''
Question:
A table composed of N x M cells, each having a certain quantity of apples, is given.
You start from the upper-left corner. At each step you can go down or right one cell.
Find the maximum number of apples you can collect.

Approach: Bottom up DP
A memo is created to store the value calculated at each point.
A for loop to run on the arrays.
The last cell will have maximum value

One easy approach: No need to have memo, modify the existing array itself

Recursive approach:
Recursive approach need memoization and it runs from last cell to the first cell. [which is not needed as per the question]
'''
def maximum_apples(table):
    if len(table) == 0:
        return 0
    else:
        # for each i,j cell, you can reach it from top or left
        # so i-1,j = top and i,j-1 left
        # pick the maximum and go to the next cell.
        rows = len(table)
        col = len(table[0])
        memo = [[None for _ in range(col)] for _ in range(rows)]
        for idx in range(len(table)):
            for idy in range(len(table[0])):
                # idx,idy cell. Top = idx-1, idy and left = idx, idy-1
                top_value = memo[idx-1][idy] if idx-1 >= 0 else 0
                left_value = memo[idx][idy-1] if idy-1 >= 0 else 0
                memo[idx][idy] = max(table[idx][idy]+ top_value , table[idx][idy]+left_value)
        print memo[-1][-1]
table = [[1,2,3,4],[1,1,1,1],[9,9,9,9]]
maximum_apples(table)
