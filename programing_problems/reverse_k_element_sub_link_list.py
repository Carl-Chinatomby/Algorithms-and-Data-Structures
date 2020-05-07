#!/usr/bin/env python3
"""
Problem:
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head: ListNode, k: int) -> ListNode:
    previous = None
    current = head
    count = 0
    while (current):
        next = current.next
        current.next = previous
        previous = current
        current = next
        count += 1
        if count == k and next:
            head.next = reverse_k_group(next, k)
            break

    return previous


def print_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()


def main():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print_list(head)
    result = reverse_k_group(head, 3)
    print_list(result)

    print()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print_list(head)
    result = reverse_k_group(head, 5)
    print_list(result)


if __name__ == "__main__":
    main()
