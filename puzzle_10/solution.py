import queue

# The pipes are arranged in a two-dimensional grid of tiles:
#
#     | is a vertical pipe connecting north and south.
#     - is a horizontal pipe connecting east and west.
#     L is a 90-degree bend connecting north and east.
#     J is a 90-degree bend connecting north and west.
#     7 is a 90-degree bend connecting south and west.
#     F is a 90-degree bend connecting south and east.
#     . is ground; there is no pipe in this tile.
#     S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what
#     shape the pipe has.

# (x,y)
directions = {
    "|": [(0, -1), (0, 1)],
    "-": [(1, 0), (-1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
    "S": [(0,1), (0, -1), (1, 0), (-1, 0)],
    ".": []
}

def traverse_maze(start_point, maze):
    pos_travelled = set()
    height, width = len(maze), len(maze[0])
    pos_queue = queue.SimpleQueue()

    # Check around starting point
    valid_entry = {
        (0, 1): "|LJ", # down
        (0, -1): "|7F",  # up
        (1, 0): "-J7",  # right
        (-1, 0): "-LF",  # left
    }
    for dir in valid_entry.keys():
        new_pos = (start_point[0] + dir[0], start_point[1] + dir[1])

        if (new_pos[0] < 0 or new_pos[0] > width) or (new_pos[1] < 0 or new_pos[1] > height):  # Out of bound
            continue

        if maze[new_pos[1]][new_pos[0]] in valid_entry[dir]:
            pos_queue.put([new_pos, 1])

    pos_travelled.add(start_point)
    score[start_point[1]][start_point[0]] = 0

    # Traverse maze until there is no more paths with BFS
    while not pos_queue.empty():
        pos, dist = pos_queue.get()
        pipe = maze[pos[1]][pos[0]]

        direction = directions[pipe]
        next_nodes_seen = 0
        for dir in direction:
            new_pos = (pos[0] + dir[0], pos[1] + dir[1])

            if (new_pos[0] < 0 or new_pos[0] > width) or (new_pos[1] < 0 or new_pos[1] > height): # Out of bound
                continue

            if new_pos not in pos_travelled:
                pos_queue.put([new_pos, dist + 1])
            else:
                next_nodes_seen += 1

        pos_travelled.add(pos)
        score[pos[1]][pos[0]] = dist

        if next_nodes_seen == len(direction) and len(direction) > 0:
            # This is the 'end' of the cycle since we can't move forward anymore as we have seen the next nodes
            return dist

    return 0


maze = []
score = []
with open('input.txt') as f:
    start_point = (0,0)  # x,y
    for y, line in enumerate(f):
        line = line.strip()

        if "S" in line:
            start_point = (line.index("S"), y)
        
        score.append([0 for _ in range(len(line))])
        maze.append(line)

print(start_point)
print("\n".join(maze))
print(traverse_maze(start_point, maze))
print("\n".join([",".join([str(i) for i in s]) for s in score]))
