#!/usr/bin/env python3
""" Advent of code day 6 """

import sys
import aoc


def __main__():
    part1 = 0
    part2 = 0
    homework = []

    for line in aoc.read_file(sys.argv[1]).strip().split("\n"):
        homework.append(line.split())

    print(homework)
    for i in range(len(homework[0])):
        val = 0
        op = homework[len(homework) - 1][i]
        if op == '*':
            val = 1
        for j in range(len(homework) - 1):
            if op == '+':
                val += int(homework[j][i])
            else:
                val *= int(homework[j][i])
        part1 += val

    print (f"Part 1: {part1}")
    print (f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
