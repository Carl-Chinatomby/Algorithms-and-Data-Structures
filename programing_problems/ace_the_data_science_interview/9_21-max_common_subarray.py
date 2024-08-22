"""
Ace The Data Science Interview


Medium Problems
9.21. Amazon: Given two arrays with integers, return the maximum length of a common subarray
within both arrays. For example, if the two arrays are [1, 3, 5, 6, 7] and [2, 4, 3, 5, 6] then
return 3, since the length of the maximum common subarray, [3, 5, 6] is 3.
"""
def longest_common(a, b):
    dp = [[0 for i in range(len(a)+1)] for j in range(len(b)+ 1)] # initialize all to 0

    max_val = 0
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1] # update dp[i][j]
                max_val = max(max_val, dp[i][j])
    print(dp)
    return max_val


if __name__ == "__main__":
    arr1 = [1, 3, 5, 6, 7]
    arr2 = [2, 4, 3, 5, 6]
    expected_value = 3

    actual_value = longest_common(arr1, arr2)
    print("Test 1:", actual_value == expected_value,
        "actual:", actual_value,
        "expected:", expected_value
    )
