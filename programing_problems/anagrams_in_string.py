#!/usr/bin/env python3
"""
Problem:
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""
from typing import List
from collections import defaultdict

def find_anagrams(s: str, p: str) -> List[int]:
    results = []
    # create a sliding window of len(p)
    # from left to right of window check if anagram, if yes, add index to results

    # delete if using set comparisons
    char_count = defaultdict(int)
    for char in p:
        char_count[char] += 1

    for i in range(len(s) - len(p) + 1):

        # This can all be simplifed to: (but maybe that's cheating?)
        #if set(s[i:i+len(p)]) == set(p):
        #    results.append(i)

        matches = True
        substr_count = defaultdict(int)
        for char in s[i:i+len(p)]:
            substr_count[char] += 1

        for key, val in char_count.items():
            if substr_count[key] != val:
                matches = False

        if matches:
            results.append(i)

    return results


def main():
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]
    assert find_anagrams("abab", "ab") == [0, 1, 2]


if __name__ == "__main__":
    main()
