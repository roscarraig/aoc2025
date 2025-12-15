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


def jcheck(target, jolt):
    jpass = 1
    for i in range(len(target)):
        if jolt[i] > target[i]:
            return 2
        if jolt[i] != target[i]:
            jpass = 0
    return jpass


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
                    print('J', newjolt)
                    return count, newjolt
                nextwave.append(newtarget)
                nextpress.append(j)
                nextjolt.append(newjolt)
        wave = nextwave
        presses = nextpress
        jolted = nextjolt


def find_presses2a(jolt, buttons):
    count = 0

    if max(jolt) == 0:
        return 0

    c, j = find_presses([(x % 1) for x in jolt], buttons)
    count += c
    print('Before', jolt)
    jolt = [jolt[i] - j[i] for i in range(len(jolt))]
    print('After', jolt)
    count += 2 * find_presses2a([(x >> 1) for x in jolt], buttons)
    print(count)

    return count


def find_presses2(jolt, buttons):
    count = 0
    wave = [[0] * len(jolt)]

    while True:
        count += 1
        nextwave = []
        print(len(wave))

        for i in range(len(wave)):
            for j in range(len(buttons)):
                newjolt = press2(wave[i], buttons[j])
                jc = jcheck(jolt, newjolt)
                if jc == 2:
                    continue
                if jc == 1:
                    print(count)
                    print("-----")
                    return count
                nextwave.append(newjolt)
        wave = nextwave


def lintest(jolt, buttons):
    arrin = []
    res = [0] * len(jolt)

    for _ in range(len(jolt)):
        arrin.append([0] * len(buttons))

    for i in range(len(buttons)):
        for x in buttons[i]:
            arrin[x][i] = 1

    a = np.array(arrin, dtype=int)
    b = np.array(jolt)
    ai = np.linalg.pinv(a)
    bi = np.dot(ai, b)
    print(ai)
    print(bi)
    x = np.linalg.lstsq(a, b)
    print(x[0])
    for i in range(len(buttons)):
        for y in buttons[i]:
            res[y] += int(x[0][i])
    print(res)
    print(jolt)
    print('----')


def __main__():
    part1 = 0
    part2 = 0

    for line in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        target = [0 if x == '.' else 1 for x in line[1:].split(']')[0]]
        buttons = [[int(y) for y in x[1:-1].split(',')] for x in line.split('] ')[1].split(' ')[:-1]]
        jolt = [int(x) for x in line.split('{')[1][:-1].split(',')]
        c, _ = find_presses(target, buttons)
        part1 += c
        part2 += find_presses2a(jolt, buttons)
        lintest(jolt, buttons)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
