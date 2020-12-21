#!/usr/bin/env python3
"""
Given a sorted array of numbers, find out if a given number key is present in the array.
Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
You should assume that the array can have duplicates.
Write a function to return the index of the key if it is present in the array, otherwise return -1.
Example-1: Input: [1, 2, 3, 4, 5, 6, 7], key = 5, Output: 4
Example-2: Input: [10, 6, 4], key = 10, Output: 0"""
from typing import List


def binary_search(arr: List[int], low_idx: int, high_idx: int, num: int) -> int:
    if high_idx >= low_idx:
        mid_idx = low_idx + ((high_idx - low_idx)//2)
        is_ascending = arr[low_idx] <= arr[high_idx]
        if arr[mid_idx] == num:
            return mid_idx

        if is_ascending:
            if arr[mid_idx] > num:
                return binary_search(arr, low_idx, mid_idx-1, num)
            else:
                return binary_search(arr, mid_idx+1, high_idx, num)
        else:
            if arr[mid_idx] > num:
                return binary_search(arr, mid_idx+1, high_idx-1, num)
            else:
                return binary_search(arr, low_idx, mid_idx, num)

    return None


def find_pos(arr: List[int], num: int) -> int:
    low_idx = 0
    high_idx = len(arr) - 1

    return binary_search(arr, low_idx, high_idx, num)


def main():
    assert find_pos([1, 2, 3, 4, 5, 6, 7], 5) == 4
    assert find_pos([10, 6, 4], 10) == 0


if __name__ == "__main__":
    main()
