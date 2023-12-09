import re

def get_next_token(sequence):
    final_numbers = []

    while True:
        print(sequence)
        final_numbers.append(sequence[-1])
        sequence = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]

        if not any(sequence):  # We are in the final layer
            break

    final_numbers.reverse()
    new_token = final_numbers[0]
    for num in final_numbers[1:]:
        new_token = new_token + num

    return new_token


tokens = []
with open('input.txt') as f:
    for line in f:
        tokens.append(get_next_token([int(i) for i in line.strip().split()]))

    print(sum(tokens))

