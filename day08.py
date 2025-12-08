#!/usr/bin/env python3
""" Advent of code day 7 """

import sys
import aoc


def distance(a, b):
    total = 0
    for i in range(3):
        total += (a[i] - b[i])**2
    return total


def connect(boxes):
    a = 0
    ad = boxes[0]['neard']

    for i in range(1, len(boxes) - 1):
        if boxes[i]['neard'] < ad:
            a = i
            ad = boxes[i]['neard']

    b = boxes[a]['near']

    if boxes[a]['circuit'] < boxes[b]['circuit']:
        c = boxes[a]['circuit']
        d = boxes[b]['circuit']
        boxes[c]['circuitnodes'] |= boxes[d]['circuitnodes']
        boxes[d]['circuitnodes'] = set()
        boxes[b]['circuit'] = c
    else:
        c = boxes[b]['circuit']
        d = boxes[a]['circuit']
        boxes[c]['circuitnodes'] |= boxes[d]['circuitnodes']
        boxes[d]['circuitnodes'] = set()
        boxes[a]['circuit'] = c

    print(a, boxes[a]['coord'], b, boxes[b]['coord'], c)
    nd = 0
    ni = -1

    for i in range(a + 1, len(boxes)):
        if boxes[i]['circuit'] == c:
            continue

        dist = boxes[a]['dists'][i] 

        if ni < 0 or dist < nd:
            ni = i
            nd = dist

    boxes[a]['near'] = ni
    boxes[a]['neard'] = nd
    
    nd = 0
    ni = -1

    for i in range(b + 1, len(boxes)):
        if boxes[i]['circuit'] == c:
            continue

        dist = boxes[b]['dists'][i] 

        if ni < 0 or dist < nd:
            ni = i
            nd = dist

    boxes[b]['near'] = ni
    boxes[b]['neard'] = nd

            
def __main__():
    part1 = 0
    part2 = 0
    boxes = []
    i = 0

    for point in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        boxes.append({"coord": [int(x) for x in point.split(',')], "dists":
                      {}, "circuit": i, "circuitnodes": set([i])})
        i += 1

    for i in range(len(boxes) - 1):
        nd = 0
        ni = -1
        for j in range(i + 1, len(boxes)):
            dist = distance(boxes[i]['coord'], boxes[j]['coord'])
            if ni < 0 or dist < nd:
                ni = j
                nd = dist
            boxes[i]['dists'][j] = dist
        boxes[i]['near'] = ni
        boxes[i]['neard'] = nd

    for i in range(9):
        connect(boxes)

    for i in range(len(boxes) - 1):
        if len(boxes[i]['circuitnodes']) > 0:
            print(len(boxes[i]['circuitnodes']), boxes[i]['circuitnodes'])

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
