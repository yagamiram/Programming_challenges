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
import user41_zuRLQSO1pM4ubyP_2 as test_case

'''

Generate the string
'''
string_list = list()
for idx in range(1,7):
    string = "C" + str("%03d" % idx)
    string_list.append(string)
location_ids = ['right-top','right-bottom','left-top','left-bottom','center-top','center-bottom']
t = test_case.TestCase(string_list, location_ids, 0, 10, 0, 15)
final_list = t.generate_test_case(500)



'''
Sort the input in the following way:
1. Sort the content in asc
2. Sort the location in asc
3. Sort the starting time in asc
4. Sort the ending time in desc
'''
final_list.sort(key=lambda x: (x[1], x[0], x[2], -x[3]))
for l in final_list:
    print l
'''
Now from each list get the starting time and ending time
If the next record in the list has starting time > ending time then keep it 
and update the new ending time as the next record's ending time
If not remove the record.
'''
after_list = list()
current = final_list[0][1]
end_time  = final_list[0][3]
content = final_list[0][0]
after_list.append(final_list[0])
for l in final_list[1:]:
    if current == l[1]:
        if content != l[0]:
            # append it
            content = l[0]
            end_time = l[3]
            after_list.append(l)
        elif end_time < l[2]:
            # append it
            end_time = l[3]
            after_list.append(l)
    else:
        content = l[0]
        current = l[1]
        end_time = l[3]
        after_list.append(l)
print "after list"
for l in after_list:
    print l
print "again sort the list by starting time"
after_list.sort(key=lambda x: (x[2], x[1]))
for l in after_list:
    print l
'''
Now pick each starting time with the location and remove the rest if 
it is greater than 3
'''
new_list = list()
current = after_list[0][2]
location = after_list[0][1]
new_list.append(after_list[0])
count = 1
for l in after_list[1:]:
    if current == l[2]:
        # same time 
        if location == l[1]:
            if count < 3:
                count += 1
                new_list.append(l)
        else:
            # new location
            count = 0
            location = l[1]
    else:
        # differnet time
        current = l[2]
        location = l[1]
        new_list.append(l)
print "after"
for l in new_list:
    print l
print "now sorting with end time"
new_list.sort(key=lambda x: (x[3], x[1]))
for l in new_list:
    print l
        
