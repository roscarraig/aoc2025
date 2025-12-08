#!/usr/bin/env python3
""" Advent of code day 7 """

import sys
import aoc


def splitsa(grid, x):
    past = set([x])
    count = 0
    for i in range(1, len(grid)):
        future = set()
        for item in past:
            if grid[i][item] == '.':
                future.add(item)
            elif grid[i][item] == '^':
                future.add(item - 1)
                future.add(item + 1)
                count += 1
            else:
                print("Unexpected item:", grid[i][item])
        past = future
    return count


def splitsb(grid, x, y, seen):
    if (x, y) in seen:
        return seen[(x, y)]
    if y == len(grid):
        seen[(x, y)] = 1
    elif grid[y][x] == '^':
        seen[(x, y)] = splitsb(grid, x - 1, y + 1, seen) + splitsb(grid, x + 1, y + 1, seen)
    else:
        seen[(x, y)] = splitsb(grid, x, y + 1, seen)
    return seen[(x, y)]


def __main__():
    part1 = 0
    part2 = 0
    seen = {}
    grid = aoc.read_file(sys.argv[1]).strip('\n').split("\n")
    sx = grid[0].index('S')
    part1 = splitsa(grid, sx)
    part2 = splitsb(grid, sx, 1, seen)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
