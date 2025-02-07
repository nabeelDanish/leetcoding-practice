from ..util import TreeNode, BinaryTree
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.traverseDiameterOfBinaryTree(root, 0)
        return self.max_diameter

    def traverseDiameterOfBinaryTree(self, root, depth):
        if root is None:
            return 0

        left_max_depth = self.traverseDiameterOfBinaryTree(root.left, depth + 1)
        right_max_depth = self.traverseDiameterOfBinaryTree(root.right, depth + 1)

        diameter = left_max_depth + right_max_depth
        if diameter > self.max_diameter:
            self.max_diameter = diameter

        return max(left_max_depth, right_max_depth) + 1

    def testDiameterOfBinaryTree(self, root: Optional[TreeNode], expected: int):
        actual = self.diameterOfBinaryTree(root)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)


Solution().testDiameterOfBinaryTree(
    BinaryTree.build_binary_tree([1, 2, 3, 4, 5]),
    3
),
Solution().testDiameterOfBinaryTree(
    BinaryTree.build_binary_tree([1, 2, 3, 4, 5, None, None, 6, None, 7, None]),
    4
)
Solution().testDiameterOfBinaryTree(
    BinaryTree.build_binary_tree([1, 2]),
    1
)
