# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Handle the case when the input node is None
        if node is None:
            return None

        # Create a mapping from original nodes to their clones
        old_to_new = {}

        def clone(node: Node) -> Node:
            if node in old_to_new:
                return old_to_new[node]

            # Create a clone of the current node
            copy = Node(node.val)
            old_to_new[node] = copy

            # Recursively clone the neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))

            return copy

        return clone(node)

    def areGraphsEqual(self, node1: Optional['Node'], node2: Optional['Node'], visited=None) -> bool:
        if visited is None:
            visited = set()

        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        if node1 in visited:
            return True

        visited.add(node1)

        if len(node1.neighbors) != len(node2.neighbors):
            return False

        for n1, n2 in zip(node1.neighbors, node2.neighbors):
            if not self.areGraphsEqual(n1, n2, visited):
                return False

        return True

    def testCloneGraph(self, node: Optional['Node'], expected: Optional['Node']):
        actual = self.cloneGraph(node)
        if self.areGraphsEqual(actual, expected):
            print("Test passed.")
        else:
            print(f"Test failed. Expected: {expected}, Actual: {actual}")

    def buildGraph(self, adjacency_list):
        if not adjacency_list:
            return None

        nodes = [Node(i) for i in range(1, len(adjacency_list) + 1)]

        for i, neighbors in enumerate(adjacency_list):
            nodes[i].neighbors = [nodes[j - 1] for j in neighbors]

        return nodes[0]


Solution().testCloneGraph(
    node=Solution().buildGraph([[2, 4], [1, 3], [2, 4], [1, 3]]),
    expected=Solution().buildGraph([[2, 4], [1, 3], [2, 4], [1, 3]])
)
Solution().testCloneGraph(
    node=Solution().buildGraph([[2], [1]]),
    expected=Solution().buildGraph([[2], [1]])
)
Solution().testCloneGraph(
    node=Solution().buildGraph([]),
    expected=Solution().buildGraph([])
)
