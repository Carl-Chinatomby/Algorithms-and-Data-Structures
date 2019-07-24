#!/usr/bin/env python3
"""
Problem

A jamcoin is a string of N ≥ 2 digits with the following properties:

Every digit is either 0 or 1.
The first digit is 1 and the last digit is 1.
If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.
Not every string of 0s and 1s is a jamcoin. For example, 101 is not a jamcoin; its interpretation in base 2 is 5, which is prime. But the string 1001 is a jamcoin: in bases 2 through 10, its interpretation is 9, 28, 65, 126, 217, 344, 513, 730, and 1001, respectively, and none of those is prime.

We hear that there may be communities that use jamcoins as a form of currency. When sending someone a jamcoin, it is polite to prove that the jamcoin is legitimate by including a nontrivial divisor of that jamcoin's interpretation in each base from 2 to 10. (A nontrivial divisor for a positive integer K is some positive integer other than 1 or K that evenly divides K.) For convenience, these divisors must be expressed in base 10.

For example, for the jamcoin 1001 mentioned above, a possible set of nontrivial divisors for the base 2 through 10 interpretations of the jamcoin would be: 3, 7, 5, 6, 31, 8, 27, 5, and 77, respectively.

Can you produce J different jamcoins of length N, along with proof that they are legitimate?

Input

The first line of the input gives the number of test cases, T. T test cases follow; each consists of one line with two integers N and J.

Output

For each test case, output J+1 lines. The first line must consist of only Case #x:, where x is the test case number (starting from 1). Each of the last J lines must consist of a jamcoin of length N followed by nine integers. The i-th of those nine integers (counting starting from 1) must be a nontrivial divisor of the jamcoin when the jamcoin is interpreted in base i+1.

All of these jamcoins must be different. You cannot submit the same jamcoin in two different lines, even if you use a different set of divisors each time.

Limits

T = 1. (There will be only one test case.)
It is guaranteed that at least J distinct jamcoins of length N exist.

Small dataset

N = 16.
J = 50.
Large dataset

N = 32.
J = 500.
Note that, unusually for a Code Jam problem, you already know the exact contents of each input file. For example, the Small dataset's input file will always be exactly these two lines:

1
16 50
So, you can consider doing some computation before actually downloading an input file and starting the clock.

Sample


Input

Output

1
6 3

Case #1:
100011 5 13 147 31 43 1121 73 77 629
111111 21 26 105 1302 217 1032 513 13286 10101
111001 3 88 5 1938 7 208 3 20 11

In this sample case, we have used very small values of N and J for ease of explanation. Note that this sample case would not appear in either the Small or Large datasets.

This is only one of multiple valid solutions. Other sets of jamcoins could have been used, and there are many other possible sets of nontrivial base 10 divisors. Some notes:

110111 could not have been included in the output because, for example, it is 337 if interpreted in base 3 (1*243 + 1*81 + 0*27 + 1*9 + 1*3 + 1*1), and 337 is prime.
010101 could not have been included in the output even though 10101 is a jamcoin, because jamcoins begin with 1.
101010 could not have been included in the output, because jamcoins end with 1.
110011 is another jamcoin that could have also been used in the output, but could not have been added to the end of this output, since the output must contain exactly J examples.
For the first jamcoin in the sample output, the first number after 100011 could not have been either 1 or 35, because those are trivial divisors of 35 (100011 in base 2).
"""
import argparse


def get_divisor(n):
    """returns the lowest divisor found for n. Returns None if n is Prime or 1.
    NOTE: No longer used in favor of a more clever appraoch.
    """
    if n < 2:
        return None
    if n == 2 or n == 3:
        return None
    if n % 2 == 0:
        return 2
    if n < 9:
        return None

    if n % 3 == 0:
        return 3

    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return f
        if n % (f + 2) == 0:
            return f+2

        f += 6
    return None


def get_jamcoins(jamcoin_len, num_of_examples):
    """Returns a list of num_of_examples of jamcoins where
    jamcon_len is jamcoin_len and each row consists of the jamcoin
    and the ith element (starting from 1) is a divisor for the when
    the jamcoin is interpreted in base i+1.
    """
    retval = []
    increment = 0
    while len(retval) < num_of_examples:
        jamcoin_set = []
        jamcoin_base10 = int('1{}1'.format('0'*(jamcoin_len-2)), 2) \
            + int(increment)
        jamcoin = bin(jamcoin_base10)[2:]
        increment += 1

        if not jamcoin.startswith('1') or not jamcoin.endswith('1'):
            continue

        jamcoin_set.append(jamcoin)

        for i in range(2, 11):
            ## This was the brute force way that got the lowest divisor
            ## However it fails on the large dataset due to inefficency
            # divisor = get_divisor(int(jamcoin, i))
            # if divisor:
            #     jamcoin_set.append(str(divisor))
            # else:
            #     break

            ## Thie large dataset solution notices that i + 1 must be a divisor
            ## if the number is a jamcoin, observed from smallfile output
            if int(jamcoin, i) % (i+1) == 0:
                jamcoin_set.append(str(i+1))
            else:
                break

        if len(jamcoin_set) == 10:
            retval.append(jamcoin_set)

    return retval


def main(filepath):
    outfile_name = filepath.replace('.in', '.out') if '.in' in filepath \
        else filepath + '.out'
    with open(filepath) as infile, open(outfile_name, 'w') as outfile:
        num_of_test_cases = int(infile.readline().strip())
        for i in range(1, num_of_test_cases+1):
            row = infile.readline().strip().split()
            jamcoin_len = int(row[0])
            num_of_examples = int(row[1])
            jamcoins = get_jamcoins(jamcoin_len, num_of_examples)
            outfile.write('Case #{}:\n'.format(i))
            for jamcoin_list in jamcoins:
                outfile.write(" ".join(jamcoin_list) + '\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", help="Filepah to the input filename")
    args = parser.parse_args()

    main(filepath=args.infile)
