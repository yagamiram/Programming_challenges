'''
Question: Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
 NOTE : If there are multiple answers possible, return the one thats lexicographically smallest. 
 
 Approach:
 
 Sort the list
 Now iterate over the list
 Two cases to form wave sort. The cases has to come altenatively
 Case 1:
 idx+1 idx idx+3
 Case 2:
 idx idx+3 idx+2
 
 First case1 then case2 then case1 so on ......
 
 Add check conditions for idx+1, idx+2, idx+3
'''
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        if len(A) == 0:
            return A
        else:
            # the list has numbers more than 2
            final_list = list()
            nums = A
            nums.sort()
            num_len = len(nums)-1
            # case 1 True
            # case 2 False
            case_flag = True
            # two cases totally
            idx = 0
            while idx <= num_len:
                # Get idx+2 and idx+3
                if case_flag ==True:
                    if idx+3 <= num_len:
                        # Add idx+1 first, idx in middle idx+3 third
                        final_list += [nums[idx+1], nums[idx], nums[idx+3]]
                        case_flag = False
                        idx += 2
                    else:
                        # no idx+3 so u have to manage with idx+1 and idx+2
                        if idx+2 <= num_len:
                            final_list += [nums[idx+1], nums[idx], nums[idx+2]]
                            return final_list
                        if idx+1 <= num_len:
                            # no idx+2 so manage with idx+2
                            final_list += [nums[idx+1], nums[idx]]
                            return final_list
                        # no idx+1 so add idx alone
                        final_list += [nums[idx]]
                        return final_list
                else:
                    # case flag is False which means we are in case
                    if idx+3 <= num_len:
                        # add in the order : idx idx+3 and idx+2
                        final_list += [nums[idx] , nums[idx+3], nums[idx+2]]
                        idx += 4
                        case_flag = True
                    else:
                        # no idx+3 so manage with idx+2
                        if idx+2 <= num_len:   
                            final_list += [nums[idx], nums[idx+2]]
                            return final_list
                        # no idx+2 so add jus idx
                        final_list += [nums[idx]]
                        return final_list
                #print final_list, idx
            return final_list
                
                    
            
