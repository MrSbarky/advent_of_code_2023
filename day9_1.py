f = open("day9_input.txt", "r")

res = 0

for line in f.read().strip().split('\n'):
    arr = list(map(int, line.split(" ")))
    new_arr = []
    lasts = []
    not_all_zeros = True
    while not_all_zeros:
        not_all_zeros = False
        for i in range(len(arr) - 1):
            new_num = arr[i+1] - arr[i]
            if new_num != 0:
                not_all_zeros = True
            new_arr.append(new_num)
            if i == len(arr) - 2:
                lasts.append(new_num)
        arr = new_arr
        new_arr = []
    res += sum(lasts) + int(line.split(" ")[-1])

print(res)