def fixed_length_sliding_window(nums, k):
    state = # choose appropriate data structure
    start = 0
    max_ = 0

    for end in range(len(nums)):
        # extend window
        # add nums[end] to state in O(1) in time

        if end - start + 1 == k:
            # INVARIANT: size of the window is k here.
            max_ = max(max_, contents of state)

            # contract window
            # remove nums[start] from state in O(1) in time
            start += 1

    return max_
