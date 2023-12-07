import math
from collections import Counter

card_strength = {j:i for i,j in enumerate("AKQJT98765432"[::-1])}

def card_sort(card_bid):
    card, bid = card_bid

    card_counts = list(Counter(card).values())
    # Possible counts = [5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1]

    hand_score = 0
    if (freq_hand := max(card_counts)) > 1:
        if freq_hand == 3:
            if len(card_counts) == 2:  # [3,2]
                hand_score = 4
            else:  # [3,1,1]
                hand_score = 3
        elif freq_hand == 2:
            if len(card_counts) == 3: # [2,2,1]
                hand_score = 2
            else:
                hand_score = 1
        else:  # [2,1,1,1]
            hand_score = freq_hand + 1

    card_score = [card_strength[c] for c in card]

    print((card, hand_score, *card_score))
    return (hand_score, *card_score)

with open('input.txt') as f:
    cards_bids = []
    for line in f:
        cards_bids.append(line.strip().split())

    cards_bids.sort(key=card_sort)
    print(cards_bids)
    print(sum([b*(r+1) for b, r in zip([int(c[1]) for c in cards_bids], range(0, len(cards_bids)))]))

