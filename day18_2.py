import heapq as hq
import math

f = open("day18_input.txt", "r")

grid = []

dirs = []
steps = []
colours = []

intToDir = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}

for i, line in enumerate(f.read().strip().split('\n')):
    dir, step, colour = line.split(" ")
    dirs.append(intToDir[colour[-2]])
    steps.append(int(colour[2:-2], 16))

n = sum(steps)

# lava = [[False] * n * 2 for i in range(n * 2)]

pos = [0, 0]
# lava[pos[0]][pos[1]] = True

dirToMove = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

corners = [[0,0]]

for i, dir in enumerate(dirs):
    pos = [pos[0] + dirToMove[dir][0] * steps[i], pos[1] + dirToMove[dir][1] * steps[i]]
    corners.append(pos)

print(corners)

count = 0

# for i, line in enumerate(lava):
#     last_dir = ""
#     interior = False
#     for j, char in enumerate(line):
#         if char:
#             count += 1
#             if last_dir == "":
#                 if lava[i - 1][j] and lava[i + 1][j]:
#                     interior = not interior
#                 elif lava[i - 1][j]:
#                     last_dir = "U"
#                 elif lava[i + 1][j]:
#                     last_dir = "D"
#             elif not lava[i][j + 1]:
#                 next_dir = ""
#                 if lava[i - 1][j]: next_dir = "U"
#                 if lava[i + 1][j]: next_dir = "D"
#                 if last_dir != next_dir: interior = not interior
#                 last_dir = ""
#         else:
#             if interior:
#                 lava[i][j] = True
#                 count += 1

# for line in lava:
#     print(''.join(list(map(lambda x: '#' if x else '.', line))))