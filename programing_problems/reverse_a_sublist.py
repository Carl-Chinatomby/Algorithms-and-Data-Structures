#!/usr/bin/env python3
"""
We are given a linked list and positions m and n. We need to reverse the linked list from position m to n.

Examples:

Input : 10->20->30->40->50->60->70->NULL
        m = 3, n = 6
Output : 10->20->60->50->40->30->70->NULL

Input :  1->2->3->4->5->6->NULL
         m = 2, n = 4
Output : 1->4->3->2->5->6->NULL

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()


def reverse_sublist(head: ListNode, m: int, n: int) -> int:
    count = 0
    before = None
    after = None
    while head:
        count += 1
        #import pdb; pdb.set_trace()
        if count+1 == m:
            before = head
        elif count == n:
            after = head.next
            break

        head = head.next

    count = 0
    k = n - m + 1
    previous = after
    current = before.next
    while current and count < k:
        next = current.next
        current.next = previous
        previous = current
        current = next
        count += 1

    before.next = previous  # set pointer to new head

    return None


def main():
    head = ListNode(10, ListNode(20, ListNode(30, ListNode(40, ListNode(50, ListNode(60, ListNode(70)))))))
    reverse_sublist(head, 3, 6)
    print_list(head)

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    reverse_sublist(head, 2, 4)
    print_list(head)


if __name__ == "__main__":
    main()
