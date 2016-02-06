'''
Find the next closest element for the given target from a sorted array
Approach : Binary search
Stop when the number of elements is 2. compare and return back.
'''
def binary_search(self, indexes, low, high, target):
    if low == high:
        return indexes[low]
    elif low == high+1:
        # 2 elements one must be the answer we are looking for
        if target - indexes[low] < target - indexes[high]:
            return indexes[low]
        else:
            return indexes[high]
    else:
        mid = (low + high)/2
        print "mid is", mid, target - indexes[mid], target - indexes[mid+1]
        if abs(target - indexes[mid]) > abs(target - indexes[mid+1]):
            # go right
            print "go right"
            return self.binary_search(indexes, mid+1, high, target)
        else:
            print "go left"
            # go left
            return self.binary_search(indexes, low, mid, target)
