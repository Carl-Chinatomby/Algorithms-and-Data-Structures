"""
Ace The Data Science Interview


Medium Problems
9.7. Google: Given an array of positive integers, a peak element is greater than it's neighbors. Write
a function to find the index of any peak elements. For example, for [3 ,5, 2, 4, 1], you should
return either 1 or 3 because the values at those indexes, 5 and 4, are both peak elements.
"""
def find_peak_indexes(arr):
    peak_indexes = []
    if not arr:
        return peak_indexes
    elif len(arr) == 1:
        return [arr[0]]
    elif len(arr) > 1 and arr[0] > arr[1]:
        peak_indexes.append(0)


    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peak_indexes.append(i)

    return peak_indexes

def find_peak_index(arr):
    start = 0
    end = len(arr) - 1
    while  True;
        mid = (start + end) // 2
        left = arr[mid-1] if mid - 1 >=0 else float ('-inf')
        right = arr[mid+1] if mid + 1 < len(arr) else float('-inf')
        if left < arr[mid] and right < arr[mid]:
            return mid
        elif arr[mid] < right:
            start = mid + 1
        else:
            end = mid - 1


if __name__ == "__main__":
    arr = [3 ,5, 2, 4, 1]
    expected_values = [1, 3]

    actual_value = find_peak_indexes(arr)
    print("Test 1: ", actual_value == expected_values)

    arr = [5 ,3, 2, 4, 1]
    expected_values = [0, 3]

    actual_value = find_peak_indexes(arr)
    print("Test 2: ", actual_value == expected_values)
