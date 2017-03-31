#!/usr/bin/env python3
"""
Problem

The Infinite House of Pancakes has just introduced a new kind of pancake! It has a happy face made of chocolate chips on one side (the "happy side"), and nothing on the other side (the "blank side").

You are the head waiter on duty, and the kitchen has just given you a stack of pancakes to serve to a customer. Like any good pancake server, you have X-ray pancake vision, and you can see whether each pancake in the stack has the happy side up or the blank side up. You think the customer will be happiest if every pancake is happy side up when you serve them.

You know the following maneuver: carefully lift up some number of pancakes (possibly all of them) from the top of the stack, flip that entire group over, and then put the group back down on top of any pancakes that you did not lift up. When flipping a group of pancakes, you flip the entire group in one motion; you do not individually flip each pancake. Formally: if we number the pancakes 1, 2, ..., N from top to bottom, you choose the top i pancakes to flip. Then, after the flip, the stack is i, i-1, ..., 2, 1, i+1, i+2, ..., N. Pancakes 1, 2, ..., i now have the opposite side up, whereas pancakes i+1, i+2, ..., N have the same side up that they had up before.

For example, let's denote the happy side as + and the blank side as -. Suppose that the stack, starting from the top, is --+-. One valid way to execute the maneuver would be to pick up the top three, flip the entire group, and put them back down on the remaining fourth pancake (which would stay where it is and remain unchanged). The new state of the stack would then be -++-. The other valid ways would be to pick up and flip the top one, the top two, or all four. It would not be valid to choose and flip the middle two or the bottom one, for example; you can only take some number off the top.

You will not serve the customer until every pancake is happy side up, but you don't want the pancakes to get cold, so you have to act fast! What is the smallest number of times you will need to execute the maneuver to get all the pancakes happy side up, if you make optimal choices?

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S, each character of which is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up). The string, when read left to right, represents the stack when viewed from top to bottom.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of times you will need to execute the maneuver to get all the pancakes happy side up.

Limits

1 ≤ T ≤ 100.
Every character in S is either + or -.

Small dataset

1 ≤ length of S ≤ 10.
Large dataset

1 ≤ length of S ≤ 100.
Sample


Input

Output

5
-
-+
+-
+++
--+-

Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3

In Case #1, you only need to execute the maneuver once, flipping the first (and only) pancake.

In Case #2, you only need to execute the maneuver once, flipping only the first pancake.

In Case #3, you must execute the maneuver twice. One optimal solution is to flip only the first pancake, changing the stack to --, and then flip both pancakes, changing the stack to ++. Notice that you cannot just flip the bottom pancake individually to get a one-move solution; every time you execute the maneuver, you must select a stack starting from the top.

In Case #4, all of the pancakes are already happy side up, so there is no need to do anything.

In Case #5, one valid solution is to first flip the entire stack of pancakes to get +-++, then flip the top pancake to get --++, then finally flip the top two pancakes to get ++++.
"""
import argparse


def flip_pancakes(arrangement):
    # reverse and then invert
    return "".join(
        [
            '-' if arrangement[i] == '+' else '+'
            for i in range(len(arrangement)-1, -1, -1)
        ]
    )


def get_min_flips_for_pancakes(arrangement):
    """
        Returns the minimum number of pancake stack flips required to get the
            arrangment to be all +* (all happy side up)

        :params :arrangment string A string of a combination of + or - chars
            where + is a happy side up and - is a happy side down pancake
    """
    num_of_flips = 0
    while arrangement != '+'*len(arrangement):
        bottom_flip = False
        for i in range(len(arrangement)-1, -1, -1):
            if arrangement[i] == '-':
                bottom_flip = True
                # we need to make sure we don't flip a correctly happy side
                # and end up placing it at the bottom
                if arrangement[0] == '-':
                    arrangement = flip_pancakes(
                            arrangement[:i+1]
                        ) + arrangement[i+1:]
                    num_of_flips += 1
                    break
            # we've arrived at a happy pancake but since we know the bottom
            # is incorrect, we'll have to flip the entire stack anyways
            # so let's get them in the happy side down position so the bottom
            # flip will correct everything.
            elif arrangement[i] == '+' and bottom_flip:
                arrangement = flip_pancakes(
                        arrangement[:i+1]
                    ) + arrangement[i+1:]
                num_of_flips += 1
                break
    return num_of_flips


def main(filepath):
    with open(filepath) as infile:
        num_of_test_cases = int(infile.readline().strip())
        outfile_name = filepath.replace('.in', '.out') if '.in' in filepath \
            else filepath + '.out'

        with open(outfile_name, 'w') as outfile:
            for i in range(1, num_of_test_cases + 1):
                pancake_arrangement = infile.readline().strip()
                min_moves = get_min_flips_for_pancakes(pancake_arrangement)
                outfile.write('Case #{}: {}\n'.format(i, min_moves))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", help="Filepath to the input filename")
    args = parser.parse_args()

    main(filepath=args.infile)
