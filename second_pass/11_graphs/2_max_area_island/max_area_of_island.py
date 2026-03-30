from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        max_area = 0

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = self.bst(grid, visited, i, j, m, n)
                    max_area = max(area, max_area)

        return max_area

    def bst(self, grid: List[List[int]], visited: set, i: int, j: int, m: int, n: int):
        queue = deque()

        queue.append((i, j))
        visited.add((i, j))
        area = 0

        while queue:
            x, y = queue.pop()
            if grid[x][y] == 1:
                area += 1

            neighbors = self.generate_neighbors(grid, x, y, m, n)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return area

    def generate_neighbors(self, grid: List[List[int]], x: int, y: int, m: int, n: int):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        neighbors = []
        for direction in directions:
            a = x + direction[0]
            b = y + direction[1]
            if a < 0 or a >= m:
                continue
            if b < 0 or b >= n:
                continue
            if grid[a][b] != 1:
                continue
            neighbors.append((a, b))
        return neighbors

    def testMaxAreaOfIsland(self, grid: List[List[int]], expected: int):
        actual = self.maxAreaOfIsland(grid)
        if actual == expected:
            print(f"Test Case Passed!")
        else:
            print(f"Test Case Failed!\ngrid: {grid}\nactual: {actual}, expected: {expected}")


Solution().testMaxAreaOfIsland(
    [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ], 6
)
Solution().testMaxAreaOfIsland(
    [[0, 0, 0, 0, 0, 0, 0, 0]], 0
)
Solution().testMaxAreaOfIsland(
    [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ],
    4
)
