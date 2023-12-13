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

def search(i, j, came_from):
    curr_i = i
    curr_j = j
    steps = 0
    while not grid[curr_i][curr_j] == 'S':
        seen[curr_i][curr_j] = True
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


if s_i < len(grid) - 1 and search(s_i + 1, s_j, "up") != 0:
    print(s_i + 1, s_j)
elif s_i > 0 and search(s_i - 1, s_j, "down") != 0:
    print(s_i - 1, s_j)
elif s_j < len(grid[0]) - 1 and search(s_i, s_j + 1, "left") != 0:
    print(s_i, s_j + 1)
elif s_j > 0 and search(s_i, s_j - 1, "right") != 0:
    print(s_i, s_j - 1)