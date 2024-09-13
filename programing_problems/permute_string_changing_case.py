#!/usr/bin/env python3
"""
Print all permutations of a string keeping the sequence but changing cases.

Examples:

Input : ab
Output : AB Ab ab aB

Input : ABC
Output : abc Abc aBc ABc abC AbC aBC ABC
"""
from typing import List


def case_permute(input_str: str) -> List[str]:
    permuations = []
    max_permutations = 2**len(input_str) # 1 << n  equivalent
    input_str = input_str.lower()

    for i in range(max_permutations):
        chars = [c for c in input_str]

        for j in range(len(input_str)):
            # if we're at the combination for this bit switch, let's capitalize according to the unique # value
            # abc = 000, Abc == 100
            # if jth bit is set, we are uppercasing
            if (i // (2**j)) & 1 == 1: # (((i >> j) & 1) == 1), equivalent
                chars[j] = input_str[j].upper()

        current_permutation = ''.join(chars)
        permuations.append(current_permutation)

    print(permuations)
    return permuations


def main():
    assert case_permute('ab') == ['ab', 'Ab', 'aB', 'AB']
    assert case_permute('ABC') == ['abc', 'Abc', 'aBc', 'ABc', 'abC', 'AbC', 'aBC', 'ABC']

if __name__ == "__main__":
    main()
