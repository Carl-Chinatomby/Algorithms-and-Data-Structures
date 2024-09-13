#!/usr/bin/env python3
"""
Given an N * N matrix where each row and column is sorted in ascending order, find the K-th smallest element in the matrix.
"""
from typing import List


def find_kth_smallest(matrix: List[List[int]], num: int) -> int:
    n = len(matrix)
    start = matrix[0][0]
    end = matrix[-1][-1]

    while start < end:
        mid = start + (end-start)//2  # a number in the middle (may not be an element)

        # we want the count of numbers less than or equal to middle number
        # we want the smallest greater than middle number
        # we want the largest number less than or equal middle number
        count = 0
        val_before, val_after = start, end
        row, col = n-1, 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                if matrix[row][col] < val_after:
                    val_after = matrix[row][col]
                row -= 1
            else:
                if matrix[row][col] > val_before:
                    val_before = matrix[row][col]
                count += row + 1
                col += 1

        if count == num:
            return val_before
        elif count < num:
            start = val_after # search higher
        else:
            end = val_before # search lower

    return start

def main():
    print(find_kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5))
    assert find_kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5) == 7

if __name__ == "__main__":
    main()
