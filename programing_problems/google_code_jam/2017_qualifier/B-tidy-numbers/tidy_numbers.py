#!/usr/bin/env python3
"""
Problem

Tatiana likes to keep things tidy. Her toys are sorted from smallest to largest, her pencils are sorted from shortest to longest and her computers from oldest to newest. One day, when practicing her counting skills, she noticed that some integers, when written in base 10 with no leading zeroes, have their digits sorted in non-decreasing order. Some examples of this are 8, 123, 555, and 224488. She decided to call these numbers tidy. Numbers that do not have this property, like 20, 321, 495 and 999990, are not tidy.

She just finished counting all positive integers in ascending order from 1 to N. What was the last tidy number she counted?

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with a single integer N, the last number counted by Tatiana.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the last tidy number counted by Tatiana.

Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ N ≤ 1000.
Large dataset

1 ≤ N ≤ 1018.
Sample


Input

Output

4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

Note that the last sample case would not appear in the Small dataset.
"""
import argparse


def get_largest_tidy_number(number):
    num_chars = list(str(number))

    borrow = False
    for i, c in enumerate(num_chars): # Move forward
        if i > 0 and c < num_chars[i-1]: #if there's a prev # and current elem is smaller
            for j in range(i, -1, -1): # move backward and update previous
                subtract_previous = False
                if num_chars[j] > '0': # we can just subtract 1 lower
                    new_digit = str(ord(num_chars[j]) - ord('1'))
                    num_chars[j] = new_digit
                    if j and num_chars[j-1] > num_chars[j]:
                        num_chars[j] = '9'
                        subtract_previous = not borrow
                    else:
                        borrow = not borrow
                else:
                    # we need to roll over from 9 and borrow from the previous numbers
                    # this requires us to rollback and ensure the previous numbers
                    # are still ascending
                    num_chars[j] = '9'
                    # only decrement if we didn't borrow from the previous iterations
                    subtract_previous = not borrow

                if not subtract_previous:
                    break

    return int("".join(num_chars))


def main(filepath):
    with open(filepath) as infile:
        num_of_test_cases = int(infile.readline().strip())
        outfile_name = filepath.replace('.in', '.out') if '.in' in filepath \
            else filepath + '.out'

        with open(outfile_name, 'w') as outfile:
            for i in range(1, num_of_test_cases + 1):
                input_num = int(infile.readline().strip())
                output = get_largest_tidy_number(input_num)
                outfile.write('Case #{}: {}\n'.format(i, output))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", help="Filepath to the input filename")
    args = parser.parse_args()

    main(filepath=args.infile)
