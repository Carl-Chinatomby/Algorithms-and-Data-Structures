#!/usr/bin/env python3
"""
Problem:
https://leetcode.com/problems/circular-array-loop/
"""
from typing import List


def is_cycle(arr: List[int]) -> bool:
    for i in range(len(arr)):
        slow, fast = i, i

        direction = 1 if arr[i] > 0 else -1

        while True:
            slow = (slow + arr[slow]) % len(arr)

            #2 step move
            tmp = (fast + arr[fast]) % len(arr)
            fast = (tmp + arr[tmp]) % len(arr)

            # direction change means no loop
            if direction > 0 and (arr[tmp] < 0 or arr[fast] < 0):
                break
            elif direction < 0 and (arr[tmp] > 0 or arr[fast] > 0):
                break

            if slow == fast: # we caught up
                # if slow is in a 1 item loop, it doesn't count
                if slow == ((slow + arr[slow]) % len(arr)):
                    break

                return True

    return False


def main():
    assert is_cycle([2,-1,1,2,2]) == True
    assert is_cycle([-1,2]) == False
    assert is_cycle([-2,1,-1,-2,-2]) == False


if __name__ == "__main__":
    main()
