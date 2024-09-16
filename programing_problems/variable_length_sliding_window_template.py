def variable_length_sliding_window(nums):
    start = # choose appropriate data structure
    start = 0
    max_ = 0

    for end in range(len(nums)):
        # extend window
        # add nums[end] to state in O(1) in time

        while state is not valid:
            # repeatedly contract window until it is valid again
            # remove nums[start] from start in O(1) in time
            start += 1

        # INVARIANT: state of current window is valid here.
        max_ = max(max_, end - start + 1)

    return max_
