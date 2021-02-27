with open('aoc2015-3a.txt') as file:
    data = file.read()
    positions = []
    xs = 0
    ys = 0
    xr = 0
    yr = 0
    santa = True
    for i in data:
        if santa:
            if i=='^': ys+=1
            elif i=='v': ys-=1
            elif i=='>': xs+=1
            elif i=='<': xs-=1
            positions.append((xs,ys))
            santa = False
        elif not santa:
            if i=='^': yr+=1
            elif i=='v': yr-=1
            elif i=='>': xr+=1
            elif i=='<': xr-=1
            positions.append((xr,yr))
            santa = True

    print(len(set(positions)))
    #print(positions)


