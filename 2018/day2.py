
from collections import Counter

twoCount = 0
threeCount = 0

with open('2/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        counts = [0] * 26
        for c in line.strip():
            counts[ord('z')-ord(c)] += 1
        two = 0
        three = 0
        for i in range(len(counts)):
            if counts[i] == 2:
                two = 1
            if counts[i] == 3:
                three = 1
        twoCount += two
        threeCount += three

print(twoCount)
print(threeCount)
print(twoCount * threeCount)

with open("2/input.txt") as f:
    lines = f.readlines()
    for i in range(len(lines[0])):
        seen = set()
        d = dict()
        for j in range(len(lines)):
        # for line in lines:
            line = lines[j]
            l = line[:i]
            r = ''
            if i < len(lines[0]) - 1:
                r = line[i+1:]
            line2 = l + r
            if line2 in d:
                print(line)
                print(i)
                print(line2)
                print(l + " " + r)
                print("+++++++++++++")
                print(lines[d[line2]])
            # seen.add(line2)
            d[line2] = j
