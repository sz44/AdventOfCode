
class Node:
    def __init__(self, val, prev, next = None):
        self.val = val
        self.prev = prev
        self.next = next

dummy = Node('', None)
root = dummy
par = root
with open("input_day5.txt") as f:
    for c in f.read():
        if c == '\n':
            break
        node = Node(c, par)
        if not root:
            root = node
            par = root
            continue
        par.next = node
        par = node

while True:
    d = 0
    #code
    node = root
    while node:
        if abs(ord(node.val) - ord(node.next.val)) == 32:
            node.
    if d == 0:
        break


print(root.next.val) 
            