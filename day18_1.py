import heapq as hq
import math

f = open("day18_input.txt", "r")

grid = []

dirs = []
steps = []
colours = []

for i, line in enumerate(f.read().strip().split('\n')):
    dir, step, colour = line.split(" ")
    dirs.append(dir)
    steps.append(int(step))
    colours.append(colour)

n = sum(steps)

lava = [[False] * 700 for i in range(700)]

pos = (350, 350)
lava[pos[0]][pos[1]] = True

dirToMove = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

min_x, max_x = n, n
min_y, max_y = n, n

for i, dir in enumerate(dirs):
    for step in range(steps[i]):
        pos = tuple(map(sum, zip(dirToMove[dir], pos)))
        lava[pos[0]][pos[1]] = True
        min_x = min(min_x, pos[0])
        max_x = max(max_x, pos[0])
        min_y = min(min_y, pos[1])
        max_y = max(max_y, pos[1])

# print(n)
# print(min_x)
# print(max_x)
# print(min_y)
# print(max_y)

count = 0

for i, line in enumerate(lava):
    last_dir = ""
    interior = False
    for j, char in enumerate(line):
        if char:
            count += 1
            if last_dir == "":
                if lava[i - 1][j] and lava[i + 1][j]:
                    interior = not interior
                elif lava[i - 1][j]:
                    last_dir = "U"
                elif lava[i + 1][j]:
                    last_dir = "D"
            elif not lava[i][j + 1]:
                next_dir = ""
                if lava[i - 1][j]: next_dir = "U"
                if lava[i + 1][j]: next_dir = "D"
                if last_dir != next_dir: interior = not interior
                last_dir = ""
        else:
            if interior:
                lava[i][j] = True
                count += 1

# for line in lava:
#     print(''.join(list(map(lambda x: '#' if x else '.', line))))

print(count)