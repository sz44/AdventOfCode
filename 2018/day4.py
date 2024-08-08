# [1518-04-15 23:56] Guard #2213 begins shift
# [1518-10-31 00:36] wakes up

from datetime import datetime

#[datetime, info]

# array 0-59 total 
#{10: [0,0,0,12,0,23,4,2,2,2,0,0,1,2]
# most minuets asleep = sum(array)
# minuet most asleep = max(array)

#{id10: {set of minuets when asleep}}, total = sum(set)
#{id10: {minuet: total}}, find id with most minutes = sum(minutes.values())
# find minuet with most total, iterate, max(minutes.values())

data = []
f = open("input_day4.txt")
for line in f:
    r = line.find(']')
    datetime_str = line[1:r] 
    datetime_format = '%Y-%m-%d %H:%M'
    dt = datetime.strptime(datetime_str, datetime_format)
    text = line[r+1:].strip()
    data.append((dt, text))
f.close()

data.sort()

hashmap = {}
current_id = None
sleep_start = 0
for dt, text in data:
    if text == 'falls asleep':
        sleep_start = dt.minute
    elif text == 'wakes up':
        for i in range(sleep_start, dt.minute):
            hashmap[current_id][i] += 1
    else:
        id = text.split()[1].strip('#')
        if id not in hashmap:
            hashmap[id] = [0] * 60
        current_id = id

# import json
# with open("input_day4_b.json", "a") as f:
    # f.write(json.dumps(hashmap))
    # for key,val in hashmap.items():
        # f.write(f'{key}: {val}\n')

most_asleep_id = None
most_asleep_time = 0
most_asleep_at_min = 0
for key,val in hashmap.items():
    total = 0
    most = 0
    for i in range(len(val)):
        total += val[i]
        if val[i] > most:
            most = val[i] 
            most_asleep_at_min = i
    if total > most_asleep_time:
        most_asleep_id = key
        most_asleep_time = total 

print(most_asleep_id, most_asleep_time)

most_asleep_at = max(hashmap[most_asleep_id])

print(most_asleep_at)

print(most_asleep_at_min)
print(most_asleep_at_min * int(most_asleep_id))

target_id = ''
target_val = 0
target_ind = 0
for id, minuets in hashmap.items():
    for i in range(len(minuets)):
        if minuets[i] > target_val:
            target_val = minuets[i]
            target_ind = i
            target_id = id

# print(most_frq_at_min, most_frq_id)
print(target_id, target_ind, target_val)
print(int(target_id) * target_ind)
