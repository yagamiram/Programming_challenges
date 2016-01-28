# link : http://www.codeskulptor.org/#user41_HH1o4W9umS_0.py
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
        elif start_records[idx][0] <= end_records[idy][0]:
            # append start records to linear-list
            start_records[idx][0] = start_records[idx][0]*-1
            linear_list.append(start_records[idx])
            idx += 1
        else:
            # append end records to liner list
            linear_list.append(end_records[idy])
            idy += 1
    return linear_list

def avoid_collision(temp_records, index_list):
    start_records = list()
    end_records = list()
    for idx in range(len(temp_records)):
        each_records = temp_records[idx]
        start_records.append([each_records[2], idx])
    #temp_records.sort(key=lambda x: x[3])
    for idy in range(len(temp_records)):
        each_records = temp_records[idy]
        end_records.append([each_records[3], idy])
    end_records.sort(key = lambda x : x[0])
    rv = merge_records(start_records, end_records)
    print rv
    counter = 1
    count_dict = dict()
    for c in rv:
        r = c[0]
        if r <= 0:
            r = r*-1
            if counter <= 3:
                if count_dict.has_key(r):
                    count_dict[r] += 1
                else:
                    count_dict[r]  = counter
            else:
                counter = 3
                count_dict[r] = 3
                index_list[c[1]] = True
            counter += 1   
        else:
            if count_dict.has_key(r):
                if index_list[c[1]] == True:
                    count_dict[r] = counter
                else:
                    count_dict[r] = counter -1
                    counter -= 1
            else:
                count_dict[r] = counter - 1
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
http://www.codeskulptor.org/#user41_WgRfh5epJZ_1.py

Now second step:

The update list is sorted by 
a. starting time in asc
b. location by asc

Now for each location and starting time if its count is greater than 
3, skip the rest.

cross checked by sorting the newly pdated list by sorting ending time and location
(beacuse at any give time, there shouldn't be more than 3 content in each location)
'''
import user41_9z0F0owFdi_2 as test_case

'''
Generate the string
'''
string_list = list()
for idx in range(1,10):
    string = "C" + str("%03d" % idx)
    string_list.append(string)
#location_ids = ['right-top','right-bottom','left-top','left-bottom','center-top','center-bottom']
location_ids = ['right-top','right-bottom']
t = test_case.TestCase(string_list, location_ids, 0, 10, 0, 15, 10)
final_list = t.generate_test_case(15)

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
temp_records.sort(key=lambda x: (x[1],x[2],x[3]))
print "sort by starting and ending time"
for l in temp_records:
    print l
temp_list = list()
first_record  = temp_records[0]
location = first_record[1]
content = first_record[0]
temp_list.append(first_record)
print "First record"
print first_record
larger_index = list()
for each_record in temp_records[1:]:
    print each_record
    current_location = each_record[1]
    if location == current_location:
        temp_list.append(each_record)
    else:
        location = each_record[1]
        content = each_record[0]
        #print "temp_list", temp_list
        index_list = [False] * len(temp_list)
        rv = avoid_collision(temp_list, index_list)
        larger_index += index_list
        print "rv", rv
        temp_list = list()
        temp_list.append(each_record)
index_list = [False] * len(temp_list)
rv = avoid_collision(temp_list, index_list)
larger_index += index_list
print "rv", rv
print "larger_index", larger_index
