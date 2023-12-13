f = open("day10_input.txt", "r")

res = 0
grid = []

s_i = 0
s_j = 0

for i, line in enumerate(f.read().strip().split('\n')):
    if line.find('S') != -1:
        s_i = i
        s_j = line.find('S')
    grid.append(list(line))

seen = [[False] * len(grid[0]) for i in range(len(grid))]

loop = [[False] * len(grid[0]) for i in range(len(grid))]


def search(i, j, came_from):
    curr_i = i
    curr_j = j
    steps = 0
    while not grid[curr_i][curr_j] == 'S':
        loop[curr_i][curr_j] = True
        steps += 1
        if grid[curr_i][curr_j] == '-':
            if (came_from == "left" or came_from == "") and curr_j < len(grid[0]) - 1:
                curr_j += 1
                came_from = "left"
            elif came_from == "right" and curr_j > 0:
                curr_j -= 1
                came_from = "right"
            else:
                return 0
        elif grid[curr_i][curr_j] == '|':
            if (came_from == "up" or came_from == "") and curr_i < len(grid) - 1:
                curr_i += 1
                came_from = "up"
            elif came_from == "down" and curr_i > 0:
                curr_i -= 1
                came_from = "down"
            else:
                return 0
        elif grid[curr_i][curr_j] == 'F':
            if (came_from == "down" or came_from == "") and curr_j < len(grid[0]) - 1:
                curr_j += 1
                came_from = "left"
            elif came_from == "right" and curr_i < len(grid) - 1:
                curr_i += 1
                came_from = "up"
            else:
                return 0
        elif grid[curr_i][curr_j] == '7':
            if (came_from == "left" or came_from == "") and curr_i < len(grid) - 1:
                curr_i += 1
                came_from = "up"
            elif came_from == "down" and curr_j > 0:
                curr_j -= 1
                came_from = "right"
            else:
                return 0
        elif grid[curr_i][curr_j] == 'J':
            if (came_from == "up" or came_from == "") and curr_j > 0:
                curr_j -= 1
                came_from = "right"
            elif came_from == "left" and curr_i > 0:
                curr_i -= 1
                came_from = "down"
            else:
                return 0
        elif grid[curr_i][curr_j] == 'L':
            if (came_from == "right" or came_from == "") and curr_i > 0:
                curr_i -= 1
                came_from = "down"
            elif came_from == "up" and curr_j < len(grid[0]) - 1:
                curr_j += 1
                came_from = "left"
            else:
                return 0
        else:
            return 0

    print(int((steps + 1) / 2))
    return 1


search(s_i + 1, s_j, "up")

loop[s_i][s_j] = True
grid[s_i][s_j] = '|'

# for loop_row in loop:
#     print(loop_row)

count = 0

for i in range(len(grid)):
    outside = True
    last_seen = ""
    for j in range(len(grid[0])):
        if loop[i][j]:
            print(grid[i][j], end='')
            if grid[i][j] == '|':
                outside = not outside
            elif grid[i][j] == 'L' or grid[i][j] == 'F':
                last_seen = grid[i][j]
            elif grid[i][j] == 'J':
                if last_seen == 'F':
                    outside = not outside
                else:
                    last_seen = ""
            elif grid[i][j] == '7':
                if last_seen == 'L':
                    outside = not outside
                else:
                    last_seen = ""
        else:
            if not outside:
                print('I', end='')
                count += 1
            else:
                print('O', end='')
    print()

print(count)
