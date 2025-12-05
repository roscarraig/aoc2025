#!/usr/bin/env

import aoc
import sys


def fresh(item, ranges):
    for range in ranges:
        if item >= range[0] and item <= range[1]:
            return True
    return False


def merge(item, ranges):
    i = 0
    while i < len(ranges):
        check = ranges[i]
        i += 1
        if item[0] >= check[0] and item[1] <= check[1]:
            return
        if item[1] < check[0]:
            continue
        if item[0] > check[1]:
            continue
        if item[0] < check[0] and item[1] <= check[1]:
            item[1] = check[0] - 1
            continue
        if item[0] < check[0] and item[1] > check[1]:
            merge([check[1] + 1, item[1]], ranges)
            item[1] = check[0] - 1
            continue
        if item[0] >= check[0] and item[1] > check[1]:
            item[0] = check[1] + 1
            continue
    ranges.append(item)


def __main__():
    lines = aoc.read_file(sys.argv[1]).strip().split('\n')
    count = 0
    ranges = []
    part1 = 0
    part2 = 0

    for line in lines:
        if len(line) == 0:
            break
        count += 1
        merge([int(x) for x in line.split('-')], ranges)

    for line in lines[count + 1:]:
        if fresh(int(line), ranges):
            part1 += 1

    print(f"Part 1: {part1}")

    for item in ranges:
        part2 += item[1] + 1 - item[0]

    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
