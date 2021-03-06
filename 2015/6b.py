import time


lights = []
size = 1000
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    lights.append(row)


def control(inst):
    if inst[0]=='turn':
        start = inst[2].split(',')
        end = inst[4].split(',')
    else:
        start = inst[1].split(',')
        end = inst[3].split(',')

    for i in range(int(start[1]), int(end[1])+1):
        for j in range(int(start[0]), int(end[0])+1):
            if inst[1]=='on':
                lights[i][j] += 1
            elif inst[1]=='off':
                if lights[i][j] > 0:
                    lights[i][j] -= 1
            else:
                lights[i][j] += 2



t0 = time.clock()
with open('day6txt', 'r') as data:
    for line in data.readlines():
        a = line.strip('\n').split(' ')
        #print(a)
        control(a)

t1 = time.clock()
print('time: ', t1-t0)


count = 0

for i in lights:
    for j in i:
       count += j

print(count)


