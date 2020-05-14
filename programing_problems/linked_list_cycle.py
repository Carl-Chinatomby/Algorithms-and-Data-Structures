#!/usr/bin/env python3
"""
https://leetcode.com/problems/squares-of-a-sorted-array/
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""
from collections import deque
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode) -> bool:
    if not head:
        return False

    slow = head
    fast = head

    while fast.next:
        slow = slow.next
        fast = fast.next.next if fast.next else None
        if not fast:
            break

        if slow == fast:
            return True

    return False

def main():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    last = head.next.next.next = ListNode(-4)
    last.next = head.next
    assert has_cycle(head) == True

    head = ListNode(1)
    last = head.next = ListNode(2)
    last.next = head
    assert has_cycle(head) == True

    head = ListNode(1)
    assert has_cycle(head) == False

    assert has_cycle(None) == False

if __name__ == "__main__":
    main()
