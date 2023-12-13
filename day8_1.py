f = open("day8_input.txt", "r")

step_seq = f.readline().strip()
f.readline()

instructions = {}

for line in f.read().strip().split('\n'):
    first, second = line.split(" = ")
    left, right = second.split(", ")
    left = left[1:]
    right = right[:-1]
    instructions[first] = [left,right]

curr = "RGZ"
last = "PBA"

steps = 0

while curr != last:
    for step in step_seq:
        if step == 'L':
            curr = instructions[curr][0]
        else:
            curr = instructions[curr][1]
        steps += 1
        if curr == last:
            break

print(steps)