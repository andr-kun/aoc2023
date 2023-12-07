from collections import Counter

card_strength = {j:i for i,j in enumerate("AKQT98765432J"[::-1])}

def card_sort(card_bid):
    card, bid = card_bid

    card_counts_dict = Counter(card)
    num_joker = card_counts_dict.pop("J", 0)
    card_counts = sorted(card_counts_dict.values(), reverse=True)

    # If J is in hand, we effectively have 5-n(J) cards:
    # n(J) = 1
    # [4] -> [5], [3,1] -> [4,1], [2,2] -> [3,2], [2,1,1] -> [3,1,1], [1,1,1,1] -> [2,1,1,1]
    # n(J) = 2
    # [3] -> [5], [2,1] -> [4,1], [1,1,1] -> [3,1,1]
    # n(J) = 3
    # [2] -> [5], [1,1] -> [4,1]
    # n(J) = 4
    # [1] -> [5]
    # The rule is basically add  n(J) to the first entry in the card_counts

    if num_joker == 5:  # Special case of all Joker card
        card_counts += [5]
    else:
        card_counts[0] += num_joker

    card_score = [card_strength[c] for c in card]

    return (card_counts, card_score)

with open('input.txt') as f:
    cards_bids = []
    for line in f:
        cards_bids.append(line.strip().split())

    cards_bids.sort(key=card_sort)
    print(cards_bids)
    print(sum([b*(r+1) for b, r in zip([int(c[1]) for c in cards_bids], range(0, len(cards_bids)))]))

