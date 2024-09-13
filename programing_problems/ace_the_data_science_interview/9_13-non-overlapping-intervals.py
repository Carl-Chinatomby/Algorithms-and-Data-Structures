"""
Ace The Data Science Interview


Medium Problems
9.13. Yelp: You are given an array of intervals, where each interval is represented by a start time
and an end time, such as [1, 3]. Determine the smallest number of intervals to remove from
the list, such that the rest of the intervals do not overlap. Intervals can "touch," such as [1, 3]
and [3, 5], but are not allowed to overlap, such as [1, 3] and  [2, 5]). FOr example, if the input
interval  list given is: [[1, 3], [3, 5], [2, 4], [6, 8]], then return 1, since the interval [2, 4]
should be removed.
"""
def interval_removal(interval_list):
    if len(interval_list) == 0:
        return 0

    intervals = sorted(interval_list, key=lambda k: (k[0], k[1]))
    res, low, count = 0, 0, 0
    for high in range(1, len(intervals)):
        if intervals[low][1] > intervals[high][0]:
            count += 1
        if not intervals[high][0] < intervals[low][1]:
            low = high # merge
    return count


if __name__ == "__main__":
    interval_list = [(1,3), (3,5), (2,4), (6,8)]
    expected_value = 1

    actual_value = interval_removal(interval_list)
    print("Test 1: ", actual_value == expected_value)
