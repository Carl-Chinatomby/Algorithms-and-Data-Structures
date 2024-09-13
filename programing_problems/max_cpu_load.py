#!/usr/bin/env python3
"""
Given an array of jobs with different time requirements, where each job consists of start time, end time and CPU load. The task is to find the maximum CPU load at any time if all jobs are running on the same machine.

Examples:

Input: jobs[] = {{1, 4, 3}, {2, 5, 4}, {7, 9, 6}}
Output: 7
Explanation:
In the above-given jobs, there are two jobs which overlaps.
That is, Job [1, 4, 3] and [2, 5, 4] overlaps for the time period in [2, 4]
Hence, the maximum CPU Load at this instant will be maximum (3 + 4 = 7).



Input: jobs[] = {{6, 7, 10}, {2, 4, 11}, {8, 12, 15}}
Output: 15
Explanation:
Since, There are no jobs that overlaps.
Maximum CPU Load will be – max(10, 11, 15) = 15
"""
from heapq import (
    heapify,
    heappush,
    heappop,
)
from typing import List


def max_cpu_load(jobs: List[List[int]]) -> int:
    # merge intervals by splitting overlapping into separate intervals
    jobs = sorted(jobs, reverse=True)
    merged_intervals = [jobs.pop()]

    while jobs:
        start, stop, cost = jobs.pop()

        if merged_intervals:
            mstart, mstop, mcost = merged_intervals[-1]
        else:
            merged_intervals.append([start, stop, cost])
            continue

        if mstop <= start: # no overlap
            merged_intervals.append([start, stop, cost])
            continue
        else: # there is overlap, we need to split this up
            merged_intervals.pop()
            if mstart == start:
                jobs.append([mstart, mstop, cost+mcost])
            else:
                jobs.append([mstart, start, mcost])
                jobs.append([start, mstop, cost+mcost])

            if mstop != stop:
                jobs.append([mstop, stop, cost])

        jobs = sorted(jobs, reverse=True)

    max_cost = 0
    for _, _, cost in merged_intervals:
        if cost > max_cost:
            max_cost = cost

    return max_cost


def max_cpu_load_minheap(jobs: List[List[int]]) -> int:
    # merge intervals by splitting overlapping into separate intervals
    jobs = sorted(jobs)
    max_cost, current_cost = 0, 0
    min_heap = []
    heapify(min_heap)

    for job in jobs:
        while min_heap and job[0] >= min_heap[0][1]:  # job start is less job end of existing jobs
            current_cost -= min_heap[0][2] # subtract cost
            heappop(min_heap)

        heappush(min_heap, job)
        current_cost += job[2]
        if current_cost > max_cost:
            max_cost = current_cost

    return max_cost


def main():
    assert max_cpu_load([[1, 4, 3], [2, 5, 4], [7, 9, 6]]) == 7
    assert max_cpu_load([[6, 7, 10], [2, 4, 11], [8, 12, 15]]) == 15
    assert max_cpu_load([[1, 4, 3], [2, 5, 4], [2, 7, 5], [2, 9, 10], [7, 9, 6]]) == 22

    # using a min heap
    assert max_cpu_load_minheap([[1, 4, 3], [2, 5, 4], [7, 9, 6]]) == 7
    assert max_cpu_load_minheap([[6, 7, 10], [2, 4, 11], [8, 12, 15]]) == 15
    assert max_cpu_load_minheap([[1, 4, 3], [2, 5, 4], [2, 7, 5], [2, 9, 10], [7, 9, 6]]) == 22


if __name__ == "__main__":
    main()
