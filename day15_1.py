f = open("day15_input.txt", "r")

grid = []

def my_hash(string):
    res = 0
    for c in string:
        res += ord(c)
        res *= 17
        res %= 256
    return res

sum = 0

for i, line in enumerate(f.read().split(',')):
    sum += my_hash(line)

print(sum)
