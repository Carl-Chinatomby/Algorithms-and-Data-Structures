#!/usr/bin/env python3
"""
Problem:
Find all triplets with zero sum
Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.

Examples :

Input : arr[] = {0, -1, 2, -3, 1}
Output : (0 -1 1), (2 -3 1)

Explanation : The triplets with zero sum are
0 + -1 + 1 = 0 and 2 + -3 + 1 = 0

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
Explanation : The triplets with zero sum is
1 + -2 + 1 = 0
"""
from typing import (
    List,
    Tuple,
)

def find_triplets_sum_zero(arr: List[int]) -> List[Tuple[int, int, int]]:
    results = []

    for i in range (0, len(arr) - 1):
        vals = {}
        for j in range(i + 1, len(arr)):
            missing_val = vals.get((arr[i] + arr[j]) * -1)
            if isinstance(missing_val, int):
                results.append((arr[i], missing_val, arr[j]))
            else:
                vals[arr[j]] = arr[j]

    return results


def main():
    assert find_triplets_sum_zero([0, -1, 2, -3, 1]) == [(0, -1, 1), (2, -3, 1)]
    assert find_triplets_sum_zero([1, -2, 1, 0, 5]) == [(1, -2, 1)]


if __name__ == "__main__":
    main()
