f = open("day2_input.txt", "r")

res = 0

break_flag = False

for i, line in enumerate(f.readlines()):
    sets = line.strip().split(": ")[1]
    sets_arr = sets.split("; ")
    red_max = 0
    green_max = 0
    blue_max = 0
    for my_set in sets_arr:
        for pick in my_set.split(", "):
            [num, colour] = pick.split(" ")
            if colour == "red":
                red_max = max(red_max, int(num))
            elif colour == "green":
                green_max = max(green_max, int(num))
            else:
                blue_max = max(blue_max, int(num))
    res += red_max * green_max * blue_max

print(res)
