class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    @classmethod
    def print_binary_tree(cls, root):
        if not root:
            print("The tree is empty.")
            return

        from collections import deque

        # Use a queue to perform level-order traversal
        queue = deque([root])
        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(str(node.val) if node else "None")

                if node:
                    queue.append(node.left)
                    queue.append(node.right)

            # Print the current level
            print(" ".join(current_level))


    @classmethod
    def build_binary_tree(cls, level_order):
        if not level_order or level_order[0] is None:
            return None

        from collections import deque

        # Create the root of the tree
        root = TreeNode(level_order[0])
        queue = deque([root])
        i = 1

        while queue and i < len(level_order):
            node = queue.popleft()

            if level_order[i] is not None:
                node.left = TreeNode(level_order[i])
                queue.append(node.left)
            i += 1

            if i < len(level_order) and level_order[i] is not None:
                node.right = TreeNode(level_order[i])
                queue.append(node.right)
            i += 1

        return root

    @classmethod
    def compare_binary_trees(cls, tree1, tree2):
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        if tree1.val != tree2.val:
            return False

        return cls.compare_binary_trees(tree1.left, tree2.left) and cls.compare_binary_trees(tree1.right, tree2.right)