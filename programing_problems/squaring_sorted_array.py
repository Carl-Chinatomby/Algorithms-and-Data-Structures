#!/usr/bin/env python3
"""
https://leetcode.com/problems/squares-of-a-sorted-array/
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""
from collections import deque
from typing import List


def sorted_squares(arr: List[int]) -> List[int]:
    #return sorted(x*x for x in arr)

    answer = deque()
    l, r = 0, len(arr) - 1
    while l <= r:
        left, right = arr[l]*arr[l], arr[r]*arr[r]
        if left > right:
            answer.appendleft(left)
            l += 1
        else:
            answer.appendleft(right)
            r -= 1
    return list(answer)


def main():
    assert sorted_squares([-4,-1,0,3,10]) == [0,1,9,16,100]
    assert sorted_squares([-7,-3,2,3,11]) == [4,9,9,49,121]


if __name__ == "__main__":
    main()
