#!/usr/bin/env python3
"""
Problem:
https://leetcode.com/problems/path-sum-ii/description/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _all_path_sum(root: TreeNode, sum: int, path: List[int], paths: List[List[int]]):
    if root:
        path.append(root.val)

        if not root.left and not root.right and sum == root.val:
            paths.append(path[:]);

        _all_path_sum(root.left, sum - root.val, path, paths)
        _all_path_sum(root.right, sum - root.val, path, paths)
        path.pop()


def all_path_sum(root: TreeNode, sum: int) -> bool:
    paths = []
    path = []
    _all_path_sum(root, sum, path, paths)

    return paths


def main():
    root = TreeNode(5,
        TreeNode(4,
            TreeNode(11,
                TreeNode(7), TreeNode(2))),
        TreeNode(8,
            TreeNode(13), TreeNode(4,
                            TreeNode(5), TreeNode(1)))
    )

    assert all_path_sum(root, 22) ==[[5,4,11,2], [5,8,4,5]]
    assert all_path_sum(root, 5) ==[]
    assert all_path_sum(root, 7) ==[]
    assert all_path_sum(root, 100) ==[]

if __name__ == "__main__":
    main()
