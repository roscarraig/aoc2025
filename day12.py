#!/usr/bin/env python3
""" Advent of code day 12 """

import sys
import aoc


def __main__():
    part1 = 0
    part2 = 0
    storage = []
    itemindex = 0
    items = {}

    for line in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        if 'x' in line:
            parts = line.split(': ')
            dims = [int(x) for x in parts[0].split('x')]
            parcels = [int(x) for x in parts[1].split(' ')]
            want = sum([items[i] * parcels[i] for i in range(len(parcels))])
            if want <= dims[0] * dims[1]:
                part1 += 1
        elif ':' in line:
            itemindex = int(line.split(':')[0])
            items[itemindex] = 0
        else:
            items[itemindex] += line.count('#')

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
