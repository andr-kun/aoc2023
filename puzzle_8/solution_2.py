import re
from dataclasses import dataclass
import logging
import typing

@dataclass
class Node:
    name: str
    left: str = None
    right: str = None


def traverse_nodes(guide, network, start_points):
    cur_nodes = start_points
    steps = 0
    guide_length = len(guide)

    num_paths = len(cur_nodes)
    arrived_nodes = 0

    while num_paths != arrived_nodes:
        direction = guide[steps % guide_length]

        arrived_nodes = 0
        for index, n in enumerate(cur_nodes):
            next_node = network[n.left if direction == "L" else n.right]
            cur_nodes[index] = next_node  # Here be danger. Creating a list is too expensive
            if next_node.name[-1] == "Z": arrived_nodes += 1

        steps += 1

    return steps


# logging.basicConfig(level=logging.DEBUG)
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
    print(len(start_nodes))
    print(traverse_nodes(navigation_guide, network, start_nodes))

