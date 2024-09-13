"""
Ace The Data Science Interview


Medium Problems
9.22. Uber: Given a list of positive integers, return the maximum increasing subsequence sum. In
other words, return the sum of the largest increasing subsequence with the input array. For
example, if the input is [3, 2, 5, 7, 6], return 15 because it's the sum of 3, 5, 7. If the input is
[5, 4, 3, 2, 1], return 5 (since no subsequence is increasing).
"""
# def max_increasing_sum(arr):
#     current_max = 0

#     for i in range(len(arr)):
#         if i-1 >= 0:
#             if arr[i] > arr[i-1]:
#                 current_max += arr[i]
#         else:
#             current_max = arr[i]
#     return current_max
def max_increasing_sum(arr):
    n = len(arr)
    res = [0 for x in range(n)]  # store results
    for a in range(n):
        res[a] = arr[a] # initialize result with initial values

    for i in range (1, n):
        for j in range(i):
            if arr[j] < arr[i] and res[i] < res[j] + arr[i]: # extend the sum
                res[i] = res[j] + arr[i] # add incremental element
    return max(res)


if __name__ == "__main__":
    arr1 = [3, 2, 5, 7, 6]
    arr2 = [5, 4, 3, 2, 1]
    expected_value1 = 15
    expected_value2 = 5

    actual_value = max_increasing_sum(arr1)
    print("Test 1:", actual_value == expected_value1,
        "actual:", actual_value,
        "expected:", expected_value1
    )

    actual_value = max_increasing_sum(arr2)
    print("Test 2:", actual_value == expected_value2,
        "actual:", actual_value,
        "expected:", expected_value2
    )
