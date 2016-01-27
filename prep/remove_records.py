# link: http://www.codeskulptor.org/#user41_SX2EPRxekJ_4.py
def merge_records(start_records, end_records):
    print start_records, end_records
    idx = 0
    idy = 0
    start_len = len(start_records)
    end_len = len(end_records)
    linear_list = list()
    while idx <= start_len-1 or idy <= end_len-1:
        if idx == start_len:
            # no more start records
            linear_list.append(end_records[idy])
            idy += 1
        elif start_records[idx] <= end_records[idy]:
            # append start records to linear-list
            linear_list.append(start_records[idx]*-1)
            idx += 1
        else:
            # append end records to liner list
            linear_list.append(end_records[idy])
            idy += 1
    return linear_list

def avoid_collision(temp_records):
    start_records = list()
    end_records = list()
    for each_records in temp_records:
        start_records.append(each_records[2])
    temp_records.sort(key=lambda x: x[3])
    for each_records in temp_records:
        end_records.append(each_records[3])
    rv = merge_records(start_records, end_records)
    print rv
    counter = 0
    count_dict = dict()
    for r in rv:
        if r <= 0:
            r = r*-1
            counter += 1
            if count_dict.has_key(r):
                count_dict[r] += 1
            else:
                count_dict[r]  = counter
        else:
            if r not in count_dict:
                count_dict[r] = counter
            counter -= 1
    return count_dict
'''
Approach of this Task 1

Two things to be taken care of:
1. Remove the content if it is more than 3 
in each location at a given point of time
2. Do not have duplicates of content in the given starting and ending time


Now this is implemented:
I did it in reverse way. 

First step:

I removed the duplicates content that falls in
between the start and end time range in the same location.
This is done by sorting the given test cases by 
a. content in asc
b. location in asc
c. starting time in asc
d. ending time in desc

Like in the sql sort by content, location, starting time, desc(ending time)

After that I removed the content that clashes each other


Now second step:

The update list is sorted by 
a. starting time in asc
b. location by asc

Now for each location and starting time if its count is greater than 
3, skip the rest.

cross checked by sorting the newly pdated list by sorting ending time and location
(beacuse at any give time, there shouldn't be more than 3 content in each location)
'''
import user41_9z0F0owFdi_0 as test_case

'''
Generate the string
'''
string_list = list()
for idx in range(1,5):
    string = "C" + str("%03d" % idx)
    string_list.append(string)
#location_ids = ['right-top','right-bottom','left-top','left-bottom','center-top','center-bottom']
location_ids = ['right-top','right-bottom']
t = test_case.TestCase(string_list, location_ids, 0, 10, 0, 15)
final_list = t.generate_test_case(25)

'''
Avoid duplicate collisions
How ?
Sort the input file in
a. location based 
b. content based
c. starting time in asc
d. ending time in asc
'''
final_list.sort(key=lambda x: (x[1],x[0],x[2],x[3]))
for l in final_list:
    print l
'''
Now to remove the duplicate collision,
Apply the principle:
Write down the starting time and ending time
in linear order and find the collision and remove one
of it.
'''
first_record = final_list[0]
current_location = first_record[1]
current_content = first_record[0]
cur_stime = first_record[2]
cur_etime = first_record[3]
temp_records = list()
temp_records.append(first_record)
for each_record in final_list[1:]:
    if current_location != each_record[1]:
        current_location = each_record[1]
        current_content = each_record[0]
        cur_stime = each_record[2]
        cur_etime = each_record[3]
        temp_records.append(each_record)
    else:
        # same location
        # check if same content
        if current_content != each_record[0]:
            cur_stime = each_record[2]
            cur_etime = each_record[3]
            current_content = each_record[0]
            temp_records.append(each_record)
        else:
            # same content
            if cur_stime < each_record[2] > cur_etime:
                # no collision
                temp_records.append(each_record)
                cur_stime = each_record[2]
                cur_etime = each_record[3]
                
print "after removing duplicate collisions"
for l in temp_records:
    print l
'''
Now remove if there are more 
than 3 contents in a location at a given 
time
'''
active_counter = 0
elapsed_completion_time = 0
recently_completed_intervals = list()
temp_records.sort(key = lambda x: (x[1], x[3]))
print "BEFORE"
for l in temp_records:
    print l
first_record = temp_records[0]
current_stime = first_record[2]
current_location = first_record[1]
current_etime = first_record[3]
recently_elapsed_interval = list()
recently_elapsed_interval.append((current_stime,current_etime))
noc_records = list()
noc_records.append(first_record)
active_counter = 1
for each_record in temp_records[1:]:
    starting_time = each_record[2]
    ending_time = each_record[3]
    location = each_record[1]
    if location == current_location:
        # Check if its overlap or not
        '''
        This condition is to check overlapping cases
        1. Starting_time <= current_stime
        ex: (1,2) (3,7) (2,9)
        2. Current_stime <= starting_time<= current_etime
        ex: (1,4) (2,5)
        '''
        if starting_time <= current_stime or current_stime <= starting_time  <= current_etime:
            print "Overlaps", (starting_time, ending_time)
            if active_counter < 3:
                print "adding it"
                active_counter += 1
                noc_records.append(each_record)
                recently_elapsed_interval.append((starting_time, ending_time))
        else:
            print "Not overlapping"
            # Now you have to check which interval's ending time 
            # overlaps with this new interval
            temp_list = list()
            idx = 0
            flag = False
            print recently_elapsed_interval
            while idx <= len(recently_elapsed_interval)-1:
                if flag == True:
                    temp_list.append(recently_elapsed_interval[idx])
                else:
                    if starting_time <= recently_elapsed_interval[idx][1]:
                        flag = True
                        temp_list.append(recently_elapsed_interval[idx])
                        elapsed_completion_time = recently_elapsed_interval[idx]
                        current_stime = recently_elapsed_interval[idx][0]
                        current_etime = recently_elapsed_interval[idx][1]
                idx += 1
            recently_elapsed_interval = temp_list[:]
            if len(recently_elapsed_interval) == 0:
                elapsed_completion_time = each_record[3]
                current_stime =  each_record[2]
                current_etime  = each_record[3]
            recently_elapsed_interval.append((each_record[2], each_record[3]))
            noc_records.append(each_record)
            active_counter = len(recently_elapsed_interval)
            print "recently elapsed interval", recently_elapsed_interval
    else:
        active_counter = 0
        current_stime = each_record[2]
        current_etime = each_record[3]
        recently_elapsed_interval = list()
        recently_elapsed_interval.append((current_stime, current_etime))
        noc_records.append(each_record)
        active_counter = 1
        elapsed_completion_time = current_etime
        current_location = each_record[1]
print "After removing more than 3 records"
for l in noc_records:
    print l
