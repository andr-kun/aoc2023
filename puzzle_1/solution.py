
with open("input.txt") as f:
    total = 0
    for line in f:
        nums = []
        line = line.strip()
        for char in line:
            if char.isnumeric():
                nums.append(char)

        if len(nums) > 0:
            total += int(nums[0] + nums[-1])

print(total)