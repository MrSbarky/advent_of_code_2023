import time

f = open("day16_input.txt", "r")

grid = []

for i, line in enumerate(f.read().strip().split('\n')):
    grid.append(list(line))

start = time.time()


def explore(start):
    stack = [start]
    energised = [[False] * len(grid[0]) for i in range(len(grid))]
    seen = set()
    while stack:
        i, j, prev_dir = stack.pop()
        if (i, j, prev_dir) in seen:
            continue
        seen.add((i, j, prev_dir))
        if i < 0 or i == len(grid):
            continue
        if j < 0 or j == len(grid[0]):
            continue

        energised[i][j] = True

        if grid[i][j] == '.':
            if prev_dir == 'north':
                stack += [(i - 1, j, prev_dir)]
            elif prev_dir == 'east':
                stack += [(i, j + 1, prev_dir)]
            elif prev_dir == 'south':
                stack += [(i + 1, j, prev_dir)]
            elif prev_dir == 'west':
                stack += [(i, j - 1, prev_dir)]
        elif grid[i][j] == '\\':
            if prev_dir == 'north':
                stack += [(i, j - 1, 'west')]
            elif prev_dir == 'east':
                stack += [(i + 1, j, 'south')]
            elif prev_dir == 'south':
                stack += [(i, j + 1, 'east')]
            elif prev_dir == 'west':
                stack += [(i - 1, j, 'north')]
        elif grid[i][j] == '/':
            if prev_dir == 'north':
                stack += [(i, j + 1, 'east')]
            elif prev_dir == 'east':
                stack += [(i - 1, j, 'north')]
            elif prev_dir == 'south':
                stack += [(i, j - 1, 'west')]
            elif prev_dir == 'west':
                stack += [(i + 1, j, 'south')]
        elif grid[i][j] == '|':
            if prev_dir == 'north':
                stack += [(i - 1, j, 'north')]
            elif prev_dir == 'south':
                stack += [(i + 1, j, 'south')]
            elif prev_dir == 'east' or prev_dir == 'west':
                stack += [(i - 1, j, 'north')]
                stack += [(i + 1, j, 'south')]
        elif grid[i][j] == '-':
            if prev_dir == 'east':
                stack += [(i, j + 1, 'east')]
            elif prev_dir == 'west':
                stack += [(i, j - 1, 'west')]
            elif prev_dir == 'south' or prev_dir == 'north':
                stack += [(i, j + 1, 'east')]
                stack += [(i, j - 1, 'west')]
    count = 0
    for line in energised:
        for char in line:
            if char:
                count += 1

    return count


res = 0
for i in range(len(grid)):
    res = max(res, explore((i, 0, 'east')))
    res = max(res, explore((i, len(grid[0]) - 1, 'west')))

for j in range(len(grid[0])):
    res = max(res, explore((0, j, 'south')))
    res = max(res, explore((len(grid)-1, j, 'north')))

print("Time take:", time.time() - start)
# print("Max stack size:", mx_size)

print(res)
