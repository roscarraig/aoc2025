#!/usr/bin/env python3
""" Advent of code day 10 """

import sys
import aoc


def trace(routes, start, cache, target="out", seen=[]):
    result = []

    if start in seen:
        print("Loop")
        return []

    if start in cache:
        return cache[start]

    if start == target:
        return ["out"]

    for item in routes[start]:
        for res in trace(routes, item, cache, target, seen + [start]):
            result.append(start + ' ' + res)

    cache[start] = result
    return result


def __main__():
    part1 = 0
    part2 = 0
    routes = {"out": []}
    cache = {}

    for line in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        src, dest = line.split(': ')
        routes[src] = dest.split(' ')

    if "you" in routes:
        part1 = len(trace(routes, "you", cache))

    print(f"Part 1: {part1}")

    dfcount = 0
    dacout = trace(routes, "dac", cache)

    for item in dacout:
        if "fft" in item:
            dfcount += 1

    if dfcount == 0:
        fftdac = trace(routes, "fft", {}, "dac")
        svrfft = trace(routes, "svr", {}, "fft")
        part2 = len(svrfft) * len(fftdac) * len(dacout)
    else:
        svrdac = trace(routes, "svr", {}, "dac")
        part2 = len(svrdac) * dfcount

    # part2 = len([x for x in trace(routes, "svr", cache) if 'dac' in x and 'fft' in x])

    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
