from ..util import TreeNode, BinaryTree
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        nodes = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(str(node.val) if node else "NONE")

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

            nodes.extend(current_level)

        return ",".join(nodes)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        for i in range(len(data)):
            if data[i] == "NONE":
                data[i] = None
            else:
                data[i] = int(data[i])

        if not data or data[0] is None:
            return None

        from collections import deque
        root = TreeNode(data[0])
        queue = deque([root])
        i = 1

        while queue and i < len(data):
            node = queue.popleft()
            if data[i] is not None:
                node.left = TreeNode(data[i])
                queue.append(node.left)
            i += 1

            if i < len(data) and data[i] is not None:
                node.right = TreeNode(data[i])
                queue.append(node.right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

codec = Codec()
root = BinaryTree.build_binary_tree([1, 2, 3, None, None, 4, 5])
serialized = codec.serialize(root)
print(serialized)

deserialized = codec.deserialize(serialized)

BinaryTree.print_binary_tree(root)
BinaryTree.print_binary_tree(deserialized)
