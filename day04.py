#!/usr/bin/env

import aoc
import sys


def neighbour_count(paper, x, y, w, h):
    result = 0

    for i in range(-1, 2):
        if x + i < 0 or x + i >= w:
            continue
        for j in range(-1, 2):
            if y + j < 0 or y + j >= h:
                continue
            if i == 0 and j == 0:
                continue
            if paper[y + j][x + i] == '@':
                result += 1
    return result


def remove_roll(paper, x, y):
    line = paper[y]
    paper[y] = line[:x] + '.' + line[x + 1:]


def __main__():
    paper = aoc.read_file(sys.argv[1]).strip().split('\n')
    h = len(paper)
    w = len(paper[0])
    part1 = 0
    part2 = 0
    delta = 1

    for y in range(h):
        for x in range(w):
            if paper[y][x] == '@':
                if neighbour_count(paper, x, y, w, h) < 4:
                    part1 += 1

    while delta > 0:
        delta = 0
        for y in range(h):
            for x in range(w):
                if paper[y][x] == '@':
                    if neighbour_count(paper, x, y, w, h) < 4:
                        delta += 1
                        remove_roll(paper, x, y)
        part2 += delta

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    __main__()
