# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    slice_cnt = 0
    start_index = 0
    end_index = 0
    done = False

    while not done:
        # We are grouping our slices by stopping at the smallest number below our start point
        for i, val in enumerate(A[start_index:]):
            if val < A[start_index]:
                end_index = i + start_index
        
        slice_cnt += 1
        start_index = end_index = end_index + 1 # start a new slice range
        
        if start_index > len(A) - 1: # we are out of bounds and the last slice covered this value
            done = True
        elif start_index == len(A) - 1: # we are at the end and the last slice is single digit sort
            slice_cnt += 1
            done = True
        
    return slice_cnt
            
        