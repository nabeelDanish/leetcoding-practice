from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        queue = deque([root])
        level_order = []

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()

                if node:
                    current_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if current_level:
                level_order.append(current_level)

        return level_order

    def testLevelOrder(self, root: Optional[TreeNode], expected: List[List[int]]):
        actual = self.levelOrder(root)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!: actual: {actual}, expected: {expected}")
            BinaryTree.print_binary_tree(root)


Solution().testLevelOrder(
    BinaryTree.build_binary_tree([3, 9, 20, None, None, 15, 7]),
    [[3], [9, 20], [15, 7]]
)
