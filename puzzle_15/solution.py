def hash(string):
    val = 0
    for c in string:
        ascii = ord(c)
        val += ascii
        val = (val * 17) % 256
    return val


with open('input.txt') as f:
    instruction = f.read().strip().split(',')
    sums = 0
    for i in instruction:
        sums += hash(i)
    print(sums)