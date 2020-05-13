#!/usr/bin/env python3
"""
https://leetcode.com/problems/task-scheduler/

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.



Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


Constraints:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
from collections import defaultdict
from heapq import(
    heapify,
    heappush,
    heappop,
    heappushpop,
)
from typing import List

def get_least_num_of_intervals(tasks: List[str], cooling_interval: int) -> int:
    task_count = defaultdict(int)
    for task in tasks: # O(n)
        task_count[task] -= 1 # to ensure the minheap values are used as max heap

    max_heap = list(task_count.values())
    heapify(max_heap)
    intervals = 0
    while max_heap:
        current_time = 0
        cooling_tasks = []
        while current_time <= cooling_interval:
            intervals += 1
            current_time += 1
            if max_heap:
            # we  queued up all the tasks to cool,
            # if the heap is empty, that means this is idle time
                if max_heap[0] < -1: # this task still has other processing left over
                    cooling_tasks.append(heappop(max_heap) + 1) # we processed 1 task
                else: # task is done, no need to care about it
                    heappop(max_heap)

            if not max_heap and not cooling_tasks: # we're done
                break

        for task in cooling_tasks: # let's add back the tasks that were cooling and pick off the max
            heappush(max_heap, task)

    return intervals



def main():
    tasks = tasks = ["A","A","A","B","B","B"]
    n = 2
    assert get_least_num_of_intervals(tasks, n) == 8


if __name__ == "__main__":
    main()
