import re
from collections import defaultdict

num_cards = defaultdict(lambda: 1)

with open('input.txt') as f:
    for index, line in enumerate(f):
        _, winning_num, own_num = re.split(r":|\|", line)
        winning_num = set(re.findall(r"(\d+)", winning_num))
        own_num = set(re.findall(r"(\d+)", own_num))

        own_win_num = len(own_num & winning_num)
        for i in range(index+1, index+own_win_num+1):
            num_cards[i] += num_cards[index]

print(sum(num_cards.values()) + (index-len(num_cards)+1))