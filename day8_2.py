f = open("day8_input.txt", "r")

step_seq = f.readline().strip()
f.readline()

instructions = {}

currs = []

for line in f.read().strip().split('\n'):
    first, second = line.split(" = ")
    left, right = second.split(", ")
    left = left[1:]
    right = right[:-1]
    instructions[first] = [left,right]
    if first[-1] == 'A':
        currs.append(first)

steps = 0

first_z = [-1] * len(currs)

steps = 0
while -1 in first_z:
    for step in step_seq:
        steps += 1
        for i,curr in enumerate(currs):
            if step == 'L':
                currs[i] = instructions[curr][0]
            else:
                currs[i] = instructions[curr][1]

            if currs[i][-1] == 'Z':
                first_z[i] = steps
        if not (-1 in first_z):
            break
        # if allEndInZ:
        #
        #     break

print(first_z)

from math import gcd
lcm = 1
for i in first_z:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)