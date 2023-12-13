f = open("day3_input.txt", "r")

grid = []

for line in f.readlines():
    grid += [[*line[:-1]]]

width = len(grid[0])
height = len(grid)

res = 0


def is_symbol(c):
    return not (c.isnumeric() or c == '.')


for i in range(height):
    num = ""
    adj_to_sym = False
    for j in range(width):
        if grid[i][j] == '.':
            new_adj_to_sym = (i > 0 and is_symbol(grid[i - 1][j])) \
                          or (i < height - 1 and is_symbol(grid[i + 1][j]))
            if (adj_to_sym or new_adj_to_sym) and num:
                res += int(num)
            adj_to_sym = new_adj_to_sym
            num = ""
        elif grid[i][j].isnumeric():
            num += grid[i][j]
            adj_to_sym |= (i > 0 and is_symbol(grid[i - 1][j])) \
                          or (i < height - 1 and is_symbol(grid[i + 1][j]))
        else:
            if num:
                res += int(num)
            adj_to_sym = True
            num = ""
    if adj_to_sym and num:
        res += int(num)

print(res)
