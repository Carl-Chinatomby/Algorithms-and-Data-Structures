#!/usr/bin/env python3
"""
Problem:
You are given an unsorted array with both positive and negative elements. You have to find the smallest positive number missing from the array in O(n) time using constant extra space. You can modify the original array.

Examples

 Input:  {2, 3, 7, 6, 8, -1, -10, 15}
 Output: 1

 Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
 Output: 4

 Input: {1, 1, 0, -1, -2}
 Output: 2
"""
from typing import List

def find_min_missing_pos_number(arr: List[int]) -> int:
    result = 0

    # move all non-postive numbers to the left and ignore them
    j = 0
    for i in range(len(arr)):
        if arr[i] <=0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    start = j
    pos_size = len(arr) - start

    # mark each index as visited by negating it now
    for i in range(start, len(arr)):
        check_idx = start + abs(arr[i]) - 1
        if check_idx < len(arr) and arr[check_idx] > 0:
            arr[check_idx] = -1 * arr[check_idx]

    # check for missing #
    for i in range(start, len(arr)):
        if arr[i] > 0:
            return i - start + 1

    return pos_size + 1 # no positive gaps so the next number is missing



def main():
    #print(find_min_missing_pos_number([2, 3, -7, 6, 8, 1, -10, 15]))
    assert find_min_missing_pos_number([2, 3, 7, 6, 8, -1, -10, 15]) == 1
    assert find_min_missing_pos_number([2, 3, -7, 6, 8, 1, -10, 15]) == 4
    assert find_min_missing_pos_number([1, 1, 0, -1, -2]) == 2
    assert find_min_missing_pos_number([2, 1, 0, -1, -2]) == 3

if __name__ == "__main__":
    main()
