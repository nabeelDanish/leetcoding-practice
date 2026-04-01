import math
from typing import List


class GraphNode:
    def __init__(self, x: int):
        self.val = x
        self.neighbors = []


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Build the graph from the grid
        graph = self.buildGraph(grid)

        # Perform BFS from each treasure cell (0) to calculate distances
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.bfs(graph, (i, j), grid)

        # After BFS, the grid will have the minimum distance to the nearest treasure for each land cell, and -1 for water cells.
        # No need to return anything as we modify the grid in place.

    def bfs(self, graph: List[List[GraphNode]], start: (int, int), grid: List[List[int]]) -> None:
        queue = [graph[start[0]][start[1]]]
        visited = set()
        distance = 0

        while queue:
            next_queue = []
            for node in queue:
                if node in visited:
                    continue
                visited.add(node)

                # Update the distance in the grid
                x, y = node.val
                if grid[x][y] != 0:  # Don't update treasure cells
                    grid[x][y] = min(grid[x][y], distance)

                # Add neighbors to the next level of BFS
                for neighbor in node.neighbors:
                    if neighbor not in visited:
                        next_queue.append(neighbor)
            queue = next_queue
            distance += 1

    def buildGraph(self, grid: List[List[int]]) -> List[List[GraphNode]]:
        # Build a graph from the grid, where each cell is a node and edges exist between adjacent cells that are not -1
        rows, cols = len(grid), len(grid[0])
        graph = [[GraphNode((i, j)) for j in range(cols)] for i in range(rows)]

        # Connect the nodes based on the grid values
        for i in range(rows):
            for j in range(cols):
                # Skip water
                if grid[i][j] == -1:
                    continue

                # Connect to adjacent nodes if they are not water
                if i > 0 and grid[i - 1][j] != -1:
                    graph[i][j].neighbors.append(graph[i - 1][j])
                if i < rows - 1 and grid[i + 1][j] != -1:
                    graph[i][j].neighbors.append(graph[i + 1][j])
                if j > 0 and grid[i][j - 1] != -1:
                    graph[i][j].neighbors.append(graph[i][j - 1])
                if j < cols - 1 and grid[i][j + 1] != -1:
                    graph[i][j].neighbors.append(graph[i][j + 1])

        return graph

    def testIslandsAndTreasure(self, grid: List[List[int]], expected: List[List[int]]) -> None:
        self.islandsAndTreasure(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                assert grid[i][j] == expected[i][j], f"Expected {expected[i][j]} at ({i}, {j}), but got {grid[i][j]}"
        print("Test passed.")


Solution().testIslandsAndTreasure(
    grid=[
        [math.inf, -1, 0, math.inf],
        [math.inf, math.inf, math.inf, -1],
        [math.inf, -1, math.inf, -1],
        [0, -1, math.inf, math.inf]
    ],
    expected=[
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4]
    ]
)
Solution().testIslandsAndTreasure(
    grid=[
        [0, -1],
        [math.inf, math.inf]
    ],
    expected=[
        [0, -1],
        [1, 2]
    ]
)
