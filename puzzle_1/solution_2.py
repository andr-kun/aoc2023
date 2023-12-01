num_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("input.txt") as f:
    total = 0
    for line in f:
        nums = []
        line = line.strip()
        i = 0

        while i < len(line):
            if line[i].isnumeric():
                nums.append(line[i])
            elif line[i:i+3] in num_mapping:
                nums.append(num_mapping[line[i:i+3]])
            elif line[i:i + 4] in num_mapping:
                nums.append(num_mapping[line[i:i + 4]])
            elif line[i:i + 5] in num_mapping:
                nums.append(num_mapping[line[i:i + 5]])

            i += 1

        if len(nums) > 0:
            total += int(nums[0] + nums[-1])

print(total)