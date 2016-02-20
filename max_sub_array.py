'''
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment's length and return segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum starting index

Apparoach:
Kadane algorithm will few additions to satisfy all the conditions

Kadane's algorithm:

max_so_far = -1
max_ending_here = 0
for each_num in array:
  max_endgin_here += each_num
  if max_so_far < max_ending_here:
    max_so_far = max_ending_here
  if max_ending_here < 0:
    max_ending_here = 0
    

'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        if len(A) == 0:
            return 0
        # Use kadanage algorithm
        max_so_far = -1
        max_list = list()
        max_list_index = -1
        array_list = list()
        array_list_index = -1
        max_ending_here = 0
        for idx in xrange(len(A)):
            each_num = A[idx]
            if each_num < 0:
                max_ending_here = 0
                array_list_index = -1
                array_list = list()
                continue
            max_ending_here += each_num
            if len(array_list) == 0:
                array_list_index = idx
            array_list.append(each_num)
            if max_so_far < max_ending_here:
                max_so_far  = max_ending_here
                max_list = array_list[:]
                max_list_index = array_list_index
            elif max_so_far == max_ending_here:
                if len(max_list) < len(array_list):
                    max_list = array_list[:]
                    max_list_index = array_list_index
                elif len(max_list) == len(array_list) and max_list_index > array_list_index:
                    max_list = array_list[:]
                    max_list_index = array_list_index
            if max_ending_here < 0:
                max_ending_here = 0
                array_list = list()
                negative_flag = False
        return max_list
