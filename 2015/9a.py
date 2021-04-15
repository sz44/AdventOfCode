import itertools

with open('day9.txt', 'r') as data:
    distances = [a.strip().split() for a in data.readlines()]
    #for a in data.readlines():
    #d2 = [[b[0],b[2],b[4]] for b in distances]
    #map(lambda x: [x[0],x[2],x[4]], distances)

cities = []

for i in distances:
    for j in i:
        if j[0].isupper():
            cities.append(j)

cities = set(cities)
cities = list(cities)
print(cities)

p = itertools.permutations(cities,len(cities))

for i in p:
    #check
    
#def follow(city):
    
