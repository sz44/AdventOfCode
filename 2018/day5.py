
class Node:
    def __init__(self, val, prev, next = None):
        self.val = val
        self.prev = prev
        self.next = next

left = Node('_', None)
root = left
par = left
with open("input_day5.txt") as f:
    for c in f.read():
        if c == '\n':
            break
        node = Node(c, par)
        par.next = node
        par = node

while True:
    d = 0
    node = root.next
    while node:
        # match found remove 2
        if node.next and abs(ord(node.val) - ord(node.next.val)) == 32:
            d += 1
            node.prev.next = node.next.next
            node.next.next.prev = node.prev
            node = node.next
        node = node.next

    if d == 0:
        break

res = ''
node = root.next
while node:
    res += node.val
    node = node.next

print(len(res))

# with open("output_day5.txt", 'w') as f:
    # f.write(res)
    
def find(res):
    for i in range(1,len(res)):
        if (res[i].islower() and not res[i-1].islower() or res[i-1].islower() and not res[i].islower()) and res[i].lower() == res[i-1].lower():
            print(i, res[i-1], res[i]) 