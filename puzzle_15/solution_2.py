from collections import defaultdict
import re


def hash(string):
    val = 0
    for c in string:
        ascii = ord(c)
        val += ascii
        val = (val * 17) % 256
    return val


boxes = defaultdict(list)
with open('input.txt') as f:
    instruction = f.read().strip().split(',')

    for i in instruction:
        label, op, focal = re.findall(r"([a-z]+)([=-])([0-9]*)", i)[0]

        box = hash(label)
        for i in range(len(boxes[box])):
            if label == boxes[box][i][0]:
                if op == '=':
                    boxes[box][i][1] = focal
                else:
                    del boxes[box][i]
                break
        else:
            if op == '=':
                boxes[box].append([label, focal])

power = 0
for box in boxes.keys():
    for i, lens in enumerate(boxes[box]):
        power += (box + 1) * (i + 1) * int(lens[1])
print(power)