from ..util import TreeNode, BinaryTree
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        self.traverseIsBalanced(root, 0)
        return self.is_balanced

    def traverseIsBalanced(self, root: Optional[TreeNode], depth: int):
        if root is None:
            return 0

        left_max_height = self.traverseIsBalanced(root.left, depth + 1)
        right_max_height = self.traverseIsBalanced(root.right, depth + 1)

        if abs(left_max_height - right_max_height) > 1:
            self.is_balanced = False

        return max(left_max_height, right_max_height) + 1

    def testIsBalance(self, root: Optional[TreeNode], expected: bool):
        actual = self.isBalanced(root)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)


Solution().testIsBalance(
    BinaryTree.build_binary_tree([3, 9, 20, None, None, 15, 7]),
    True
)
Solution().testIsBalance(
    BinaryTree.build_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4]),
    False
)
Solution().testIsBalance(
    BinaryTree.build_binary_tree([]),
    True
)
