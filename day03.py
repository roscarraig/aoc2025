#!/usr/bin/env

import aoc
import sys


def joltage(battery, count):
    pos = 0
    l = len(battery)
    cells = []
    for i in range(count):
        a = max(list(battery[pos:l - (count - i - 1)]))
        cells.append(a)
        pos += battery[pos:].index(a) + 1
    return int(''.join(cells))


def __main__():
    part1 = 0
    part2 = 0

    for battery in aoc.read_file(sys.argv[1]).strip().split('\n'):
        part1 += joltage(battery, 2)
        part2 += joltage(battery, 12)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
