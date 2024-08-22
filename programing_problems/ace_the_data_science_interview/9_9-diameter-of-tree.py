"""
Ace The Data Science Interview


Medium Problems
9.9. Amazon: Given a binary tree, write a function to determine the diameter of the tree, which is
the longest path between any two nodes.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def func(root):
    # Assumption: the longest path is the path from the leftmost node with highest depth
    # to the rightmost node with highest dept

    # Find leftmode node:
    cur = root
    distance = 0
    stack = []
    while cur:
        if cur.left:
            if stack:
                stack.pop()
            distance += 1
            stack.push(cur)
            cur = cur.left
        elif cur.right:
            if stack:
                stack.pop()
            distance += 1
            stack.push(cur)
            cur = cur.right
        else: # we hit a leaf node
            if stack:
                parent = stack.pop()
                if parent.right:
                    cur = parent.right

def calc_diameter(root):
    def depth(root, diameter): # helper
        if root is None:
            return 0, diameter # base case

        left, diameter = depth(root.left, diameter)
        right, diameter = depth(root.right, diameter)
        diameter = max(diameter, left + right) # update diameter
        return max(left, right) + 1, diameter


    depth, diameter = depth(root, 0)
    return diameter



if __name__ == "__main__":
    arr1 = []
    arr2 = []
    expected_value = 0

    actual_value = func(arr1)
    print("Test 1: ", actual_value == expected_value)
