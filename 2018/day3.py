
def a():
    #1 @ 286,440: 19x24
    res = 0
    width = 1000
    height = 1000
    grid = [[0] * width for i in range(height)]

    with open("./input_day3.txt") as f:
        for line in f.readline():
            print(line)
            id, _, start, size = line.split(' ')
            id = id.strip('#')
            start = start.strip(':').split(',')
            size = size.strip().split('x')
            
            x = int(start[0])
            y = int(start[1])
            w = int(size[0])
            h = int(size[1])
            id = int(id)

            for row in range(h):
                for col in range(w):
                    if grid[y+row][x+col] != 0:  
                        grid[y+row][x+col] = -1
                    else:
                        grid[y+row][x+col] = id

        f.seek(0)
        for line in f.readlines():
            id, _, start, size = line.split(' ')
            id = id.strip('#')
            start = start.strip(':').split(',')
            size = size.strip().split('x')
            
            x = int(start[0])
            y = int(start[1])
            w = int(size[0])
            h = int(size[1])
            id = int(id)

            ans = True

            if id == 1:
                print(id)

            for row in range(h):
                for col in range(w):
                    if grid[y+row][x+col] == -1:  
                        ans = False
            
            if ans:
                print(id)
                return 

    return
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == -1:
                res += 1
    print(res)
a()