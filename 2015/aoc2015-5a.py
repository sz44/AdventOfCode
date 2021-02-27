import re
s = 'adf df df eff pq iuo oozrzzo'
p = '([aeiou]{3,})'
p2 = '([a-z])\\1'
p3 = '(ab|cd|pq|xy)'
m = re.search(p3, s)
if m: print(m)

p4 = '([aeiou])'

niceCount = 0

with open('day5txt', 'r') as s:
    #print(s.readlines().strip('\n'))
    for line in s.readlines():
        if len(re.findall(p4,line))>=3:
            if len(re.findall(p2,line))>=1:
                if len(re.findall(p3,line))==0:
                    print(line)
                    niceCount += 1

print(niceCount)
#([a-z])\1([a-z]*)([a-z])\3
#([a-z][a-z])([a-z]*)\1
#([a-z]{2})[a-z]*\1
