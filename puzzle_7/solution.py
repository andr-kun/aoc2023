import math
from collections import Counter

card_strength = {j:i for i,j in enumerate("AKQJT98765432"[::-1])}

def card_sort(card_bid):
    card, bid = card_bid

    card_counts = sorted(Counter(card).values(), reverse=True)
    card_score = [card_strength[c] for c in card]

    return (card_counts, card_score)

with open('input.txt') as f:
    cards_bids = []
    for line in f:
        cards_bids.append(line.strip().split())

    cards_bids.sort(key=card_sort)
    print(cards_bids)
    print(sum([b*(r+1) for b, r in zip([int(c[1]) for c in cards_bids], range(0, len(cards_bids)))]))

