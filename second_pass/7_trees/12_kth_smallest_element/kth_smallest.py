from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.smallest = None
        self.traverse(root)
        return self.smallest

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return

        if self.smallest is not None:
            return

        self.traverse(root.left)
        if self.smallest is not None:
            return

        self.k -= 1
        if self.k == 0:
            self.smallest = root.val
            return

        self.traverse(root.right)
        if self.smallest is not None:
            return

    def testKthSmallest(self, root: Optional[TreeNode], k: int, expected: int):
        actual = self.kthSmallest(root, k)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)


Solution().testKthSmallest(
    BinaryTree.build_binary_tree([3, 1, 4, None, 2]),
    1,
    1
)
Solution().testKthSmallest(
    BinaryTree.build_binary_tree([5, 3, 6, 2, 4, None, None, 1]),
    3,
    3
)
