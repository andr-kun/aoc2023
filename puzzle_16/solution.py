from collections import defaultdict

maze = []
traced = []
rays = []
traced_dict = defaultdict(set)
width, height = 0, 0


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


with open('input.txt') as f:
    for line in f:
        line = line.strip()
        maze.append(line)
        traced.append([0] * len(line))

    width = len(maze[0])
    height = len(maze)
    print(width, height)
    rays.append(([0, 0], [1, 0]))
    while len(rays) > 0:
        trace_rays(*rays.pop())
    # print(rays)

total = 0
for line in traced:
    total += sum(line)
print(total)