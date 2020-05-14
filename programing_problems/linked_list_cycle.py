#!/usr/bin/env python3
"""
https://leetcode.com/problems/linked-list-cycle/
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
