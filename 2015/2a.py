f = open('input', 'r')

total = 0
totalr = 0
for line in f:
    a = line.strip('\n').split('x')
    a = [int(i) for i in a]
    a.sort()
    #print(a)
    r = 2*a[0]+2*a[1]+a[0]*a[1]*a[2]
    d = 2*int(a[0])*int(a[1])+2*int(a[0])*int(a[2])+2*int(a[1])*int(a[2])+int(a[0])*int(a[1])
    total += d
    totalr += r

print(total, ' ', totalr)

