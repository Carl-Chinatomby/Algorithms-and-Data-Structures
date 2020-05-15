#!/usr/bin/env python3
"""
k largest(or smallest) elements in an array
Question: Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.
For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.
"""
from collections import defaultdict
from heapq import (
    heapify,
    heappush,
    heappop,
    heapreplace,
    heappushpop,
)


def get_top_k(arr, k):
    min_heap = []
    heapify(min_heap)
    # loop through the hash and add values to the heap, until size of heap > k
    heap_size = 0
    for num in arr:
        # once size of heap is =k, we're doing a  pushpop if the root of heap is < current value
        if heap_size < k:
            heappush(min_heap, num)
            heap_size += 1
        elif min_heap[0] < num:
            heappushpop(min_heap, num)

    # return the heap, various sorting options or manips can be done here
    return sorted(min_heap, reverse=True)



def main():
    assert get_top_k([1, 23, 12, 9, 30, 2, 50], 3) == [50, 30, 23]


if __name__ == "__main__":
    main()
