from functools import reduce

f = open("day9_input.txt", "r")

res = 0

for line in f.read().strip().split('\n'):
    arr = list(map(int, line.split(" ")))
    new_arr = []
    firsts = [arr[0]]
    not_all_zeros = True
    while not_all_zeros:
        not_all_zeros = False
        for i in range(len(arr) - 1):
            new_num = arr[i+1] - arr[i]
            if new_num != 0:
                not_all_zeros = True
            new_arr.append(new_num)
            if i == 0:
                firsts.append(new_num)
        arr = new_arr
        new_arr = []
    print(firsts)
    res += reduce(lambda x,y: y-x, reversed(firsts), 0)

print(res)