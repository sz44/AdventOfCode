points = [
( 78, 335 ),
( 74, 309 ),
( 277, 44 ),
( 178, 286 ),
( 239, 252 ),
( 118, 354 ),
( 170, 152 ),
( 75, 317 ),
( 156, 318 ),
( 172, 45 ),
( 138, 162 ),
( 261, 195 ),
( 306, 102 ),
( 282, 67 ),
( 53, 141 ),
( 191, 237 ),
( 352, 180 ),
( 95, 247 ),
( 353, 357 ),
( 201, 327 ),
( 316, 336 ),
( 57, 43 ),
( 119, 288 ),
( 299, 328 ),
( 125, 327 ),
( 187, 186 ),
( 121, 151 ),
( 121, 201 ),
( 43, 67 ),
( 76, 166 ),
( 238, 148 ),
( 326, 221 ),
( 219, 207 ),
( 237, 160 ),
( 345, 244 ),
( 321, 346 ),
( 48, 114 ),
( 304, 80 ),
( 265, 216 ),
( 191, 92 ),
( 54, 75 ),
( 118, 260 ),
( 336, 249 ),
( 81, 103 ),
( 290, 215 ),
( 300, 246 ),
( 293, 59 ),
( 150, 274 ),
( 296, 311 ),
( 264, 286 )] 

# points = [
#     ( 1, 1 ),
#     ( 1, 6 ),
#     ( 8, 3 ),
#     ( 3, 4 ),
#     ( 5, 5 ),
#     ( 8, 9 )
# ]

def a():
    # find bound
    max_x = 0
    max_y = 0
    for x,y in points:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    max_x += 1
    max_y += 1
    # construct grid
    grid = [[0] * (max_x) for _ in range(max_y)]
    # fill grid
    for row in range(max_y):
        for col in range(max_x):
            # find closest point
            closest = (max_x*2, max_y*2)
            for i in range(len(points)):
                x,y = points[i]
                dist_to_point = abs(x - col) + abs(y - row)
                dist_to_closest = abs(closest[0] - col) + abs(closest[1] - row)
                if  dist_to_point < dist_to_closest:
                    closest = (x, y)
                    grid[row][col] = i
                elif dist_to_point == dist_to_closest:
                    grid[row][col] = -1
    # count area
    count = [0] * len(points)
    for row in range(max_y):
        for col in range(max_x):
            if grid[row][col] > -1:
                count[grid[row][col]] += 1
    # remove edge points
    for i in range(max_y):
        count[grid[i][0]] = 0
        count[grid[i][max_x-1]] = 0
    for j in range(max_x):
        count[grid[0][j]] = 0
        count[grid[max_y-1][j]] = 0
    # get max area
    print(max(count))

# a()

def b():
    target = 10000
    size = 0
    # find bound
    max_x = 0
    max_y = 0
    for x,y in points:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    # check all cells
    for row in range(max_y + 1):
        for col in range(max_x + 1):
            dist_total = 0
            # compute total distance
            for x,y in points:
                dist_total += abs(x - col) + abs(y - row)
            # update size
            if dist_total < target:
                size += 1
    # get size 
    print(size)

b()