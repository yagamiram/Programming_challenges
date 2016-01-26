'''
link: http://www.codeskulptor.org/#user41_SX2EPRxekJ_0.py
'''
def merge_records(start_records, end_records):
    #print start_records, end_records
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
    #print rv
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
final_list = t.generate_test_case(50)

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
print "Given list"
for l in final_list:
    print l
print "=================================="
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
                
'''
Now remove if there are more 
than 3 contents in a location at a given 
time
'''
temp_records.sort(key=lambda x:(x[1],x[2],x[3]))

first_record = temp_records[0]
current_location = first_record[1]
current_content = first_record[0]
cur_stime = first_record[2]
cur_etime = first_record[3]
noc_records = list()
noc_records.append(first_record)
task_list = list()

for each_record in temp_records[1:]:
    if current_location != each_record[1]:
        current_location = each_record[1]
        current_content = each_record[0]
        cur_stime = each_record[2]
        cur_etime = each_record[3]
        count_dict = avoid_collision(noc_records)
        #print count_dict
        threshold_times = list()
        noc_records.sort(key = lambda x : (x[2],x[3]))
        dec_counter = 0
        for er in noc_records:
            #print er
            stime = er[2]
            ftime = er[3]
            if stime in count_dict and count_dict[stime] <= 3:
                #print "appended to the list"
                task_list.append(er)
            else:
                #print "greater than 3"
                # Greater than 3
                for k in count_dict.keys():
                    if ftime != k:
                        count_dict[k] -= 1
                    else:
                        break
        noc_records = list()
        noc_records.append(each_record)
    else:
        # same location
        noc_records.append(each_record)
count_dict = avoid_collision(noc_records)

noc_records.sort(key = lambda x : (x[2],x[3]))
for er in noc_records:
    stime = er[2]
    ftime = er[3]
    if stime in count_dict and count_dict[stime] <= 3:
        #print "appended to the list"
        task_list.append(er)
    else:
        #print "greater than 3"
        # Greater than 3
        for k in count_dict.keys():
            if ftime != k:
                count_dict[k] -= 1
            else:
                count_dict[k] -= 1
                break
print "final list"
for l in task_list:
    print l
