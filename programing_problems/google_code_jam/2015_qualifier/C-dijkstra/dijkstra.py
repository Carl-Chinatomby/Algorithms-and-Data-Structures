#!/usr/bin/env python3
"""
Problem

The Dutch computer scientist Edsger Dijkstra made many important contributions to the field, including the shortest path finding algorithm that bears his name. This problem is not about that algorithm.

You were marked down one point on an algorithms exam for misspelling "Dijkstra" -- between D and stra, you wrote some number of characters, each of which was either i, j, or k. You are prepared to argue to get your point back using quaternions, an actual number system (extended from complex numbers) with the following multiplicative structure:



To multiply one quaternion by another, look at the row for the first quaternion and the column for the second quaternion. For example, to multiply i by j, look in the row for i and the column for j to find that the answer is k. To multiply j by i, look in the row for j and the column for i to find that the answer is -k.

As you can see from the above examples, the quaternions are not commutative -- that is, there are some a and b for which a * b != b * a. However they are associative -- for any a, b, and c, it's true that a * (b * c) = (a * b) * c.

Negative signs before quaternions work as they normally do -- for any quaternions a and b, it's true that -a * -b = a * b, and -a * b = a * -b = -(a * b).

You want to argue that your misspelling was equivalent to the correct spelling ijk by showing that you can split your string of is, js, and ks in two places, forming three substrings, such that the leftmost substring reduces (under quaternion multiplication) to i, the middle substring reduces to j, and the right substring reduces to k. (For example, jij would be interpreted as j * i * j; j * i is -k, and -k * j is i, so jij reduces to i.) If this is possible, you will get your point back. Can you find a way to do it?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with two space-separated integers L and X, followed by another line with L characters, all of which are i, j, or k. Note that the string never contains negative signs, 1s, or any other characters. The string that you are to evaluate is the given string of L characters repeated X times. For instance, for L = 4, X = 3, and the given string kiij, your input string would be kiijkiijkiij.

Output

For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is either YES or NO, depending on whether the string can be broken into three parts that reduce to i, j, and k, in that order, as described above.

Limits

1 ≤ T ≤ 100.
1 ≤ L ≤ 10000.
Small dataset

1 ≤ X ≤ 10000.
1 ≤ L * X ≤ 10000.
Large dataset

1 ≤ X ≤ 1012.
1 ≤ L * X ≤ 1016.
Sample


Input

Output

5
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i

Case #1: NO
Case #2: YES
Case #3: NO
Case #4: YES
Case #5: NO
In Case #1, the string is too short to be split into three substrings.

In Case #2, just split the string into i, j, and k.

In Case #3, the only way to split the string into three parts is k, j, i, and this does not satisfy the conditions.

In Case #4, the string is jijijijijiji. It can be split into jij (which reduces to i), iji (which reduces to j), and jijiji (which reduces to k).

In Case #5, no matter how you choose your substrings, none of them can ever reduce to a j or a k.
"""
import argparse
from itertools import repeat


NO = 'NO'
YES = 'YES'


def reduce_string(input_string):
    reduce_table = {
        '1': {
            '1': '1',
            'i': 'i',
            'j': 'j',
            'k': 'k',
        },
        'i': {
            '1': 'i',
            'i': '-1',
            'j': 'k',
            'k': '-j',
        },
        'j': {
            '1': 'j',
            'i': '-k',
            'j': '-1',
            'k': 'i',
        },
        'k': {
            '1': 'k',
            'i': 'j',
            'j': '-i',
            'k': '-1',
        },
    }

    value = '1'
    for char in input_string:
        if value[0] == '-':
            res = reduce_table[value[-1]][char]
            value = res[-1] if res[0] == '-' else '-' + res
        else:
            value = reduce_table[value][char]

    return value


def is_string_reducable(input_string, reps):
    """Returns NO or YES if string is reducable to
    i, j or k based on rules specified in module docstring.
    """
    # reps of 4 of the same thing equal 1 (large problem trick)
    if not reps % 4:  # this always equals 1
        return NO
    elif reps > 4:  # min need to for the first 2 splits
        reps = 4 + reps % 4

    # get rid of some base cases
    if len(input_string) * reps < 3 or \
            (len(input_string) * reps == 3 and input_string != 'ijk'):
        return NO

    if len([c for c in ('i', 'j', 'k') if c in input_string]) < 2:
        return NO

    # calculate value: if not -1 fail (i*j*k == -1)
    value = reduce_string(input_string)
    if not reps % 2:
        # negative value, repeated twice is cancels each other out
        if value[0] == '-':
            value = reduce_string(value[-1] * 2)
        else:
            value = reduce_string(value * 2)
    else:
        if value[0] == '-':
            res = reduce_string(value[-1] * 2)
            value = res[-1] if res[0] == '-' else '-' + res

    if value != '-1':
        return NO

    # reduce value matches, check order
    # Ok it reduces to -1, can it be split 3 ways for i, j, k?
    desired_value = 'i'
    value = '1'
    chars_remaining = len(input_string) * reps
    for strset in repeat(input_string, times=reps):
        for char in strset:
            chars_remaining -= 1
            if value[0] != '-':
                value = reduce_string(value + char)
            else:
                res = reduce_string(value[-1] + char)
                value = res[-1] if res[0] == '-' else '-' + res

            if value == desired_value:
                value = '1'
                if desired_value == 'i':
                    desired_value = 'j'
                elif desired_value == 'j':
                    desired_value = 'k'
                else:  # ijk found, the rest needs to equal 1
                    desired_value = '1'
                    value = '1'

    if value != '1':
        return NO

    return YES


def main(filepath):
    outfile_name = filepath.replace('.in', '.out') if '.in' in filepath \
        else filepath + '.out'
    with open(filepath) as infile, open(outfile_name, 'w') as outfile:
        num_of_test_cases = int(infile.readline().strip())
        for i in range(1, num_of_test_cases+1):
            row = infile.readline().strip().split()
            word_len = int(row[0])
            reps = int(row[1])
            word = infile.readline().strip()
            if len(word) != word_len:
                raise Exception(
                    'Incorrect input file, {} != {} on test case: {}'.format(
                        word_len,
                        len(word),
                        i
                    )
                )
            output = is_string_reducable(word, reps)
            outfile.write('Case #{}: {}\n'.format(i, output))

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", help="Filepah to the input filename")
    args = parser.parse_args()

    main(filepath=args.infile)
