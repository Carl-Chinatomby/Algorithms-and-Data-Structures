"""
Ace The Data Science Interview


Medium Problems
9.23. Palantir: Given a positive integer n, find the smallest number of perfect squares that sum up to
n. For example, for n = 7, you should return 4, since 7 = 4 + 1 + 1 + 1.  For n = 13, you should
return 2, since 13 = 9 + 4.
"""
import math

# def smallest_perfect_squares(n): # Greedy approach doesn't work see 4^2 + 5^2 = 16 + 25 = 41,
#     # greedy would give 6^2 + 2^2 + 1 = 36 + 4 + 1
#     count = 0

#     while n:
#         val = int(math.sqrt(n))
#         if n - val**2 >= 0:
#             n -= val**2
#             count += 1
#     return count

def smallest_perfect_squares(n):
    res = [x for x in range(n+1)] # store results
    for i in range (2, n+1):
        for j in range(1, int(i**0.5) + 1):
            res[i] = min(res[i], res[i - j ** 2] + 1)
    return res[n]

if __name__ == "__main__":
    n1 = 7
    n2 = 13
    expected_value1 = 4
    expected_value2 = 2

    actual_value = smallest_perfect_squares(n1)
    print("Test 1:", actual_value == expected_value1,
        "actual:", actual_value,
        "expected:", expected_value1
    )

    actual_value = smallest_perfect_squares(n2)
    print("Test 2:", actual_value == expected_value2,
        "actual:", actual_value,
        "expected:", expected_value2
    )
