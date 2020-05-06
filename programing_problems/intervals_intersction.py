#!/usr/bin/env python3
"""
Problem:
https://leetcode.com/problems/interval-list-intersections/
"""
from typing import List


def interval_intersection(a: List[int], b:List[int]) -> List[int]:
    first = sorted(a)
    second = sorted(b)
    intervals = []

    i, j = 0, 0
    while i < len(first) and j < len(second):
        start = max(first[i][0], second[j][0])
        end = min(first[i][1], second[j][1])

        if start <= end: # they overlap
            intervals.append([start, end])

        if first[i][1] < second[j][1]:
            i += 1
        else:
            j += 1

    return intervals


def main():
    a = [[0,2],[5,10],[13,23],[24,25]]
    b = [[1,5],[8,12],[15,24],[25,26]]
    print(interval_intersection(a, b))
    assert interval_intersection(a, b) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

if __name__ == "__main__":
    main()
