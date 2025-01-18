from typing import Optional
from ..util import TreeNode, BinaryTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        reversed_root = None
        reversed_root = self.invertNode(root, reversed_root)

        return reversed_root

    def invertNode(self, root: Optional[TreeNode], reversed_root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        reversed_root = TreeNode(root.val)

        reversed_root.left = self.invertNode(root.right, reversed_root.left)
        reversed_root.right = self.invertNode(root.left, reversed_root.right)

        return reversed_root

    def testInvertTree(self, root: Optional[TreeNode], expected: Optional[TreeNode]):
        actual = self.invertTree(root)

        if not BinaryTree.compare_binary_trees(actual, expected):
            print(f"\nTest Case Failed! Trees are not equal")
            print(f"actual: ")
            BinaryTree.print_binary_tree(actual)
            print(f"expected: ")
            BinaryTree.print_binary_tree(expected)
        else:
            print("Test Case Passed!")


Solution().testInvertTree(
    BinaryTree.build_binary_tree([4, 2, 7, 1, 3, 6, 9]),
    BinaryTree.build_binary_tree([4, 7, 2, 9, 6, 3, 1]),
)
Solution().testInvertTree(
    BinaryTree.build_binary_tree([2, 1, 3]),
    BinaryTree.build_binary_tree([2, 3, 1]),
)
