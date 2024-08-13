testData = [
"Step C must be finished before step A can begin.",
"Step C must be finished before step F can begin.",
"Step A must be finished before step B can begin.",
"Step A must be finished before step D can begin.",
"Step B must be finished before step E can begin.",
"Step D must be finished before step E can begin.",
"Step F must be finished before step E can begin."
]

data = []
with open("input_day7.txt") as f:
    data = f.readlines()

adj = {}

for line in data:
    words = line.strip().split()
    val = words[1]
    key = words[-3]
    if key not in adj:
        adj[key] = set()
    if val not in adj:
        adj[val] = set()
    adj[key].add(val)

chars = sorted(adj.keys())

order = ''

done = set()

# part 1
# while len(order) < len(adj.keys()):
#     for c in chars:
#         # found available step
#         if len(adj[c]) == 0 and c not in done:
#             order += c
#             done.add(c)
#             for k,v in adj.items():
#                 if c in v:
#                     adj[k].remove(c)
#             # restart from sorted first
#             break

# print(adj)
# print(order)

# part 2
workers = 5
doing = dict() # char : time
time = 0

while len(order) < len(adj.keys()):
    # part 1: do jobs
    for k,v in doing.items():
        doing[k] -= 1
        if doing[k] < 1:
            done.add(k) 
            order += k
            workers += 1
            # update adj list
            for c,reqs in adj.items():
                if k in reqs:
                    adj[c].remove(k)
    
    # clean doing 
    for c in done:
        if c in doing:
            del doing[c]

    # part 2: add jobs to workers
    while workers > 0:
        for c in chars:
            if len(adj[c]) == 0 and c not in done and c not in doing:
                doing[c] = ord(c) - ord('A') + 1 + 60
                workers -= 1
                # job assigned, go to next worker
                break
        else:
            # print("no jobs available")
            break
        # no jobs available
        # break

    time += 1

print(order)
print(time) 