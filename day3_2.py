f = open("day3_input.txt", "r")

grid = []

for line in f.readlines():
    grid += [[*line[:-1]]]

height = len(grid)
width = len(grid[0])


def count_surrounding(i, j):
    count = 0
    if i > 0:
        if grid[i - 1][j].isnumeric():
            count += 1
        else:
            if j > 0:
                count += grid[i - 1][j - 1].isnumeric()
            if j < width - 1:
                count += grid[i - 1][j + 1].isnumeric()
    if j > 0 and grid[i][j - 1].isnumeric():
        count += 1
    if j < width - 1 and grid[i][j + 1].isnumeric():
        count += 1
    if i < height - 1:
        if grid[i + 1][j].isnumeric():
            count += 1
        else:
            if j > 0:
                count += grid[i + 1][j - 1].isnumeric()
            if j < width - 1:
                count += grid[i + 1][j + 1].isnumeric()
    return count


def read_num(i, j):
    curr_j = j
    res = ""
    while curr_j >= 0 and grid[i][curr_j].isnumeric():
        curr_j -= 1
    curr_j += 1
    while curr_j < width and grid[i][curr_j].isnumeric():
        res = res + grid[i][curr_j]
        curr_j += 1
    # print(int(res))
    return int(res)


def get_product(i, j):
    res = 1
    if i > 0:
        if grid[i - 1][j].isnumeric():
            if j < width - 1 and grid[i - 1][j + 1].isnumeric():
                res *= read_num(i - 1, j + 1)
            else:
                res *= read_num(i - 1, j)
        else:
            if j > 0 and grid[i - 1][j - 1].isnumeric():
                res *= read_num(i - 1, j - 1)
            if j < width - 1 and grid[i - 1][j + 1].isnumeric():
                res *= read_num(i - 1, j + 1)
    if j > 0 and grid[i][j - 1].isnumeric():
        res *= read_num(i, j - 1)
    if j < width - 1 and grid[i][j + 1].isnumeric():
        res *= read_num(i, j + 1)
    if i < height - 1:
        if grid[i + 1][j].isnumeric():
            if j < width - 1 and grid[i + 1][j + 1].isnumeric():
                res *= read_num(i + 1, j + 1)
            else:
                res *= read_num(i + 1, j)
        else:
            if j > 0 and grid[i + 1][j - 1].isnumeric():
                res *= read_num(i + 1, j - 1)
            if j < width - 1 and grid[i + 1][j + 1].isnumeric():
                res *= read_num(i + 1, j + 1)
    return res


count = 0

for i in range(height):
    for j in range(width):
        if grid[i][j] == '*':
            if count_surrounding(i, j) == 2:
                count += get_product(i, j)

print(count)
