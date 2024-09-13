"""
Ace The Data Science Interview


Medium Problems
9.20. Two Sigma: Given a list of several categories (for example, the strings A, B, C, and D), sample
from the list of categories according to a particular relative weighting scheme. For example,
say we give A a relative weight of 5, B a weight of 10, C a weight of 15, and D a weight of 20,
How do we construct this sampling? How do you extend the solution to an arbitrary large number of
k categories?
"""
import random

def get_random_sample_from_weighted_k_inefficient(): # O(N) time and space
    w_a, w_b, w_c, w_d = 5, 10, 15, 20
    lst = ['A'] * w_a + ['B'] * w_b + ['C'] * w_c + ['D'] * w_d
    return(random.choice(lst))

def binary_search(a, k):
    lo, hi = 0, len(a) - 1
    best = lo
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        if a[mid] < k:
            lo = mid + 1
        elif a[mid] > k:
            hi = mid - 1
        else:
            best = mid
            break
    return best


def get_random_sample_from_weighted_k():
    categories = ['A', 'B', 'C', 'D']
    weights = [5, 10, 15, 20]
    # cumulative sum [5, 15, 30, 50]
    cum_sum = [sum(weights[:i]) for i in range i(len(weights)+1)]
    k = random.randrange(cum_sum[-1]) # choose randomly in range (0, total_sum)
    i = binary_search(cum_sum, k) # binary search for k
    return categories[i]

if __name__ == "__main__":
    arr1 = []
    arr2 = []
    expected_value = 0

    actual_value = func(arr1, arr2)
    print("Test 1: ", actual_value == expected_value,
        "actual: ", actual_value,
        "expected: ", expected_value
    )
