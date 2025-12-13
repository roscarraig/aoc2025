#!/usr/bin/env python3
""" Advent of code day 10 """

import sys
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
    presses = [-1]

    while True:
        count += 1
        nextwave = []
        nextpress = []

        for i in range(len(wave)):
            for j in range(presses[i] + 1, len(buttons)):
                newtarget = press(wave[i], buttons[j])
                if sum(newtarget) == 0:
                    return count
                nextwave.append(newtarget)
                nextpress.append(j)
        wave = nextwave
        presses = nextpress


def find_presses2(target, jolt, buttons):
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


def __main__():
    part1 = 0
    part2 = 0

    for line in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        target = [0 if x == '.' else 1 for x in line[1:].split(']')[0]]
        buttons = [[int(y) for y in x[1:-1].split(',')] for x in line.split('] ')[1].split(' ')[:-1]]
        jolt = [int(x) for x in line.split('{')[1][:-1].split(',')]
        part1 += find_presses(target, buttons)
        part2 += find_presses2(target, jolt, buttons)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
