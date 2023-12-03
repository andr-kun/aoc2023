import re
import time

sum = 0
star_pos = []
num_matrix = []
matrix_width = 0


def number_search(pos):
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    nums = []

    for offset in offsets:
        xpos = pos[0] + offset[0]
        ypos = pos[1] + offset[1]

        if (xpos < 0 or ypos < 0) or (xpos >= matrix_width or ypos >= matrix_width):
            continue

        if xpos in num_matrix[ypos]:
            num = num_matrix[ypos][xpos]
            if num not in nums:
                nums.append(num)

    return [int(n.group()) for n in nums]


t = time.time()
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        star_line = list(re.finditer(r"\*", line))
        star_pos.append(star_line)
        matrix_width = len(line)

        line_dict = {}
        for num in re.finditer(r"(\d+)", line):
            for i in range(*num.span()):
                line_dict[i] = num

        num_matrix.append(line_dict)

for y, star_line in enumerate(star_pos):
    for star in star_line:
        nums = number_search((star.span()[0], y))
        if len(nums) > 1:
            sum += nums[0] * nums[1]

print(sum)
print(time.time()-t)