#!/usr/bin/env python3
"""
Problem:
https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""


import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def count_triplets(arr, r):
    pass


if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH', 'output.txt')
    fptr = open(output_path, 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = count_triplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
