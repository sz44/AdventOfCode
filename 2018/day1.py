
def f():
    total = 0
    seen = set([0])
    while True:
        with open("./input.txt") as f:
            for l in f:
                l = l.strip()
                total += int(l)
                if total in seen:
                    print(total)
                    return
                seen.add(total)
                
f()