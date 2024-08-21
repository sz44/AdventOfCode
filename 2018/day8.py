import re

f = open('input_day8.txt') 
data = [int(s) for s in f.read().split()]
# data2 = list(map(int, re.findall('\d+', f.read())))

# data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
# data = [int(s) for s in data.split()]

total = 0

def dfs(i):
    if i >= len(data):
        return 0

    children = data[i]
    metaData = data[i+1]

    skip = 2 

    childVals = []

    # skip children
    for _ in range(children):
        s, val = dfs(i + skip)
        skip += s
        childVals.append(val)

    val = 0

    if children:
        for n in range(metaData):
            ind = data[i + skip + n]
            if ind <= children:
                val += childVals[ind-1] 
    else:
        for n in range(metaData):
            val += data[i + skip + n]

    # part 1
    global total
    for n in range(metaData):
        total += data[i + skip + n]

    # node size: 2 for header + size of children + metaData
    skip += metaData

    return [skip, val]

a = dfs(0)   

# part 1
print(total)
# part 2
print(a[1])