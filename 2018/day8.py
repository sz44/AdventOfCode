import re

f = open('input_day8.txt') 
data = [int(s) for s in f.read().split()]
# data2 = list(map(int, re.findall('\d+', f.read())))

# data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
# data = [int(s) for s in data.split()]

total = 0

def dfs(i):
    global total

    if i >= len(data):
        return 0

    children = data[i]
    metaData = data[i+1]

    skip = 2 

    # skip children
    for _ in range(children):
        skip += dfs(i + skip)

    # add to total
    for n in range(metaData):
        total += data[i + skip + n]

    # node size: 2 for header + size of children + metaData
    return skip + metaData

dfs(0)   

print(total)
