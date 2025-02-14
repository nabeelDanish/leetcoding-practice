from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        self.traverse(root)
        return self.is_valid

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return None, None

        if not self.is_valid:
            return None, None

        if root.left is None and root.right is None:
            return root.val, root.val

        left_min_val, left_max_val = self.traverse(root.left)
        right_min_val, right_max_val = self.traverse(root.right)

        if not self.is_valid:
            return None, None

        if left_max_val is not None and left_max_val >= root.val:
            self.is_valid = False
            return None, None

        if right_min_val is not None and right_min_val <= root.val:
            self.is_valid = False
            return None, None

        if left_min_val is None:
            left_min_val = root.val
        if left_max_val is None:
            left_max_val = root.val
        if right_min_val is None:
            right_min_val = root.val
        if right_max_val is None:
            right_max_val = root.val

        max_val = max(left_max_val, right_max_val, root.val)
        min_val = min(left_min_val, right_min_val, root.val)

        return min_val, max_val

    def testIsValidBST(self, root: Optional[TreeNode], expected: bool):
        actual = self.isValidBST(root)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)


Solution().testIsValidBST(
    BinaryTree.build_binary_tree([2, 1, 3]),
    True
)
Solution().testIsValidBST(
    BinaryTree.build_binary_tree([5, 1, 4, None, None, 3, 6]),
    False
)
Solution().testIsValidBST(
    BinaryTree.build_binary_tree([2, 2, 2]),
    False
)
Solution().testIsValidBST(
    BinaryTree.build_binary_tree([1, 1]),
    False
)
Solution().testIsValidBST(
    BinaryTree.build_binary_tree([5, 4, 6, None, None, 3, 7]),
    False
)
Solution().testIsValidBST(
    BinaryTree.build_binary_tree([45, 42, None, None, 44, 43, None, 41]),
    False
)
