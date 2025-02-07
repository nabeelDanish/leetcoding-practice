from ..util import TreeNode, BinaryTree
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def testIsSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode], expected: bool):
        actual = self.isSameTree(p, q)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(p)
            BinaryTree.print_binary_tree(q)


Solution().testIsSameTree(
    BinaryTree.build_binary_tree([1, 2, 3]),
    BinaryTree.build_binary_tree([1, 2, 3]),
    True
)
Solution().testIsSameTree(
    BinaryTree.build_binary_tree([1, 2]),
    BinaryTree.build_binary_tree([1, None, 2]),
    False
)
Solution().testIsSameTree(
    BinaryTree.build_binary_tree([1, 2, 1]),
    BinaryTree.build_binary_tree([1, 1, 2]),
    False
)
