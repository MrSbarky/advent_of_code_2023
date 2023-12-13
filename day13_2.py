f = open("day13_input.txt", "r")

def mirrors(grid):
    for i in range(1,len(grid)):
        diffs = 0
        for j in range(min(i, len(grid) - i)):
            for k in range(len(grid[0])):
                if grid[i + j][k] != grid[i - j - 1][k]:
                    diffs += 1
            if diffs > 1:
                break
        if diffs == 1:
            return 100 * i

    for i in range(1,len(grid[0])):
        diffs = 0
        for j in range(min(i, len(grid[0]) - i)):
            for k in range(len(grid)):
                if grid[k][i + j] != grid[k][i - j - 1]:
                    diffs += 1
            if diffs > 1:
                break
        if diffs == 1:
            return i

grid = []
sum = 0
for i, line in enumerate(f.read().strip().split('\n')):
    if line == "":
        sum += (mirrors(grid))
        grid = []
        continue
    grid.append(line)

print(sum)