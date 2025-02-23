from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.visited = set()
        total_islands = 0

        n = len(self.grid)
        m = len(self.grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    self.bst(i, j)
                    total_islands += 1

        return total_islands

    def bst(self, i, j):
        self.visited.add((i, j))
        queue = deque([(i, j)])

        while queue:
            node = queue.popleft()
            neighbors = self.generate_neighbors(node[0], node[1])
            for neighbor in neighbors:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    queue.append(neighbor)

    def generate_neighbors(self, i, j):
        neighbors = []
        n = len(self.grid)
        m = len(self.grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and self.grid[ni][nj] == "1":
                neighbors.append((ni, nj))
        return neighbors

    def testNumIslands(self, grid: List[List[str]], expected: int):
        actual = self.numIslands(grid)
        if actual == expected:
            print(f"Test Case Passed!")
        else:
            print(f"Test Case Failed!\ngrid: {grid}\nactual: {actual}, expected: {expected}")


Solution().testNumIslands(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ],
    1
)
Solution().testNumIslands(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ],
    3
)
