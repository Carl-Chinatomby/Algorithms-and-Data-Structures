"""
Ace The Data Science Interview

Hard Problems
9.27. Google: Given a number n, return the number of lists  of consecutive positive integers that sum
up to n. For example, for n = 9, return 3, since the consecutive positive integer lists are
[2, 3, 4], [4, 5], and [9]. Can you solve this in linear time?
"""
import math


def count_increasing_subarrays_sum(n):
    if n <= 1:
        return 1

    count = 0
    start = 1
    end = 2

    while start <= end and end <= (n//2+1):
        current_sum = sum(range(start, end+1))
        if current_sum < n:
            end += 1
        elif current_sum == n:
            print('found match', current_sum, start, end)
            count+= 1
            start += 1
        else:
            start += 1
    return count + 1 # This accounts for start == end == n since we stop at the high way mark


def count_increasing_subarrays_sum(n):
    upper_limit = int(math.sqrt(2*n))
    num = 0
    for m in range(upper_limit):
        if (2*n) % (m+1) == 0 and (2*n/(m+1)-m) % 2 == 0:
            num += 1
    return num


if __name__ == "__main__":
    n = 9
    expected_value = 3

    actual_value = count_increasing_subarrays_sum(9)
    print("Test 1:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )
