'''
Question : 
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

Make sure the returned intervals are also sorted.

Approach : On the fly include the interval
O(N) or slighly bigger than O(N) because i'm doing slicing [unncessatliy because of laziness] 

Lots of inline comments are given 
easy to understand even if the inline comments are not in readable format.

https://www.interviewbit.com/courses/programming/topics/arrays/problems/interval/
'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        if len(intervals) == 0:
            return [new_interval]
        else:
            idx = 0
            final_list = list()
            while idx <= len(intervals)-1:
                current = intervals[idx]
                #print current
                '''
                Check if the start interval is before or in middle or after 
                the current interval
                '''
                if new_interval.start < current.start:
                    # the interval is before the current interval
                    '''
                    Now check if the interval's end time is before , on , or after current interval
                    '''
                    if new_interval.end < current.start:
                        # the new interval occurs before the current interval
                        # no collision
                        final_list.append(new_interval)
                        final_list += intervals[idx:]
                        return final_list
                    elif new_interval.end == current.start:
                        # the new interval's end time collides with the current i
                        # interval's start time
                        final_list.append(Interval(new_interval.start, new_interval.end))
                        final_list += intervals[idx+1:]
                        return final_list
                    elif current.start < new_interval.end < current.end:
                        # collides but smaller than the current end time
                        final_list.append(Interval(new_interval.start, current.end))
                        final_list += intervals[idx+1:]
                        return final_list                                 
                    elif new_interval.end == current.end:
                        final_list.append(Interval(new_interval.start, current.end))
                        final_list += intervals[idx+1:]
                        return final_list                                  
                    else:
                        # the end time is going beyond the current interval
                        # so skip the interval
                        pass
                elif current.start <= new_interval.start <= current.end:
                    # the interval collides with the current interval
                    if current.start == new_interval.start:
                        if current.start < new_interval.end < current.end:
                            # collides but smaller than the current end time
                            final_list.append(Interval(new_interval.start, current.end))
                            final_list += intervals[idx+1:]
                            return final_list
                        elif new_interval.end == current.end:
                            final_list.append(Interval(new_interval.start, current.end))
                            final_list += intervals[idx+1:]
                            return final_list                                 
                        else:
                            # the end time is going beyond the current interval
                            # so skip the interval
                            pass
                    else:
                        # the new interval is greater than the current interval
                        #print "the new interval is greater than the current interval"
                        if current.start < new_interval.end < current.end:
                            # collides but smaller than the current end time
                            final_list.append(Interval(curent.start, current.end))
                            final_list += intervals[idx+1:]
                            return final_list
                        elif new_interval.end == current.end:
                            final_list.append(Interval(current.start, current.end))
                            final_list += intervals[idx+1:]
                            return final_list                                 
                        else:
                            # the end time is going beyond the current interval
                            # so skip the interval
                            #print "skip the interval"
                            new_interval.start = current.start
                            pass
                else:
                    # the interval occurs after the current interval
                    final_list.append(current)
                idx += 1
            final_list.append(new_interval)
            return final_list
