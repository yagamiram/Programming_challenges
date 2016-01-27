import user41_SX2EPRxekJ_9 as task1
import random
print "new records"
for l in task1.noc_records:
    print l
    
frame = random.randint(0,15)
new_list = list()
for l in task1.noc_records:
    if l[2] <= frame <= l[3]:
        new_list.append(l)
        
print "new list"
print "================="
for l in new_list:
    print l
window_score = dict()
window_score = {'center-bottom':2.0,
                'center-top':1.5,
                'left-bottom':1.25,
                'left-top':1.15,
                'right-bottom':1.0,
                'right-top':0.75}
windows = window_score.keys()
windows.sort()

content_map = dict()
for l in new_list:
    content_map[l[0]] = False
print content_map

def find_max(idy, ridx, content_map):
    if idy >= len(windows):
        # no more windows
        return -1
    elif ridx >= len(new_list):
        # no more records
        return -1
    else:
        window = windows[idy]
        final_list = list()
        for idx in range(ridx, len(new_list)):
            record = new_list[idx]
            if window == record[1]:
                value = window_score[window] * record[4]
                content_map[record[0]] = True
                chosen = value + find_max(idy+1, idx+1, content_map)
                content_map[record[0]] = False
                not_chosen = find_max(idy+1, idx+1, content_map)
                final_list.append(max(chosen, not_chosen))
        return max(final_list) if len(final_list) != 0 else -1
print find_max(0, 0, content_map)
