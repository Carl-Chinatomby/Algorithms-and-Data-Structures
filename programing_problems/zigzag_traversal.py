#!/usr/bin/env python3
"""
Problem:
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(root: TreeNode) -> List[List[int]]:
    level = 0
    stack = []
    queue = [root]
    vals = []
    while stack or queue:
        level += 1
        level_vals = []
        if level % 2:
            while(queue):
                node = queue.pop(0)
                level_vals.append(node.val)
                if node.left:
                   stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        else:
            while stack:
                node = stack.pop()
                level_vals.append(node.val)
                if node.left:
                   queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        vals.append(level_vals)

    return vals


def main():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    result = zigzag_level_order(root)
    assert result == [[3], [20,9], [15,7]]

if __name__ == "__main__":
    main()
