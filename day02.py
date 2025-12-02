#!/usr/bin/env

import aoc
import sys


def invalid(code):
    codes = str(code)
    l = len(codes)
    for i in range(2, l + 1):
        if l % i > 0:
            continue
        step = int(l / i)
        if codes == codes[:step]*i:
            return i
    return 0

def __main__():
    part1 = 0
    part2 = 0
    for item in aoc.read_file(sys.argv[1]).strip().split(','):
        a, b = item.split('-')
        for code in range(int(a), int(b) + 1):
            check = invalid(code)
            if check == 2:
                part1 += code
            if check > 0:
                part2 += code

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
