f = open("day4_input.txt", "r")

seeds = list(map(int, f.readline().strip().split(":")[1].split()))
f.readline()
mn = int(seeds[0])



for category in range(7):
    nums = f.readline().split()
    new_seeds = [-1 for i in range(len(seeds))]
    while len(nums) == 3:
        nums = list(map(int,nums))
        for i,seed in enumerate(seeds):
            if nums[1] <= seed < nums[1] + nums[2] and new_seeds[i] == -1:
                new_seeds[i] = nums[0] + seed - nums[1]
        nums = f.readline().split()
    for i,seed in enumerate(new_seeds):
        if seed == -1:
            new_seeds[i] = seeds[i]
    seeds = new_seeds
    print(seeds)
    print("---------------")

print(min(seeds))