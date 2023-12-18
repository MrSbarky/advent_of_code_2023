f = open("day14_input.txt", "r")

grid = []

for i, line in enumerate(f.read().strip().split('\n')):
    grid.append(line)

last_rock = [0] * len(grid[0])
count = [0] * len(grid[0])

res = 0

for i,line in enumerate(grid):
    for j,char in enumerate(line):
        if char == 'O':
            res += len(grid) + 1 - (last_rock[j] + count[j] + 1)
            count[j] += 1
        elif char == '#':
            last_rock[j] = i + 1
            count[j] = 0

print(res)
