'''
Task 3
http://www.codeskulptor.org/#user41_1lgZ6rXpvt_1.py
'''
# Get the input from the task2 
'''
The input is of the format
content_id location starting_time ending_time content_score location_score

Another input is of the format
scores Job_ids Duration_ids 
'''
import user41_8yJpv0nZJt_2 as heap
schedule = [[]]

new_jobs = [[]]

new_jobs.sort(key = lambda x = (x[4]))

# pre process the schedule
# Atmost 6 records at a given point of time
# first find the longest running time
longest_running_time = float('-inf')
for l in schedule:
    ending_time = l[3]
    if ending_time > longest_running_time:
        longest_running_time = ending_time
running_jobs = set()
heap_keys = list()
keys = list()
for record in schedule:
    content = record[0]
    running_jobs.add(content)
    end_time = record[3]
    keys.append((longest_running_time - end_time, endtime, record[-1], record[1], record[0]))
# now build the heap
location = heap.BinHeap()
location.buildHeap(keys) # free time, end_time, location, multiplier, job id
# Now build a heap for new jobs
jobs = heap.BinHeap()
jobs.buildHeap(new_jobs) # (score, job_id, duration)

# Now do the actual logic here
final_list = list()
'''
Pick the maximum element from both the location and jobs and see if it fits
'''
next_location = location.delMax()
# If the location is chosen then it means the job is finished cross it

next_job = jobs.delMax()
while next_job == None:
    running_jobs.remove(next_location[-1])
    # check if it fitst
    new_job_time = next_job[-1]
    free_slot_time = next_location[0]
    if next_job[0] not in running_jobs:
        if free_slot_time >= new_job_time:
            # fits
            final_list.append((next_job[0], next_location[1], next_location[2]))
            running_jobs.add(next_job[0])
            # add the record back to location heap
            location.insert(free_slot_time - new_job_time ,new_job_time, next_location[2], next_location[3], next_job[0])
    next_location = location.delMax()
    next_job = jobs.delMax()
print final_list
