f = open("day12_input.txt", "r")


def count(string, nums):
    res = 0
    # print(string)
    # print(nums)
    # if len(nu
    if sum(nums) > len(string):
        return 0
    if len(nums) == 0:
        # print("yes")
        return not '#' in string
    if len(string) == 0:
        return 0
    while string and string[0] == '.':
        string = string[1:]
    if len(string) == 0:
        return 0
    i = 0
    while i < len(string) and (string[i] == '#' or string[i] == '?'):
        i += 1
    if i >= nums[0]:
        for j in range(i - nums[0] + 1):
            if j + nums[0] < len(string) and string[j + nums[0]] == '#':
                continue
            if '#' in string[:j]:
                continue
            res += count(string[j + nums[0] + 1:], nums[1:])
    if not '#' in string[:i]:
        res += count(string[i:], nums)
    return res


res = 0

for i, line in enumerate(f.read().strip().split('\n')):
    string, nums = line.split()
    nums = list(map(int, nums.split(',')))
    res += count(string, nums)

print(res)
