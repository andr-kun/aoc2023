import re

def get_previous_token(sequence):
    first_numbers = []

    while True:
        print(sequence)
        first_numbers.append(sequence[0])
        sequence = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]

        if not any(sequence):
            break

    first_numbers.reverse()
    new_token = first_numbers[0]
    for num in first_numbers[1:]:
        new_token = num - new_token
        print(new_token)

    return new_token


tokens = []
with open('input.txt') as f:
    for line in f:
        tokens.append(get_previous_token([int(i) for i in line.strip().split()]))

    print(sum(tokens))

