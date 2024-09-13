"""
Ace The Data Science Interview


Medium Problems
9.10. D.E. Shaw: Given a target number, generate a random sample of n integers that sum in that
target that also are within sigma standard deviations of the mean.
"""
import random


def generate_nums(target, n, sigma):
    mean = target / n
    sd = int(sigma * mean)
    max_val, min_val = mean + sd, mean - sd
    results = [min_val] * n
    remaining = target - n * min_val

    while remaining > 0:
        a = random.randint(0, n-1) # choose random index
        if results[a] >= max_val: # skip if above bound
            continue
        results[a] += min(remaining, 1)
        remaining -= 1
    return results


if __name__ == "__main__":
    arr1 = []
    arr2 = []
    expected_value = 0

    #actual_value = func(arr1, arr2)
    #print("Test 1: ", actual_value == expected_value)
