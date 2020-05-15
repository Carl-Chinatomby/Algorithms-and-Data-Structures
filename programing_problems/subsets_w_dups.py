#!/usr/bin/env python3
"""
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
import collections
from typing import List


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    subsets = []

    subsets_total= 2**len(nums) # 2^n is subset size with duplicates

    for i in range(subsets_total):
        subset = []
        for j in range(len(nums)):
            #seet if the jth bit is true, if so add that element to to subset
            if (i & (1 << j)) > 0:
              subset.append(nums[j])

        if subset not in subsets:
            subsets.append(subset)
    return subsets



def subsets_with_dup_dict(nums: List[int]) -> List[List[int]]:
    subsets = [[]]
    for num, freq in collections.Counter(nums).items():
        current_subset_size = len(subsets)
        for reps in range(1, freq+1):
            for subset in subsets[:current_subset_size]: # we need subsets to be copied as a temp list
                subsets.append(subset + [num] * reps)
    return subsets


def main():
    assert sorted(subsets_with_dup([1,2,2])) == sorted([[2], [1], [1,2,2], [2,2], [1,2], []])
    assert sorted(subsets_with_dup_dict([1,2,2])) == sorted([[2], [1], [1,2,2], [2,2], [1,2], []])


if __name__ == "__main__":
    main()
