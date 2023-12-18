import re

frame_evaluated = 0

def find_possible_match(pattern, group, prefix="", level=1):
    global frame_evaluated

    print(level, pattern, group, prefix)
    frame_evaluated += 1
    possible_match = 0

    # Special case - check if group is still valid
    prefix_groups = [len(g.group()) for g in re.finditer(r"(#+)", prefix)]
    if len(prefix_groups) > len(group):
        return possible_match
    for i in range(len(prefix_groups)):
        if prefix_groups[i] > group[i]:
            print("jumping out", level)
            return possible_match

    if "?" not in pattern:  # We now have a complete pattern
        full_pattern = prefix + pattern
        if [len(g.group()) for g in re.finditer(r"(#+)", full_pattern)]== group:
            possible_match += 1
    else:
        diverging_index = pattern.index("?")
        prefix += pattern[:diverging_index]

        possible_match += find_possible_match(pattern[diverging_index + 1:], group, prefix + "#", level + 1)
        possible_match += find_possible_match(pattern[diverging_index + 1:], group, prefix + ".", level + 1)

    return possible_match

def find_possible_match_alt(pattern, group, prefix="", level=1):
    global frame_evaluated

    print(level, pattern, group, prefix)
    frame_evaluated += 1
    possible_match = 0

    if "?" not in pattern:  # We now have a complete pattern
        full_pattern = prefix + pattern
        if [len(g.group()) for g in re.finditer(r"(#+)", full_pattern)] == group:
            possible_match += 1
    else:
        diverging_index = pattern.index("?")
        prefix += pattern[:diverging_index]

        # remove any groups that is already covered by the prefix
        for c in ".#":
            new_prefix = prefix + c
            prefix_groups = [len(g.group()) for g in re.finditer(r"(#+)", new_prefix)]
            print(prefix_groups, group)

            if len(prefix_groups) > len(group):
                continue

            for i in range(len(prefix_groups)):
                if (i < len(prefix_groups) - 1 and prefix_groups[i] != group[i]) or prefix_groups[i] > group[i]:
                    print("jumping out", level)
                    break
            else:
                possible_match += find_possible_match_alt(pattern[diverging_index + 1:], group, new_prefix, level + 1)

    return possible_match

def find_possible_match_alt(pattern, group, level=1):
    global frame_evaluated

    print(level, pattern, group)
    frame_evaluated += 1
    possible_match = 0

    if len(group) == 0:
        return possible_match

    if "?" not in pattern:  # We now have a complete pattern
        full_pattern = pattern
        if [len(g.group()) for g in re.finditer(r"(#+)", full_pattern)] == group:
            possible_match += 1
    else:
        diverging_index = pattern.index("?")
        prefix = pattern[:diverging_index]

        for c in "#.":
            new_prefix = prefix + c
            prefix_groups = [len(g.group()) for g in re.finditer(r"(#+)", new_prefix)]
            print(level, new_prefix, prefix_groups, group)

            # remove any groups that is already covered by the prefix
            if len(prefix_groups) > 0:
                print("In")
                if prefix_groups[0] == group[0]:
                    print("Recursing")
                    possible_match += find_possible_match_alt(pattern[diverging_index + 1:], group[1:], level + 1)
                elif prefix_groups[0] > group[0]:
                    possible_match += 0
                else:
                    possible_match += find_possible_match_alt(pattern[diverging_index + 1:], group, level + 1)
            else:
                possible_match += find_possible_match_alt(pattern[diverging_index + 1:], group, level + 1)

    return possible_match


# print(find_possible_match("???.###", [1,1,3]))

total_patterns = 0
with open('test_input.txt') as f:
    for line in f:
        pattern, groups = line.strip().split()
        groups = [int(g) for g in groups.split(",")]

        total_patterns += find_possible_match_alt(pattern, groups)

print(frame_evaluated)
print(total_patterns)