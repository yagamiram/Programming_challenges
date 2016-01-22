'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Apparoach:
XOR

Do XOR of all the elements. It will return the element that occurrs only once.
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        else:
            # More than one element is present in the array
            # Apply XOR function to the given array
            final = 0
            for each_elem in nums:
                final = final ^ each_elem
            return final
