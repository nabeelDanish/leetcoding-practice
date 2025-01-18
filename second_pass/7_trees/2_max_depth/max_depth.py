from ..util import TreeNode, BinaryTree
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverseMaxDepth(root, 0, 0)

    def traverseMaxDepth(self, root, currentDepth, maxDepth):
        if root is None:
            return currentDepth

        return max(
            maxDepth,
            self.traverseMaxDepth(root.left, currentDepth + 1, maxDepth),
            self.traverseMaxDepth(root.right, currentDepth + 1, maxDepth),
        )

    def testMaxDepth(self, root: Optional[TreeNode], expected: int):
        actual = self.maxDepth(root)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)


Solution().testMaxDepth(
    BinaryTree.build_binary_tree([3, 9, 20, None, None, 15, 7]),
    3
)
Solution().testMaxDepth(
    BinaryTree.build_binary_tree([1, None, 3]),
    2
)
