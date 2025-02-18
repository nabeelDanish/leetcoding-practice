from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])

        inorder_index = inorder.index(preorder[0])
        inorder_left = inorder[:inorder_index]
        inorder_right = inorder[inorder_index + 1:]

        preorder_left = preorder[1:1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left):]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root

    def testBuildTree(self, preorder: List[int], inorder: List[int], expected: Optional[TreeNode]):
        actual = self.buildTree(preorder, inorder)
        if BinaryTree.compare_binary_trees(actual, expected):
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! preorder: {preorder} -- inorder {inorder}")
            BinaryTree.print_binary_tree(actual)
            BinaryTree.print_binary_tree(expected)


Solution().testBuildTree(
    [3, 9, 20, 15, 7],
    [9, 3, 15, 20, 7],
    BinaryTree.build_binary_tree([3, 9, 20, None, None, 15, 7])
)
Solution().testBuildTree(
    [-1],
    [-1],
    BinaryTree.build_binary_tree([-1])
)
