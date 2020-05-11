#!/usr/bin/env python3
"""
Problem:
https://leetcode.com/problems/find-median-from-data-stream/
"""
from heapq import (
    heapify,
    heappush,
    heappop,
)
from typing import List


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        heapify(self.min_heap)
        self.max_heap = []
        heapify(self.max_heap)

    def top_min(self):
        return self.min_heap[0]

    def top_max(self):
        return -1 * self.max_heap[0] # we negated values to turn a min_heap into a max heap

    def push_max(self, val):
        # negate val so that the sort is a max heap
        heappush(self.max_heap, float(-1 * val))

    def push_min(self, val):
        heappush(self.min_heap, float(val))

    def pop_min(self):
        x = self.top_min()
        heappop(self.min_heap)
        return x

    def pop_max(self):
        # we avoid return the normalized top_max value which already considers negations
        x = self.top_max()
        heappop(self.max_heap)
        return x

    def add_num(self, num: int) -> None:
        if not len(self.max_heap) and not len(self.min_heap):
            self.push_max(num)
        # elif len(self.max_heap) == 1 and not len(self.min_heap):
        #     if num > self.top_max():
        #         self.push_min(num)
        #     else:
        #         new_min = self.pop_max()
        #         self.push_max(num)
        #         self.push_min(new_min)
        else:
            if num < self.top_max():
                self.push_max(num)
            else:
                self.push_min(num)

        # balance the heaps to each other (heapq will handle the heaps internally)
        if len(self.max_heap) - len(self.min_heap) > 1:
            new_min = self.pop_max()
            self.push_min(new_min)
        elif len(self.min_heap) > len(self.max_heap):
            new_max = self.pop_min()
            self.push_max(new_max)

    def find_median(self) -> float:
        if len(self.max_heap) == 0 and len(self.min_heap) == 0:
            return None
        elif len(self.max_heap) > len(self.min_heap):
            return self.top_max()
        elif len(self.max_heap) < len(self.min_heap):
            return self.top_min()
        else: # len(self.max_heap) == len(self.min_heap)
            return (self.top_max() + self.top_min())/2


def main():
    mf = MedianFinder()
    mf.add_num(2)
    mf.add_num(3)
    assert mf.find_median() == 2.5
    mf.add_num(4)
    assert mf.find_median() == 3


if __name__ == "__main__":
    main()
