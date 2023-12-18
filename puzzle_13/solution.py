def find_horizontal_reflection_bounded(pattern):
    for start in range(len(pattern) - 1):
        for end in range(start + 1, len(pattern), 2):
            mid = (end - start + 1) // 2
            if ''.join(pattern[start:start + mid]) == ''.join(pattern[start + mid:end + 1][::-1]):
                if start == 0 or end == len(pattern)-1:
                    return start + mid
    return 0

def find_horizontal_reflection_simple(pattern):
    for start in range(len(pattern) - 1):
        # First, look to the right
        end = len(pattern)
        if not(end-start)%2:
            mid = (end - start + 1) // 2
            # print(start, start+mid, end)
            # print(''.join(pattern[start:start + mid]), ''.join(pattern[start + mid:end + 1][::-1]))
            if ''.join(pattern[start:start + mid]) == ''.join(pattern[start + mid:end + 1][::-1]):
                return start + mid

        # Then, look the left
        end = start+1
        start = 0
        if not(end-start)%2:
            mid = (end + 1) // 2
            # print(start, start + mid, end)
            # print(''.join(pattern[start:start + mid]), ''.join(pattern[start + mid:end][::-1]))
            if ''.join(pattern[start:start + mid]) == ''.join(pattern[start + mid:end][::-1]):
                return start + mid
    return 0

print(find_horizontal_reflection_simple(["a","b", "b","a","c"]))

sum = 0
with open('input.txt') as f:
    pattern = []
    transposed_pattern = []
    for line in f:
        line = line.strip()
        if line == '':
            # Fix the transposed pattern to make sure it's a rotated pattern instead
            transposed_pattern = [l[::-1] for l in transposed_pattern]

            # horizontal reflection
            row = find_horizontal_reflection_simple(pattern)
            col = find_horizontal_reflection_simple(transposed_pattern)

            print("\n".join(pattern))
            print("-----")
            print("\n".join(transposed_pattern))
            print(row,col)

            sum += col + (row * 100)

            pattern = []
            transposed_pattern = []
        else:
            pattern.append(line)

            new_pattern = transposed_pattern == []
            for i, c in enumerate(line):
                if new_pattern:
                    transposed_pattern.append(c)
                else:
                    transposed_pattern[i] += c

    # Fix the transposed pattern to make sure it's a rotated pattern instead
    transposed_pattern = [l[::-1] for l in transposed_pattern]
    row = find_horizontal_reflection_simple(pattern)
    col = find_horizontal_reflection_simple(transposed_pattern)

    print("\n".join(pattern))
    print("-----")
    print("\n".join(transposed_pattern))
    print(row, col)

    sum += col + (row * 100)

print(sum)