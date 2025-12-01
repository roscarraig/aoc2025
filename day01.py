#!/usr/bin/env python3

import aoc
import sys


def __main__():
    pos = 50
    part1 = 0
    part2 = 0

    for move in aoc.read_file(sys.argv[1]).split("\n"):
        if len(move) == 0:
            continue

        dist = int(move[1:])
        if dist > 99:
            part2 += int(dist / 100)
            dist %= 100

        if move[0] == 'L':
            dir = -1
            if pos == 0:
                part2 -= 1
        else:
            dir = 1
        pos += dir * dist
        opos = pos
        pos %= 100

        if opos != pos and pos != 0:
            part2 += 1

        if pos == 0:
            part1 += 1
            part2 += 1

    print (f"Part 1: {part1}")
    print (f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
