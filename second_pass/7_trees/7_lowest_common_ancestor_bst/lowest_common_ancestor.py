from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Path Tracing Solution

# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         path_to_p: List[TreeNode] = []
#         path_to_q: List[TreeNode] = []

#         self.build_path(root, p, path_to_p)
#         self.build_path(root, q, path_to_q)

#         lowest_common_ancestor = root
#         n = len(path_to_p)
#         m = len(path_to_q)

#         for i in range(min(n, m)):
#             if path_to_p[i].val == path_to_q[i].val:
#                 lowest_common_ancestor = path_to_p[i]
#             else:
#                 break

#         return lowest_common_ancestor

#     def build_path(self, node: Optional[TreeNode], target: TreeNode, path: List[TreeNode]):
#         if node is None:
#             return

#         if node.val == target.val:
#             path.append(node)
#             return
#         elif node.val > target.val:
#             path.append(node.left)
#             return self.build_path(node.left, target, path)
#         else:
#             path.append(node.right)
#             return self.build_path(node.right, target, path)

#     def testLowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode, expected: TreeNode):
#         actual = self.lowestCommonAncestor(root, p, q)
#         if actual.val == expected.val:
#             print("Test Case Passed!")
#         else:
#             print(f"Test Case Failed! actual: {actual}, expected: {expected}")
#             BinaryTree.print_binary_tree(p)
#             BinaryTree.print_binary_tree(q)


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

    def testLowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode, expected: TreeNode):
        actual = self.lowestCommonAncestor(root, p, q)
        if actual.val == expected.val:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(p)
            BinaryTree.print_binary_tree(q)


Solution().testLowestCommonAncestor(
    BinaryTree.build_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
    BinaryTree.build_binary_tree([2]),
    BinaryTree.build_binary_tree([8]),
    BinaryTree.build_binary_tree([6]),
)
Solution().testLowestCommonAncestor(
    BinaryTree.build_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
    BinaryTree.build_binary_tree([2]),
    BinaryTree.build_binary_tree([4]),
    BinaryTree.build_binary_tree([2]),
)
Solution().testLowestCommonAncestor(
    BinaryTree.build_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
    BinaryTree.build_binary_tree([3]),
    BinaryTree.build_binary_tree([5]),
    BinaryTree.build_binary_tree([4]),
)
Solution().testLowestCommonAncestor(
    BinaryTree.build_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]),
    BinaryTree.build_binary_tree([3]),
    BinaryTree.build_binary_tree([9]),
    BinaryTree.build_binary_tree([6]),
)
