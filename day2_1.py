f = open("day2_input.txt", "r")

res = 0

break_flag = False

for i, line in enumerate(f.readlines()):
    break_flag = False
    sets = line.split(": ")[1]
    sets_arr = sets.split("; ")
    for my_set in sets_arr:
        for pick in my_set.split(", "):
            [num, colour] = pick.split(" ")
            if (colour == "red" and int(num) > 12) or (colour == "green" and int(num) > 13) or (colour == "blue" and int(num) > 14):
                break_flag = True
                break
        if break_flag:
            break
    if not break_flag:
        res += i + 1

print(res)
