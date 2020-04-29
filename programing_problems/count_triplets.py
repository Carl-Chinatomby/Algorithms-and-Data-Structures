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
    x_lets = 3
    #build val->list(indexes)
    val_indexes = {}
    for idx, val in enumerate(arr):
        if val_indexes.get(val):
            val_indexes[val].append(idx)
        else:
            val_indexes[val] = [idx]

    current_cnt = 0
    # check indexes for triplets
    for idx, val in enumerate(arr):
        xlet_vals = []
        for i in range(1, x_lets):
            xlet_vals.append(val * (r ** i))

        possible_counts = 1
        for xval in xlet_vals:

            possible_counts *= len(val_indexes.get(xval, []))
            for validx in val_indexes.get(xval, []):
                if idx > validx:
                    possible_counts -= 1

        current_cnt += possible_counts

    return current_cnt




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
