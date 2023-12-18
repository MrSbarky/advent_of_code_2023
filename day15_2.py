f = open("day15_input.txt", "r")

grid = []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def my_hash(string):
    res = 0
    for c in string:
        res += ord(c)
        res *= 17
        res %= 256
    return res

sum = 0

hashmap = dict()
node_refs = dict()

for i, op in enumerate(f.read().split(',')):
    if op[-1] == '-':
        string = op[:-1]
        if not string in node_refs:
            continue
        prev = node_refs[string].prev
        next = node_refs[string].next
        prev.next = next
        if next:
            next.prev = prev
        else:
            hashmap[my_hash(string)].prev = prev
        del node_refs[string]
    else:
        string, num = op.split('=')
        hash = my_hash(string)
        if not hash in hashmap.keys():
            hashmap[hash] = Node('dummy')
            hashmap[hash].prev = hashmap[hash]

        if not string in node_refs.keys():
            new_node = Node(num)
            hashmap[hash].prev.next = new_node
            new_node.prev = hashmap[hash].prev
            hashmap[hash].prev = new_node

            node_refs[string] = new_node
        else:
            node_refs[string].data = num

res = 0

for j,key in enumerate(hashmap.keys()):
    i = 1
    node = hashmap[key].next
    while node:
        val = (key + 1) * i * int(node.data)
        res += val
        node = node.next
        i += 1

print("Part 2:", res)
