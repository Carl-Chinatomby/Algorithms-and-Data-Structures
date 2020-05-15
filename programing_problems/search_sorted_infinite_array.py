#!/usr/bin/env python3
"""
Suppose you have a sorted array of infinite numbers, how would you search an element in the array?
"""
from typing import List


def binary_search(arr: List[int], low_idx: int, high_idx: int, num: int) -> int:
    if high_idx >= low_idx:
        mid_idx = low_idx + ((high_idx - low_idx)//2)

        if arr[mid_idx] == num:
            return mid_idx
        elif arr[mid_idx] > num:
            return binary_search(arr, low_idx, mid_idx-1, num)
        else:
            return binary_search(arr, mid_idx+1, high_idx, num)

    return None



def find_pos(arr: List[int], num: int) -> int:
    low_idx = 0
    high_idx = 1
    val = arr[low_idx]

    # find the low and the high indexes where our value must exist
    while val < num:
        low_idx = high_idx
        high_idx *= 2
        val = arr[high_idx]


    # do a binary search in between those indexes
    return binary_search(arr, low_idx, high_idx, num)

def main():
    assert find_pos([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170], 10) == 4

if __name__ == "__main__":
    main()
