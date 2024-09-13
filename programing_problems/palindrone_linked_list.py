#!/usr/bin/env python3
"""
Problem:
Given a singly linked list of characters, write a function that returns true if the given list is a palindrome, else false.
"""
class Node:

    def __init__(self, value, parent=None):
        self.value = value
        self.next = None
        if parent:
            parent.next = self


def is_palindrone_stack(head):
    is_palindrone = True
    current = head

    values = []
    while current:
        values.append(current.value)
        current = current.next

    current = head
    while current:
        if current.value != values.pop():
            return False
        current = current.next

    return is_palindrone

def is_palindrone_reverse(head):
    if not head or not head.next:
        return True

    slow_ptr = head
    fast_ptr = head
    count = 1

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next
        count += 1
        if fast_ptr.next:
            fast_ptr = fast_ptr.next
            count += 1
    # when the fast pointer reaches None, slowptr is at the midpoint

    # when the split is even we just reverse from mid point
    if not count % 2:
        start = slow_ptr
    else:
        start = slow_ptr.next

    # reverse second half of list
    midlist = reverse(start)

    # compare lists
    is_palindrone = True
    lcurrent = head
    rcurrent = midlist
    while rcurrent:
        if lcurrent.value != rcurrent.value:
            is_palindrone = False
            break

        lcurrent = lcurrent.next
        rcurrent = rcurrent.next

    # rereverse the list so it's back in it's original state
    midlist = reverse(midlist)

    return is_palindrone

def reverse(start):
    current = start
    previous = None
    while (current):
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def main():
    head = Node(1)
    child = Node(2, head)
    assert is_palindrone_stack(head) == False

    child = Node(2, child)
    child = Node(1, child)
    assert is_palindrone_stack(head) == True

    head = Node(1)
    child = Node(2, head)
    assert is_palindrone_reverse(head) == False

    child = Node(2, child)
    child = Node(2, child)
    child = Node(1, child)
    assert is_palindrone_reverse(head) == True
    assert is_palindrone_reverse(head) == True


if __name__ == "__main__":
    main()
