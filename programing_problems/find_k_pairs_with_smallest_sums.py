#!/usr/bin/env python3
"""
Given two integer arrays arr1[] and arr2[] sorted in ascending order and an integer k. Find k pairs with smallest sums such that one element of a pair belongs to arr1[] and other element belongs to arr2[]

Examples:

Input :  arr1[] = {1, 7, 11}
         arr2[] = {2, 4, 6}
         k = 3
Output : [1, 2],
         [1, 4],
         [1, 6]
Explanation: The first 3 pairs are returned
from the sequence [1, 2], [1, 4], [1, 6],
[7, 2], [7, 4], [11, 2], [7, 6], [11, 4],
[11, 6]
"""
from heapq import (
    heapify,
    heappush,
    heappop,
)
from typing import (
    List,
    Tuple,
)

def get_k_pairs_smallest_sums(arr1: List[int], arr2: List[int], k: int) -> List[Tuple[int, int]]:
    first = sorted(arr1)
    second = sorted(arr2)
    min_heap = []
    heapify(min_heap)

    pairs = []
    min_heap = [(first[0] + second[0], 0, 0)] # total, i, j
    added_indexes = set()
    heapify(min_heap)
    while k and min_heap:
        k -= 1
        total, i, j = heappop(min_heap)
        pairs.append((first[i], second[j]))


        if i+1 < len(first) and (i+1, j) not in added_indexes:
            heappush(min_heap, (first[i+1] + second[j], i+1, j))
            added_indexes.add((i+1, j))

        if j+1 < len(second) and (i, j+1) not in added_indexes:
            heappush(min_heap, (first[i] + second[j+1], i, j+1))
            added_indexes.add((i, j+1))

    return pairs



def main():
    arr1 = [1,3,11]
    arr2 = [2,4,8]
    assert get_k_pairs_smallest_sums(arr1, arr2, 4) == [(1, 2), (1, 4), (3, 2), (3, 4)]


if __name__ == "__main__":
    main()
