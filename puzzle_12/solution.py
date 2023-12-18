from itertools import combinations

def find_possible_match(pattern, groups):
    n_groups = len(groups)
    n_empty = len(pattern) - sum(groups) - (n_groups - 1)
    matching_pattern = 0

    # This line borrowed from https://towardsdatascience.com/solving-nonograms-with-120-lines-of-code-a7c6e0f627e4 first code block
    opts = list(combinations(range(n_groups + n_empty), n_groups))

    for opt in opts:
        line = ""
        g = 0
        for pos in range(n_groups + n_empty):
            if pos in opt:
                line += "#" * groups[g] + ("." if g < len(groups)-1 else "")
                g += 1
            else:
                line += "."

        # check if line is compatible with pattern
        for i in range(len(pattern)):
            if pattern[i] != "?" and pattern[i] != line[i]:
                break
        else:
            matching_pattern += 1

    return matching_pattern

# print(find_possible_match("???.###", [1,1,3]))

total_patterns = 0
with open('input.txt') as f:
    for line in f:
        pattern, groups = line.strip().split()
        groups = [int(g) for g in groups.split(",")]

        total_patterns += find_possible_match(pattern, groups)

print(total_patterns)