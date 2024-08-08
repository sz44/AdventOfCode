line = open("input_day5.txt").read().strip()

def react(x):
    res = ['']
    for c in x:
        if c == res[-1].swapcase():
            res.pop()
        else:
            res.append(c)
    
    return ''.join(res)

print(len(react(line)))

m = 5E4
for i in range(ord('A'), ord('Z')+1):
    l = []
    for a in line:
        if a != chr(i) and a != chr(i).lower():
            l.append(a)
    res = len(react(l))
    if res < m:
        m = res
print(m) 