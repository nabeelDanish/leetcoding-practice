from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Best optimized recursive solution
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if not root and not subRoot:
#             return True

#         if not root or not subRoot:
#             return False

#         if root.val == subRoot.val:
#             is_same_tree = self.isSameTree(root, subRoot)
#             if is_same_tree:
#                 return is_same_tree

#         return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if not p or not q:
#             return False
#         if p.val != q.val:
#             return False

#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#     def testIsSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], expected: bool):
#         actual = self.isSubtree(root, subRoot)
#         if actual == expected:
#             print("Test Case Passed!")
#         else:
#             print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
#             BinaryTree.print_binary_tree(root)
#             BinaryTree.print_binary_tree(subRoot)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        root_serialized = []
        self.serializeTree(root, root_serialized)

        sub_root_serialized = []
        self.serializeTree(subRoot, sub_root_serialized)

        root_str = ''.join(map(str, root_serialized))
        sub_root_str = ''.join(map(str, sub_root_serialized))

        return sub_root_str in root_str

    def serializeTree(self, root: Optional[TreeNode], serialized_list: List[str]):
        if not root:
            serialized_list.append("#")
            return

        serialized_list.append(root.val)
        self.serializeTree(root.left, serialized_list)
        self.serializeTree(root.right, serialized_list)

    def testIsSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], expected: bool):
        actual = self.isSubtree(root, subRoot)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)
            BinaryTree.print_binary_tree(subRoot)


Solution().testIsSubtree(
    BinaryTree.build_binary_tree([3, 4, 5, 1, 2]),
    BinaryTree.build_binary_tree([4, 1, 2]),
    True
)
Solution().testIsSubtree(
    BinaryTree.build_binary_tree([3, 4, 5, 1, 2, None, None, None, None, 0]),
    BinaryTree.build_binary_tree([4, 1, 2]),
    False
)
