import re

def remap_nums(number_list, mapping):
    new_nums = []
    for num in number_list:
        new_num = num
        for maps in mapping:
            dest_start, source_start, range_val = maps
            if num >= source_start and num < (source_start+range_val):
                diff = num - source_start
                new_num = dest_start + diff
        new_nums.append(new_num)

    return new_nums

with open('test_input.txt') as f:
    mapping = []
    nums = []
    map_block = False
    for index, line in enumerate(f):
        line = line.strip()
        if index == 0: # Always seeds first
            nums = [int(i) for i in re.findall(r"(\d+)", line)]
        elif "map" in line:
            map_block = True
        elif map_block:
            if line != "":
                mapping.append([int(i) for i in re.findall(r"(\d+)", line)])
            else:
                map_block = False
                nums = remap_nums(nums, mapping)
                mapping = []
                print(nums)

nums = remap_nums(nums, mapping)
print(sorted(nums))
print(min(nums))
