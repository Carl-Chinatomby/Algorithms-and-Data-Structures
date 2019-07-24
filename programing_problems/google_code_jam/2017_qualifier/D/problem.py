#!/usr/bin/env python3
"""
"""
import argparse


def problem():
    return True


def main(filepath):
    with open(filepath) as infile:
        num_of_test_cases = int(infile.readline().strip())
        outfile_name = filepath.replace('.in', '.out') if '.in' in filepath \
            else filepath + '.out'

        with open(outfile_name, 'w') as outfile:
            for i in range(1, num_of_test_cases + 1):
                input_num = int(infile.readline().strip())
                output = problem(input_num)
                outfile.write('Case #{}: {}\n'.format(i, output))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", help="Filepath to the input filename")
    args = parser.parse_args()

    main(filepath=args.infile)
