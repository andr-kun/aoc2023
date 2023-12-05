import re
from pyinter import IntervalSet, interval

def remap_nums(num_range, mappings):
    interval_set = IntervalSet([interval.closedopen(num_range[0], num_range[1])])

    # print("start", interval_set)
    for mapping in mappings:
        mapped_interval_set = IntervalSet()
        for maps in mapping:
            dest_start, source_start, range_val = maps
            source_interval = interval.closedopen(source_start, source_start + range_val)
            interval_intersection = interval_set.intersection([source_interval])
            for intersect in interval_intersection:
                # print(maps)
                # print("intersection", intersect)
                interval_set = interval_set.difference(intersect)
                # print("remainder", interval_set)


                new_start = dest_start + (intersect.lower_value - source_start)
                new_end = dest_start + (intersect.upper_value - source_start)
                mapped_interval_set.add(interval.closedopen(new_start, new_end))

        # Any remaining interval get added back in to mapped interval set as is
        mapped_interval_set = mapped_interval_set.union(interval_set)
        # print("map_done", mapped_interval_set)

        interval_set = mapped_interval_set

    # print(interval_set)
    return min([i.lower_value for i in iter(interval_set)])


mappings = []
num_ranges = []

with open('input.txt') as f:
    mapping = []
    map_block = False
    for index, line in enumerate(f):
        line = line.strip()
        if index == 0: # Always seeds first
            seeds = [int(i) for i in re.findall(r"(\d+)", line)]
            for i in range(0, len(seeds)-1, 2):
                num_ranges.append((seeds[i], seeds[i]+seeds[i+1]))
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

nums = [remap_nums(num_range, mappings) for num_range in num_ranges]
print(nums)
print(min(nums))
