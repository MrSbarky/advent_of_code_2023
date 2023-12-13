f = open("day13_input.txt", "r")

def mirrors(grid):
    for i in range(1,len(grid)):
        mirror_line = True
        for j in range(min(i, len(grid) - i)):
            for k in range(len(grid[0])):
                if grid[i + j][k] != grid[i - j - 1][k]:
                    mirror_line = False
                    break
            if not mirror_line:
                break
        if mirror_line:
            return 100 * i

    for i in range(1,len(grid[0])):
        mirror_line = True
        for j in range(min(i, len(grid[0]) - i)):
            for k in range(len(grid)):
                if grid[k][i + j] != grid[k][i - j - 1]:
                    mirror_line = False
                    break
            if not mirror_line:
                break
        if mirror_line:
            return i

grid = []
sum = 0
for i, line in enumerate(f.read().strip().split('\n')):
    if line == "":
        sum += mirrors(grid)
        grid = []
        continue
    grid.append(line)

print(sum)