import re

def remap_nums(num_range, mappings):
    min_num = float("inf")
    for num in range(*num_range):
        new_num = num
        for mapping in mappings:
            for maps in mapping:
                dest_start, source_start, range_val = maps
                if new_num >= source_start and new_num < (source_start+range_val):
                    diff = new_num - source_start
                    new_num = dest_start + diff
                    break  # break to stop the new_num value to be changed further in this round of mapping

        min_num = min(min_num, new_num)
    return min_num


mappings = []
num_ranges = []
sum = 0

with open('input.txt') as f:
    mapping = []
    map_block = False
    for index, line in enumerate(f):
        line = line.strip()
        if index == 0: # Always seeds first
            seeds = [int(i) for i in re.findall(r"(\d+)", line)]
            for i in range(0, len(seeds)-1, 2):
                num_ranges.append((seeds[i], seeds[i]+seeds[i+1]))
                sum += seeds[i+1]
        elif "map" in line:
            map_block = True
        elif map_block:
            if line != "":
                mapping.append([int(i) for i in re.findall(r"(\d+)", line)])
            else:
                map_block = False
                mappings.append(mapping)

                mapping = []
    mappings.append(mapping)

print(sum)
nums = [remap_nums(num_range, mappings) for num_range in num_ranges]
print(nums)
print(min(nums))
