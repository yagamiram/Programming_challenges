'''
Given a collection of intervals, merge all overlapping intervals.

Approach: 
1. Sort by Start time
2. Process each interval and see if it fall between start time and end time.
3. If yes, update the end time if needed
4. If not, a new non overlapping interval is found.
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals) in [0, 1]:
        return intervals
    else:
        # sort by start time
        intervals = sorted(intervals, key = lambda x : x.start)
        start_time = None
        end_time = None
        non_overlapping_list = list()
        idx = 0
        while idx <= len(intervals)-1:
            current_interval = intervals[idx]
            if start_time == None:
                # new interval
                start_time = current_interval.start
                end_time = current_interval.end
            else:
                # check if this interval overlaps with
                # curent start and end time
                if start_time <= current_interval.start <= end_time:
                    # Yes it overlaps 
                    if current_interval.end > end_time:
                        # update the end time
                        end_time = current_interval.end
                else:
                    # It's not overlapping
                    # so append the start and end time
                    non_overlapping_list.append([start_time, end_time])
                    # update the start time
                    start_time = current_interval.start
                    end_time = current_interval.end
            idx += 1
        non_overlapping_list.append([start_time, end_time])
        return non_overlapping_list
