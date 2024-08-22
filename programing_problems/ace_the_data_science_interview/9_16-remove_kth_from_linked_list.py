"""
Ace The Data Science Interview


Medium Problems
9.16. Workday: Given a linked list, return the head of the same linked list but with k-th node from
the end of a linked list removed. For example, given the linked list 3 -> 2 -> 5 -> 1 -> 4 and k = 3,
remove the 5 node and thus, return the linked list 3 -> 2-> 1 -> 4.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_vals(self):
        vals = [self.val]
        cur = self
        while cur.next:
            vals.append(cur.next.val)
            cur = cur.next
        return vals


def remove_kth(tree, k):
    tree_length = 0
    cur = tree
    while cur:
        tree_length += 1
        cur = cur.next

    remove_pos = tree_length - k + 1
    if remove_pos > 0:
        cur = tree
        pos = 1
        while pos != remove_pos - 1:
            print(pos)
            pos += 1
            cur = cur.next

        cur.next = cur.next.next



if __name__ == "__main__":
    tree = Node(3)
    tree.next = Node(2)
    tree.next.next = Node(5)
    tree.next.next.next = Node(1)
    tree.next.next.next.next = Node(4)

    expected_value = [3,2,1,4]
    remove_kth(tree, 3)
    actual_value = tree.get_vals()
    print("Test 1: ", actual_value == expected_value,
        "actual: ", actual_value,
        "expected: ", expected_value
    )
