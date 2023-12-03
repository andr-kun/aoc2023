import re

sum = 0
numbers_list = []
num_matrix = []


def symbol_search(pos):
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

    for offset in offsets:
        xpos = pos[0] + offset[0]
        ypos = pos[1] + offset[1]

        if (xpos < 0 or ypos < 0) or (xpos >= len(num_matrix[0]) or ypos >= len(num_matrix)):
            continue

        if num_matrix[ypos][xpos] not in set("0123456789."):
            return True

    return False


with open('input.txt') as f:
    for line in f:
        line = line.strip()
        number_line = list(re.finditer(r"(\d+)", line))
        numbers_list.append(number_line)

        num_matrix.append(line)

for y, numbers in enumerate(numbers_list):
    for num in numbers:
        valid_num = False
        for x in range(*num.span()):
            if symbol_search((x, y)):
                valid_num = True
                break

        if valid_num:
            sum += int(num.group())

print(sum)
