#!/usr/bin/env python3
""" Advent of code day 10 """

import sys
import numpy as np
import aoc


def press(target, button):
    result = list(target)
    for point in button:
        result[point] = 1 - result[point]
    return result


def press2(target, button):
    result = list(target)
    for point in button:
        result[point] += 1
    return result


def find_presses(target, buttons):
    count = 0
    wave = [list(target)]
    jolted = [[0] * len(target)]
    presses = [-1]

    while True:
        count += 1
        nextwave = []
        nextpress = []
        nextjolt = []

        for i in range(len(wave)):
            for j in range(presses[i] + 1, len(buttons)):
                newtarget = press(wave[i], buttons[j])
                newjolt = press2(jolted[i], buttons[j])
                if max(newtarget) == 0:
                    return count, newjolt
                nextwave.append(newtarget)
                nextpress.append(j)
                nextjolt.append(newjolt)
        wave = nextwave
        presses = nextpress
        jolted = nextjolt


def click(jolt, buttons, presses):
    rjolt = list(jolt)
    clicks = 0

    for i in range(len(buttons)):
        if presses & (1 << i):
            for item in buttons[i]:
                rjolt[item] -= 1
            clicks += 1
    for item in rjolt:
        if item % 2:
            clicks = 1000000
    return rjolt, clicks


def find_presses2(jolt, buttons, cache):
    tjolt = tuple(jolt)

    if tjolt in cache:
        return cache[tjolt]

    cache[tjolt] = 1000000

    for item in jolt:
        if item < 0:
            return cache[tjolt]

    bjolt = [x % 2 for x in jolt]

    for i in range(1 << len(buttons)):
        rjolt, clicks = click(bjolt, buttons, i)
        if clicks >= 1000000:
            continue
        njolt = [jolt[j] + rjolt[j] - bjolt[j] for j in range(len(jolt))]

        if min(njolt) < 0:
            continue
        if max(njolt) > 0:
            clicks += 2 * find_presses2([x >> 1 for x in njolt], buttons, cache)
        if clicks < cache[tjolt]:
            cache[tjolt] = clicks

    return cache[tjolt]


def __main__():
    part1 = 0
    part2 = 0

    for line in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        cache = {}
        target = [0 if x == '.' else 1 for x in line[1:].split(']')[0]]
        buttons = [[int(y) for y in x[1:-1].split(',')] for x in line.split('] ')[1].split(' ')[:-1]]
        jolt = [int(x) for x in line.split('{')[1][:-1].split(',')]
        c, _ = find_presses(target, buttons)
        part1 += c
        part2 += find_presses2(jolt, buttons, cache)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
