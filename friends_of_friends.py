'''
Find the number of connected components in the graph
A question asked in the tricky way
Applied BFS algorithm
How BFS works ?
BFS blossoms - i.e goes level by level
So keep a frontier list which cover all the neighbours that are connected to the start node by some way
This helps to build the connected components list

Steps:
Given : Adjacency matrix
A while loop that runs through all nodes in the adjacency matrix:
    Check if the node is already visited or not by looking at the dict - level:
        if not then add it as visited or in level dict as "0" (0th level)
        then add it to the frontier
        while frontier is not empty:
            next = list()
            pick element one by one
            for neigh in each eleme:
                if neigh not in level:
                    add it to the level as level+1
                    add it to the list next - which keeps track of element in the next level
            frontier  = next
In between this, include the connected components condition as per the problem instruction.
'''
def friendCircles(friends):
    if len(friends) == 0:
        return 0
    else:
        # This is nothing but finding the 
        # number of connected components
        # in the given adjacency matrix
        # Apply BFS to find the number of connected components
        # Let the first node by the start node
        nodes = len(friends)
        level = dict()
        frontier = list()
        final_cc = list()
        idx = 0
        while idx <= len(friends)-1:
            if idx not in level:
                frontier.append(idx)
                i = 0
                level[idx] = i
                cc = set()
                while len(frontier) != 0:
                    next = list()
                    for u in frontier:
                        cc.add(u)
                        idy = 0
                        while idy <= len(friends[u])-1:
                            en = friends[u][idy]
                            if idy != u and en != "N" and idy not in level:
                                level[idy] = i+1
                                next.append(idy)
                                cc.add(idy)
                            idy += 1
                    frontier = next
                    i += 1
                final_cc.append(cc)
            idx += 1
        print final_cc
friends = [['Y','Y','Y','N'],['N','Y','N','Y'],['N','N','Y','N'],['N','N','N','Y']]
print friendCircles(friends)
