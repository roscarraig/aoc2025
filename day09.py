#!/usr/bin/env python3
""" Advent of code day 8 """

import sys
import aoc


def dist(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


def dir(a, b):
    if b[0] > a[0]:
        return 0
    if b[1] > a[1]:
        return 1
    if a[0] > b[0]:
        return 2
    if a[1] > b[1]:
        return 3
    print("This should not happen")
    return 0


def turn(a, b):
    if a == 0 and b == 3:
        return -1
    if b == 0 and a == 3:
        return 1
    if b < a:
        return -1
    return 1

def isopposite(tiles, dirs, a, b):
    """ Have validated that the data set is moving clockwise """

    return True
    if tiles[a][0] > tiles[b][0]:
        if dirs[a] == 3 or dirs[b] == 1:
            return False
        
    if tiles[a][0] < tiles[b][0]:
        if dirs[a] == 1 or dirs[b] == 3:
            return False

    if tiles[a][1] > tiles[b][1]:
        if dirs[a] == 0 or dirs[b] == 2:
            return False
        
    if tiles[a][1] < tiles[b][1]:
        if dirs[a] == 2 or dirs[b] == 0:
            return False

    return True


def inside(tiles, a, b, c):
    if tiles[c][0] <= min(tiles[a][0], tiles[b][0]):
        return False
    if tiles[c][0] >= max(tiles[a][0], tiles[b][0]):
        return False
    if tiles[c][1] <= min(tiles[a][1], tiles[b][1]):
        return False
    if tiles[c][1] >= max(tiles[a][1], tiles[b][1]):
        return False

    return True


def __main__():
    part1 = 0
    part2 = 0
    tiles = []
    areas = []
    dirs = [-1]
    pointed = -1
    turns = 0

    for point in aoc.read_file(sys.argv[1]).strip('\n').split("\n"):
        newtile = [int(x) for x in point.split(',')]
        for tile in tiles:
            areas.append(dist(tile, newtile))
        if len(tiles) > 0:
            tile = tiles[-1]
            newdir = dir(tile, newtile)
            if pointed < 0:
                pointed = newdir
                dirs.append(-1)
            else:
                turns += turn(pointed, newdir)
                pointed = newdir
                dirs.append(newdir)
            print(newtile, tile, pointed, turns)
        tiles.append(newtile)
    dirs[0] = newdir

    print(turns)
    part1 = max(areas)

    print(f"Part 1: {part1}")

    areas = []
    print

    for i in range(1, len(tiles)):
        for j in range(i):
            if (i - j) % 2 != 0:
                continue
            if isopposite(tiles, dirs, i, j):
                area = dist(tiles[i], tiles[j])
                if area > part2:
                    for k in range(len(tiles)):
                        if k in [i, j]:
                            continue
                        if inside(tiles, i, j, k):
                            area = 0
                            break
                if area > part2:
                    print(area, tiles[i], tiles[j])
                    part2 = area

    print(f"Part 2: {part2}")
    # 4600181596 High


if __name__ == '__main__':
    __main__()
