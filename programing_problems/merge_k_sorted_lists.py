#!/usr/bin/env python3
"""
Given K sorted linked lists of size N each, merge them and print the sorted output.

Example:

Input: k = 3, n =  4
list1 = 1->3->5->7->NULL
list2 = 2->4->6->8->NULL
list3 = 0->9->10->11->NULL

Output:
0->1->2->3->4->5->6->7->8->9->10->11
"""
from collections import defaultdict
from heapq import (
    heapify,
    heappush,
    heappop,
    heapreplace,
    heappushpop,
)

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def merge_k_sorted_lists(arrs, k):
    min_heap = [(arrs[i].val, arrs[i]) for i in range(k)]
    heapify(min_heap)

    head = None
    current = head
    while min_heap:
        _, minnode = heappop(min_heap)
        if not head:
            head = minnode
            current = head
        else:
            current.next = minnode
            current = minnode

        if minnode.next:
            heappush(min_heap, (minnode.next.val, minnode.next))

    return head


def print_list(head: Node):
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()


def main():
    # create lists
    k = 3

    head1 = Node(1, Node(3, Node(5, Node(7))))
    head2 = Node(2, Node(4, Node(6, Node(8))))
    head3 = Node(0, Node(9, Node(10, Node(11))))
    print_list(head1)
    print_list(head2)
    print_list(head3)
    print('Sorted:')
    lists = [head1, head2, head3]
    merged_head = merge_k_sorted_lists(lists, k)
    print_list(merged_head)



if __name__ == "__main__":
    main()
