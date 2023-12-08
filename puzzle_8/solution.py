import re
from dataclasses import dataclass
import logging
import typing
log = logging.getLogger(__name__)

@dataclass
class Node:
    name: str
    left: str = None
    right: str = None


def traverse_node(guide, network):
    cur_node = network["AAA"]
    steps = 0
    guide_length = len(guide)

    while cur_node.name != "ZZZ":
        log.debug(cur_node)
        direction = guide[steps % guide_length]
        cur_node = network[cur_node.left if direction == "L" else cur_node.right]
        steps += 1

    return steps


# logging.basicConfig(level=logging.DEBUG)
with open('input.txt') as f:
    navigation_guide = ""
    network = {}
    for index, line in enumerate(f):
        line = line.strip()
        if index == 0:
            navigation_guide = line
        else:
            if node := re.search(r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)', line):
                node_name, node_left, node_right = node.groups()
                network[node_name] = Node(node_name, node_left, node_right)

    print(traverse_node(navigation_guide, network))

