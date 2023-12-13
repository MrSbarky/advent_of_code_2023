f = open("day6_input.txt", "r")

times = list(map(int, f.readline().strip().split(":")[1].split()))
distances = list(map(int, f.readline().strip().split(":")[1].split()))

res = 1

for i,time in enumerate(times):
    beats = 0
    for j in range(time+1):
        if (time - j) * j > distances[i]:
            beats += 1

    res *= beats

print(res)
