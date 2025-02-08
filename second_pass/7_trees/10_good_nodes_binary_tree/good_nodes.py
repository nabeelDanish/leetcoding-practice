from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Best Solution
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         import math
#         return self.traverse(root, -math.inf)

#     def traverse(self, root: Optional[TreeNode], max_above: int) -> int:
#         if root is None:
#             return 0

#         score = 0
#         if root.val >= max_above:
#             score = 1

#         return score + self.traverse(root.left, max(max_above, root.val)) + self.traverse(root.right, max(max_above, root.val))

#     def testGoodNodes(self, root: TreeNode, expected: int):
#         actual = self.goodNodes(root)
#         if actual == expected:
#             print("Test Case Passed!")
#         else:
#             print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
#             BinaryTree.print_binary_tree(root)

# DFS Solutions
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, float('-inf'))]

        good_nodes = 0
        while stack:
            last_tuple = stack.pop()
            last_node = last_tuple[0]
            last_max_value = last_tuple[1]

            if not last_node:
                continue
            
            if last_node.val >= last_max_value:
                good_nodes += 1

            stack.append((last_node.left, max(last_max_value, last_node.val)))
            stack.append((last_node.right, max(last_max_value, last_node.val)))

        return good_nodes

    def testGoodNodes(self, root: TreeNode, expected: int):
        actual = self.goodNodes(root)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)


Solution().testGoodNodes(
    BinaryTree.build_binary_tree([3, 1, 4, 3, None, 1, 5]),
    4
)
Solution().testGoodNodes(
    BinaryTree.build_binary_tree([3, 3, None, 4, 2]),
    3
)
Solution().testGoodNodes(
    BinaryTree.build_binary_tree([-1, 5, -2, 4, 4, 2, -2, None, None, -4, None, -2, 3, None, -2, 0, None, -1, None, -3, None, -4, -3, 3, None, None, None, None, None, None, None, 3, -3]),
    5
)
