import re

sum = 0

with open('input.txt') as f:
    for line in f:
        _, winning_num, own_num = re.split(r":|\|", line)
        winning_num = set(re.findall(r"(\d+)", winning_num))
        own_num = set(re.findall(r"(\d+)", own_num))

        own_win_num = len(own_num & winning_num)
        if own_win_num > 0:
            sum += 2 ** (own_win_num - 1)

print(sum)
