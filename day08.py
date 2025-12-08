#!/usr/bin/env python3
""" Advent of code day 8 """

import sys
import math
import aoc


def connect(boxes, a, b):
    """ Connect box a to box b """
    if boxes[a]['circuit'] == boxes[b]['circuit']:
        return

    both = [boxes[a]['circuit'], boxes[b]['circuit']]
    c = min(both)
    d = max(both)

    boxes[c]['circuitnodes'] |= boxes[d]['circuitnodes']
    boxes[d]['circuitnodes'] = set()
    boxes[a]['circuit'] = c
    boxes[b]['circuit'] = c


def __main__():
    part1 = 0
    part2 = 0
    boxes = []
    links = []
    i = 0
    circuitlens = []

    for point in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        boxes.append(
            {
                "coord": [int(x) for x in point.split(',')],
                "circuit": i,
                "circuitnodes": set([i])
            }
        )
        i += 1

    for i in range(len(boxes) - 1):
        for j in range(i + 1, len(boxes)):
            dist = math.dist(boxes[i]['coord'], boxes[j]['coord'])
            links.append((i, j, dist))

    links.sort(key=lambda link: link[2])

    for i in range(1000):
        a, b, _ = links[i]
        connect(boxes, a, b)

    for box in boxes:
        circuitlens.append(len(box['circuitnodes']))

    circuitlens.sort(reverse=True)
    print(sum(circuitlens))
    print(circuitlens[:3])
    part1 = math.prod(circuitlens[:3])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
    # 8360 low


if __name__ == '__main__':
    __main__()
