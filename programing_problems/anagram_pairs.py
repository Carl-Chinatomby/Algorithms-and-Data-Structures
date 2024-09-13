#!/usr/bin/env python3
"""
Problem:
https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem
"""
import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    # abab
    anagram_cnt = defaultdict(int)

    # create a map of all possible substrings (we sort so that anagrams are always ordered the same)
    for i in range(len(s)):
        sbstr = ''

        for j in range(i, len(s)):
            sbstr = ''.join(sorted(sbstr + s[j])) # 'a'
            anagram_cnt[sbstr] += 1

    # We can count the pairs of k anagrammatic occurrences of a string with the formula: k*(k-1)/2
    total_anagrams = 0
    for k, v in anagram_cnt.items():
        total_anagrams += (v*(v-1))//2

    return total_anagrams

if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.txt')
    fptr = open(output_path, 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

