f = open("day6_input.txt", "r")

times = list(map(int, f.readline().strip().split(":")[1].split()))
distances = list(map(int, f.readline().strip().split(":")[1].split()))

res = 1

for i,time in enumerate([60947882]):
    beats = 0
    for j in range(time+1):
        if (time - j) * j > 475213810151650:
            print(time + 1 - j * 2)
            break

    res *= beats

print(res)
