import re
p = '([a-z][a-z])([a-z]*)\\1'
p2 = '([a-z])[a-z]\\1'

niceCount = 0

with open('day5txt', 'r') as data:
    for line in data.readlines():
        if re.findall(p, line):
            if re.findall(p2, line):
                print(line)
                niceCount += 1

print(niceCount)

