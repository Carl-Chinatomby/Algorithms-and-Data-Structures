#!/usr/bin/env python3
"""
You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

Example:

Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
Output: 5
Explanation: The missing number from 1 to 8 is 5

Input: arr[] = {1, 2, 3, 5}
Output: 4
Explanation: The missing number from 1 to 5 is 4
"""
from heapq import (
    heapify,
    heappush,
    heappop,
)
from typing import List


def find_missing_num(arr: List[int]) -> int:
    # merge intervals by splitting overlapping into separate intervals
    actual_sum = 0
    n = len(arr) + 1

    # this is by doing a loop
    # expected_sum = n + 1 # since we're missing 1 number this needs to be added
    # n = len(arr)
    # for i in range(n):
    #     expected_sum += i+1
    #     actual_sum += arr[i]

    expected_sum = (n*(n+1))//2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


def main():
    assert find_missing_num([1, 2, 4, 6, 3, 7, 8]) == 5
    assert find_missing_num([1, 2, 3, 5]) == 4

if __name__ == "__main__":
    main()
