import re
from dataclasses import dataclass
import logging
import typing

@dataclass
class Node:
    name: str
    left: str = None
    right: str = None


def find_cycle(guide, network, start_point):
    cur_node = start_point
    steps = 0
    guide_length = len(guide)
    nodes_seen = {}
    endpoints = set()

    while True:
        direction = guide[steps % guide_length]
        cur_node = network[cur_node.left if direction == "L" else cur_node.right]
        steps += 1

        # Check if we have seen the node before
        if cur_node.name not in nodes_seen:
            nodes_seen[cur_node.name] = steps

            if cur_node.name[-1] == "Z":
                endpoints.add(cur_node.name)
        else:
            if (steps - nodes_seen[cur_node.name]) % guide_length == 0:
                # Full cycle detected
                break

    cycle_length = steps - nodes_seen[cur_node.name]

    print(steps)
    print(nodes_seen)
    print(len(endpoints))
    print("start_cycle", cur_node.name)
    print("cycle_length", cycle_length)

    return cycle_length, [nodes_seen[endpoint] for endpoint in endpoints]


def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    """Combine two phased rotations into a single phased rotation

    Returns: combined_period, combined_phase

    The combined rotation is at its reference point if and only if both a and b
    are at their reference points.

    From https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset
    """
    gcd, s, t = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def extended_gcd(a, b):
    """Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    From https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


with open('input.txt') as f:
    navigation_guide = ""
    network = {}
    start_nodes = []
    for index, line in enumerate(f):
        line = line.strip()
        if index == 0:
            navigation_guide = line
        else:
            if node := re.search(r'([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)', line):
                node_name, node_left, node_right = node.groups()
                network[node_name] = Node(node_name, node_left, node_right)
                if node_name.endswith("A"):
                    start_nodes.append(network[node_name])

    cycles = []
    for node in start_nodes:
        cycles.append(find_cycle(navigation_guide, network, node))

    print(cycles)
    # Surprisingly, all 'offset' to the first endpoint are the same value as the cycles.

    # The solution below ends up being an over-engineered solution due to special properties of the input
    # - Only 1 end point per start point
    # - Cycle phases are the same as the cycle lengths/periods
    # Very frustrating that the question does not specify this at all! Solution should not be tailored to a single
    # input/special properties of the input and should be generalisable to all possible input as defined in the question

    # Since we only have one end point, we don't need to try all possible endpoint combination.
    cycles = [(cycle[0], cycle[1][0]) for cycle in cycles]

    cur_cycle = cycles[0]
    for cycle in cycles[1:]:
        cur_cycle = combine_phased_rotations(cur_cycle[0], cur_cycle[1], cycle[0], cycle[1])

    if cur_cycle[1] == 0:
        print(cur_cycle[0])
    else:
        print(-cur_cycle[1] % cur_cycle[0])
