from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_side_view = []
        self.build_right_side_view(root, right_side_view, 0)
        return right_side_view

    def build_right_side_view(self, root: Optional[TreeNode], right_side_view: List[int], depth: int):
        if root is None:
            return

        if depth >= len(right_side_view):
            right_side_view.append(root.val)

        self.build_right_side_view(root.right, right_side_view, depth + 1)
        self.build_right_side_view(root.left, right_side_view, depth + 1)

    def testRightSideView(self, root: Optional[TreeNode], expected: List[int]):
        actual = self.rightSideView(root)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)


Solution().testRightSideView(
    BinaryTree.build_binary_tree([1, 2, 3, None, 5, None, 4]),
    [1, 3, 4]
)
Solution().testRightSideView(
    BinaryTree.build_binary_tree([1, 2, 3, 4, None, None, None, 5]),
    [1, 3, 4, 5]
)
Solution().testRightSideView(
    BinaryTree.build_binary_tree([1, None, 3]),
    [1, 3]
)
Solution().testRightSideView(
    BinaryTree.build_binary_tree([]),
    []
)
