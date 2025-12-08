#!/usr/bin/env python3
""" Advent of code day 6 """

import sys
import aoc
import math


def __main__():
    part1 = 0
    part2 = 0
    homework = []
    lines = []
    nums = []

    for line in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        homework.append(line.split())
        lines.append(line)

    lc = len(lines)

    for i in range(len(homework[0])):
        val = 0
        oper = homework[len(homework) - 1][i]

        if oper == '*':
            val = 1
        for j in range(len(homework) - 1):
            if oper == '+':
                val += int(homework[j][i])
            else:
                val *= int(homework[j][i])
        part1 += val

    for i in range(len(lines[0]) -1, -1, -1):
        v = 0
        blank = True

        for j in range(lc - 1):
            if lines[j][i] != ' ':
                blank = False
                v = v * 10 + int(lines[j][i])

        if not blank:
            nums.append(v)

        if lines[lc - 1][i] == '+':
            part2 += sum(nums)
            nums = []

        if lines[lc - 1][i] == '*':
            part2 += math.prod(nums)
            nums = []

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
