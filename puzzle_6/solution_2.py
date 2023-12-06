import re

def boat_race(time, distance):
    time, distance = int(time), int(distance)
    win = 0
    for i in range(1, time):
        distance_traveled = i*(time-i)
        win += distance_traveled > distance
    return win

with open('input.txt') as f:
    time_distance = []
    for index, line in enumerate(f):
        time_distance.append(re.findall(r"\d", line))
    time_distance = ["".join(num) for num in time_distance]

    print(boat_race(*["".join(num) for num in time_distance]))
