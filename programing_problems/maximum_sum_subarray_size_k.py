#!/usr/bin/env python3
"""
Given an array of integers and a number k, find maximum sum of a subarray of size k.

Examples :

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.
"""
from typing import List

def maximum_subarray_size_k(arr: List[int], k: int) -> int:
    if k > len(arr):
        return None

    total = 0
    current_sum = 0
    for i in range(k):
        current_sum += arr[i]

    total = current_sum
    # sliding window
    for i in range(1, len(arr)-k+1):
        current_sum -= arr[i-1]
        current_sum += arr[i + k - 1]
        if current_sum > total:
            total = current_sum

    print(total)
    return total



def main():
    assert maximum_subarray_size_k([100, 200, 300, 400], 2) == 700
    assert maximum_subarray_size_k([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39
    assert maximum_subarray_size_k([2, 3], 3) == None

if __name__ == "__main__":
    main()
