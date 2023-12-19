import re
import bisect
from itertools import combinations

stars = []
empty_col = []
empty_row = []
transposed_input = []
with open('input.txt') as f:
    for y, line in enumerate(f):
        cur_star = [(star.span()[0], y) for star in re.finditer(r"(#)", line)]
        stars.extend(cur_star)

        if len(cur_star) == 0:
            empty_row.append(y)

        for x, char in enumerate(line):
            if y == 0:
                transposed_input.append(char)
            else:
                transposed_input[x] += char

    for x, line in enumerate(transposed_input):
        if "#" not in line:
            empty_col.append(x)

print(stars)
for i in range(len(stars)):
    x, y = stars[i]

    x_expansion = bisect.bisect_left(empty_col, x)*(1000000-1)
    y_expansion = bisect.bisect_left(empty_row, y)*(1000000-1)

    x += x_expansion
    y += y_expansion
    stars[i] = (x,y)
print(stars)

dist_sum = 0
for star_pair in combinations(stars, 2):
    star_one, star_two = star_pair

    dist = abs(star_one[0] - star_two [0]) + abs(star_one[1] - star_two[1])
    dist_sum += dist

print(dist_sum)
