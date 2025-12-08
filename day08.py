#!/usr/bin/env python3
""" Advent of code day 8 """

import sys
import math
import aoc


def connect(boxes, a, b):
    """ Connect box a to box b """

    boxes[a]['connected'].add(b)
    boxes[b]['connected'].add(a)


def trace(boxes, ind, seen):
    result = set([ind])
    seen.add(ind)

    for node in boxes[ind]['connected']:
        if node not in seen:
            result |= trace(boxes, node, seen)
    return result


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
                "connected": set()
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

    seen = set()

    for i in range(len(boxes)):
        if i in seen:
            continue
        cl = len(trace(boxes, i, seen))
        if cl > 0:
            circuitlens.append(cl)

    circuitlens.sort(reverse=True)
    part1 = math.prod(circuitlens[:3])

    print(f"Part 1: {part1}")
    pointer = 1000
    more = len(circuitlens) - 1

    while more > 0:
        for i in range(pointer, pointer + more):
            a, b, _ = links[i]
            connect(boxes, a, b)

        seen = set()
        circuitlens = []
        pointer += more

        for i in range(len(boxes)):
            if i in seen:
                continue

            cl = len(trace(boxes, i, seen))

            if cl > 0:
                circuitlens.append(cl)

        more = len(circuitlens) - 1

    part2 = boxes[a]['coord'][0] * boxes[b]['coord'][0]

    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
