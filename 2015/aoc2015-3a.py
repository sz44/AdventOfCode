with open('aoc2015-3a.txt') as file:
    data = file.read()
    positions = []
    x = 0
    y = 0
    for i in data:
        if i=='^': y+=1
        elif i=='v': y-=1
        elif i=='>': x+=1
        elif i=='<': x-=1
        positions.append((x,y))
    print(len(set(positions)))
    #print(positions)


