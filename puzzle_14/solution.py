from collections import defaultdict


# all coord and dir is in (x, y) format

def tilt_platform(platform, ball_pos):
    x, y = ball_pos

    y = y - 1
    while y >= 0 and platform[y][x] == '.':
        # try to move the ball
        platform[y + 1][x] = '.'
        platform[y][x] = 'O'

        y = y - 1

    return platform


def get_tilted_load(platform):
    width, height = len(platform[0]), len(platform)

    for y in range(1, height):
        for x in range(width):
            if platform[y][x] == 'O':
                platform = tilt_platform(platform, (x, y))

            # for line in platform:
            #	print(''.join(line))
            # print('=========')

    load = 0
    for y in range(height):
        for x in range(width):
            if platform[y][x] == 'O':
                load += height - y

    return load


with open('input.txt') as f:
    platform = []
    for line in f:
        line = line.strip()
        platform.append([c for c in line])

    load_total = get_tilted_load(platform)

print(load_total)