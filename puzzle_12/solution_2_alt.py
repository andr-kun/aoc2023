import re

def find_permutations(pattern, groups, prefix="", level=0):
    permutation = 0

    print("new", pattern, groups, prefix, level)
    if len(pattern) == 0:
        return None

    if len(groups) == 0:
        print('empty')
        if '#' not in pattern:  # There should be no more groups (though there can still be ? but all will become .)
            permutation += 1
    elif len(pattern) < (sum(groups)+len(groups)):
        print('too short')
        permutation = 0
    elif '?' not in pattern:
        print('no ?')
        # The pattern is static for the remaining. Now check the validity of the remaining group
        cur_groups = [len(g.group()) for g in re.finditer(r'(#+)', pattern)]
        if cur_groups == groups:
            permutation += 1
    else:
        divergence = pattern.find('?')
        prefix, pattern = prefix+pattern[:divergence], pattern[divergence + 1:]

        for c in ".#":
            new_prefix = prefix + c
            new_groups = groups
            cur_groups = [len(g.group()) for g in re.finditer(r'(#+)', new_prefix)]
            print(cur_groups)

            if len(cur_groups) > 0:
                print("in")
                mismatch_index = 0
                for i in range(len(cur_groups)):
                    if cur_groups[i] > groups[i]:
                        return permutation
                new_groups = new_groups[mismatch_index:]
                new_prefix = new_prefix.rsplit(".", 1)[-1]

            permutation += find_permutations(pattern, new_groups, new_prefix, level+1)

    return permutation


permutations = 0
with open('sample_input_2.txt') as f:
    for line in f:
        pattern, groups = line.strip().split()
        groups = [int(i) for i in groups.split(',')]

        permutations += find_permutations(pattern, groups)

print(permutations)