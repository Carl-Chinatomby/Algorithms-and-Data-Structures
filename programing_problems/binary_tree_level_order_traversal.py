#!/usr/bin/env python3
"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root: TreeNode) -> List[int]:
    levels = [root]
    order = []
    while levels:
        new_levels = []
        current_level_vals = []
        for node in levels:
            current_level_vals.append(node.val)
            if node.left:
                new_levels.append(node.left)
            if node.right:
                new_levels.append(node.right)
        levels = new_levels
        order.append(current_level_vals)

    return order


def main():
    head = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order_traversal(head) == [[3], [9, 20], [15, 7]]


if __name__ == "__main__":
    main()
