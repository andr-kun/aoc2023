from collections import defaultdict

maze = []


# all coord and dir is in (x, y) format

def trace_rays(start, dir):
    x, y = start

    while (x >= 0 and y >= 0) and (x < width and y < height):
        # print(x,y)
        # print(counter)

        # for line in traced:
        #	print(line)
        # print('==========')

        # guard for infinite loop
        # if we ever retrace our step in the exact direction as before, we can just quit
        if tuple(dir) in traced_dict.get((x, y), set()):
            break
        else:
            traced_dict[(x, y)].add(tuple(dir))

        traced[y][x] = 1
        if maze[y][x] == '|' and dir[1] == 0:
            dir = [0, 1]
            rays.append(([x, y - 1], [0, -1]))
        elif maze[y][x] == '-' and dir[0] == 0:
            dir = [1, 0]
            rays.append(([x - 1, y], [-1, 0]))
        elif maze[y][x] == '\\':
            dir = dir[::-1]
        elif maze[y][x] == '/':
            dir = [d * -1 for d in dir[::-1]]

        x, y = x + dir[0], y + dir[1]


def get_energised_count(pos, dir):
    # print(pos, dir)
    global traced
    global rays
    global traced_dict
    traced = [[0] * width for _ in range(height)]
    rays = [([x, y], dir)]
    traced_dict = defaultdict(set)

    while len(rays) > 0:
        trace_rays(*rays.pop())

    total = 0
    for line in traced:
        total += sum(line)
    return total


with open('input.txt') as f:
    for line in f:
        line = line.strip()
        maze.append(line)

    width = len(maze[0])
    height = len(maze)
    print(width, height)

    max_total = 0
    for x in range(width):
        for y, dir in [(0, [0, 1]), (height - 1, [0, -1])]:
            max_total = max(max_total, get_energised_count((x, y), dir))

    for y in range(height):
        for x, dir in [(0, [1, 0]), (width - 1, [-1, 0])]:
            max_total = max(max_total, get_energised_count((x, y), dir))

print(max_total)

