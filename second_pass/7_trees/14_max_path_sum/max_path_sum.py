from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -10000000
        self.traverse(root)
        return self.max_path

    def traverse(self, root: Optional[TreeNode]):
        if not root:
            return 0

        left_max_path = self.traverse(root.left)
        right_max_path = self.traverse(root.right)

        max_path = max(
            left_max_path + right_max_path + root.val,
            left_max_path + root.val, 
            right_max_path + root.val, 
            root.val
        )
        
        if max_path > self.max_path:
            self.max_path = max_path

        return max(left_max_path + root.val, right_max_path + root.val, root.val)

    def testMaxPathSum(self, root: Optional[TreeNode], expected: int):
        actual = self.maxPathSum(root)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)


Solution().testMaxPathSum(
    BinaryTree.build_binary_tree([-10, 9, 20, None, None, 15, 7]),
    42
)
Solution().testMaxPathSum(
    BinaryTree.build_binary_tree([2, -1]),
    2
)
