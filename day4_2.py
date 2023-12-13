f = open("day4_input.txt", "r")

range_list = list(map(int, f.readline().strip().split(":")[1].split()))
i = 0
ranges = []
while i < len(range_list):
    ranges.append([range_list[i], range_list[i] + range_list[i+1] - 1])
    i += 2

f.readline()
print(ranges)
for category in range(7):
    nums = f.readline().split()
    new_ranges = []

    # 56 - 92 -> 60 - 97
    # 93 - 96 -> 56 - 59
    while len(nums) == 3:
        nums = list(map(int,nums))
        for i,range in enumerate(ranges):
            if nums[1] <= range[0] < nums[1] + nums[2] and nums[1] <= range[1] < nums[1] + nums[2]:
                new_ranges.append([nums[0] + range[0] - nums[1], nums[0] + range[1] - nums[1]])
                range[0] = -1
                range[1] = -1
            elif nums[1] <= range[0] < nums[1] + nums[2]:
                new_ranges.append([nums[0] + range[0] - nums[1], nums[0] + nums[2] - 1])
                range[0] = nums[1] + nums[2]
            elif nums[1] <= range[1] < nums[1] + nums[2]:
                new_ranges.append([nums[0], nums[0] + range[1] - nums[1]])
                range[1] = nums[1] - 1
        nums = f.readline().split()
    for range in ranges:
        if (range[0] != -1):
            new_ranges.append(range)
    ranges = new_ranges
    print(ranges)
    print("---------------")

print(min(ranges))