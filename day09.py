#!/usr/bin/env python3
""" Advent of code day 9 """

import sys
import aoc


def dist(a, b):
    """ Calcuate rectangle area """
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def pdir(a, b):
    """ Work out the direction of travel """
    if b[0] > a[0]:
        return 0
    if b[1] > a[1]:
        return 1
    if a[0] > b[0]:
        return 2
    if a[1] > b[1]:
        return 3
    return 0


def turn(a, b):
    if a == 0 and b == 3:
        return -1
    if b == 0 and a == 3:
        return 1
    if b < a:
        return -1
    return 1


def corner(tiles, p):
    """ Determine the orientation of a corner """

    result = 0
    n = len(tiles)
    a = tiles[(p - 1) % n]
    b = tiles[p]
    c = tiles[(p + 1) % n]

    if a[0] == b[0] and b[1] > a[1] and c[0] < b[0]:
        result = 0
    elif a[0] == b[0] and b[1] > a[1] and c[0] > b[0]:
        result = 5
    elif a[0] == b[0] and b[1] < a[1] and c[0] < b[0]:
        result = 6
    elif a[0] == b[0] and b[1] < a[1] and c[0] > b[0]:
        result = 3
    elif a[1] == b[1] and b[0] > a[0] and c[1] > b[1]:
        result = 2
    elif a[1] == b[1] and b[0] > a[0] and c[1] < b[1]:
        result = 4
    elif a[1] == b[1] and b[0] < a[0] and c[1] > b[1]:
        result = 7
    elif a[1] == b[1] and b[0] < a[0] and c[1] < b[1]:
        result = 1

    return result


def isopposite(tiles, corners, i, j):
    """ Have validated that the data set is moving clockwise """

    if tiles[i][0] < tiles[j][0]:
        a = i
        b = j
    else:
        a = j
        b = i

    n = len(tiles)
    ac = corners[a]
    bc = corners[b]

    if tiles[b][1] > tiles[a][1]:
        if bc in [1, 2, 3, 4]:
            return False
        if ac in [0, 1, 2, 7]:
            return False
    else:
        if bc in [0, 1, 3, 6]:
            return False
        if ac in [0, 2, 3, 5]:
            return False

    return True


def inside(tiles, a, b, c):
    a0 = tiles[a][0]
    a1 = tiles[a][1]
    b0 = tiles[b][0]
    b1 = tiles[b][1]
    c0 = tiles[c][0]
    c1 = tiles[c][1]
    n = len(tiles)
    d0 = tiles[(c + 1) % n][0]
    d1 = tiles[(c + 1) % n][1]

    if c0 < min(a0, b0) or c0 > max(a0, b0) or c1 < min(a1, b1) or c1 > max(a1, b1):
        return False

    if c0 > min(a0, b0) and c0 < max(a0, b0) and c1 > min(a1, b1) and c1 < max(a1, b1):
        return True

    if c0 in [min(a0, b0), max(a0, b0)] and c1 in [min(a1, b1), max(a1, b1)]:
        return False

    if c0 == min(a0, b0) and tiles[(c + 1)%n][0] > c0:
        return True
    if c0 == min(a0, b0) and tiles[(c - 1)%n][0] > c0:
        return True
    if c0 == max(a0, b0) and tiles[(c + 1)%n][0] < c0:
        return True
    if c0 == max(a0, b0) and tiles[(c - 1)%n][0] < c0:
        return True

    if c1 == min(a1, b1) and tiles[(c + 1)%n][1] > c1:
        return True
    if c1 == min(a1, b1) and tiles[(c - 1)%n][1] > c1:
        return True
    if c1 == max(a1, b1) and tiles[(c + 1)%n][1] < c1:
        return True
    if c1 == max(a1, b1) and tiles[(c - 1)%n][1] < c1:
        return True

    return False


def crosses(a, b, c, d):
    x0 = min(a[0], b[0])
    x1 = max(a[0], b[0])
    y0 = min(a[1], b[1])
    y1 = max(a[1], b[1])

    if c[0] == d[0] and c[0] > x0 and c[0] < x1:
        if min(c[1], d[1]) < y0 and max(c[1], d[1]) > y1:
            return True

    if c[1] == d[1] and c[1] > y0 and c[1] < y1:
        if min(c[0], d[0]) < x0 and max(c[0], d[0]) > x1:
            return True

    return False


def __main__():
    part1 = 0
    part2 = 0
    tiles = []
    areas = []
    corners = []
    pointed = -1
    turns = 0

    for point in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        newtile = [int(x) for x in point.split(',')]
        for tile in tiles:
            areas.append(dist(tile, newtile))
        if len(tiles) > 0:
            tile = tiles[-1]
            newdir = pdir(tile, newtile)
            if pointed < 0:
                pointed = newdir
            else:
                turns += turn(pointed, newdir)
                pointed = newdir
        tiles.append(newtile)

    part1 = max(areas)

    print(f"Part 1: {part1}")
    n = len(tiles)

    areas = []
    for i in range(len(tiles)):
        corners.append(corner(tiles, i))

    for i in range(1, len(tiles)):
        for j in range(i):
            if isopposite(tiles, corners, i, j):
                area = dist(tiles[i], tiles[j])
                if area > part2:
                    for k in range(len(tiles)):
                        if k in [i, j]:
                            continue
                        if inside(tiles, i, j, k):
                            area = 0
                            break
                        if crosses(tiles[i], tiles[j], tiles[k], tiles[(k + 1) % n]):
                            area = 0
                            break
                if area > part2:
                    part2 = area

    print(f"Part 2: {part2}")


if __name__ == '__main__':
    __main__()
