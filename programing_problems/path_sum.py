#!/usr/bin/env python3
"""
Problem:
https://leetcode.com/problems/path-sum/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: TreeNode, sum: int) -> bool:
    if root is None:
        return sum == 0
    else:
        result = False
        remaining_sum = sum - root.val

        if  not remaining_sum and not root.left and not root.right:
            return True

        if root.left:
            result = result or has_path_sum(root.left, remaining_sum)

        if root.right:
            result = result or has_path_sum(root.right, remaining_sum)

    return result


def main():
    root = TreeNode(10, TreeNode(8, TreeNode(3), TreeNode(5)), TreeNode(2, TreeNode(2)))
    assert has_path_sum(root, 21) == True
    assert has_path_sum(root, 23) == True
    assert has_path_sum(root, 14) == True
    assert has_path_sum(root, 10) == False
    assert has_path_sum(root, 5) == False


if __name__ == "__main__":
    main()
