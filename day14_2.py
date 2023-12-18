f = open("day14_input.txt", "r")

grid = []

for i, line in enumerate(f.read().strip().split('\n')):
    grid.append(list(line))

last_rock = [0] * len(grid[0])
count = [0] * len(grid[0])

res = 0

def cycle():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                height = i
                while height > 0 and grid[height-1][j] == '.':
                    grid[height][j] = '.'
                    grid[height-1][j] = 'O'
                    height -= 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                width = j
                while width > 0 and grid[i][width - 1] == '.':
                    grid[i][width] = '.'
                    grid[i][width - 1] = 'O'
                    width -= 1

    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0]) - 1, -1, -1):
            if grid[i][j] == 'O':
                height = i
                while height < len(grid) - 1 and grid[height + 1][j] == '.':
                    grid[height][j] = '.'
                    grid[height + 1][j] = 'O'
                    height += 1

    for i in range(len(grid) - 1, -1, -1):
        for j in range(len(grid[0]) - 1, -1, -1):
            if grid[i][j] == 'O':
                width = j
                while width < len(grid[0]) - 1 and grid[i][width + 1] == '.':
                    grid[i][width] = '.'
                    grid[i][width + 1] = 'O'
                    width += 1

def result():
    res = 0
    for i,line in enumerate(grid):
        for j,char in enumerate(line):
            if char == 'O':
                res += len(grid) - i

    return res

new_grid = []

seen = set()

i = 0

while i < 200:
    cycle()
    i += 1
    if hash(str(grid)) in seen:
        print(i, ':', result())
    seen.add(hash(str(grid)))




