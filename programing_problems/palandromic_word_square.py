# Determine if a NxN matrix is a palindromic word square
# https://digitalcommons.butler.edu/cgi/viewcontent.cgi?article=2003&context=wordways
from typing import List


square1 = [
    ['S', 'A', 'T', 'O', 'R'],
    ['A', 'R', 'E', 'P', 'O'],
    ['T', 'E', 'N', 'E', 'T'],
    ['O', 'P', 'E', 'R', 'A'],
    ['R', 'O', 'T', 'A', 'S'],
]

square2 = [
    ['S', 'A', 'T', 'O', 'R'],
    ['A', 'R', 'E', 'P', 'O'],
    ['T', 'E', 'L', 'E', 'T'],
    ['O', 'P', 'E', 'R', 'A'],
    ['R', 'O', 'T', 'A', 'S'],
]

square3 = [
    ['S', 'A', 'T', 'O', 'R'],
    ['A', 'R', 'E', 'P', 'O'],
    ['T', 'E', 'N', 'E', 'T'],
    ['O', 'P', 'E', 'R', 'A'],
    ['B', 'O', 'T', 'A', 'S'],
]

square4 = [
    ['B', 'A', 'T', 'O', 'R'],
    ['A', 'R', 'E', 'P', 'O'],
    ['T', 'E', 'N', 'E', 'T'],
    ['O', 'P', 'E', 'R', 'A'],
    ['R', 'O', 'T', 'A', 'S'],
]


def is_sator_square(square: List[List]) -> bool:
    n = len(square)  # matrix is NxN

    for i in range(n):
        for j in range(i, n):
            if square[i][j] != square[j][i] or square[i][j] != square[n-j-1][n-i-1]:
                return False

    return True


def main():
    assert is_sator_square(square1) == True  # noqa
    assert is_sator_square(square2) == True  # noqa
    assert is_sator_square(square3) == False  # noqa
    assert is_sator_square(square4) == False  # noqa


if __name__ == "__main__":
    main()
