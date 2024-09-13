"""
Ace The Data Science Interview


Medium Problems
9.24. Facebook: Given an integer n and an integer k, output a list of all the combinations of k
numbers chosen from 1 to n. For example, if n = 3 and k = 2, return [1, 2], [1, 3], [2, 3].
"""
def get_combinations(n, k):
    def backtrack(n, k, res, combo, num, start):
        if num == k:
            res.append(list(combo))
        if start > n or num >= k:
            return

        for i in range(start, n+1): # iterate over every element
            combo.append(i)
            backtrack(n, k, res, combo, num+1, i+1) # recurse
            combo.remove(i)
    res = []
    backtrack(n, k, res, [], 0, 1)
    return res



if __name__ == "__main__":
    n = 3
    k = 2
    expected_value = [[1, 2], [1, 3], [2, 3]]

    actual_value = get_combinations(n, k)
    print("Test 1:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )
