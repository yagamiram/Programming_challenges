'''
Question:
Find all distinct pairs of the numbers that sums to the value K
[0,0,0,0,1,4,46,1,5,9,9,9,4,5,4,5,6,3,9], 9
output: set([(0, 9), (4, 5), (3, 6)])
'''
def NumberofPairs(A, K):
    if len(A) == 0:
        return []
    else:
        A.sort()
        idx  = 0
        idy = len(A)-1
        final_list = set()
        while idx < idy:
            value = A[idx] + A[idy]
            if value == K:
                # match found
                final_list.add((A[idx], A[idy]))
                idx_value = A[idx]
                idy_value = A[idy]
                # Fast forward the pointers
                idx +=1
                idy -= 1
                while A[idx] == idx_value or A[idy] == idy_value:
                    if A[idx] == idx_value:
                        idx += 1
                    if A[idy] == idy_value:
                        idy -= 1
            elif value < K:
                # increase the left pointer
                idx += 1
            else:
                # decrement the right poiner
                idy -= 1
        return final_list
print NumberofPairs([0,0,0,0,1,4,46,1,5,9,9,9,4,5,4,5,6,3,9], 9)
