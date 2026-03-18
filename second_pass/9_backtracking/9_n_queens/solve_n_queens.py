from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        paths = []
        self.backtrack(n, [], paths, 0)
        return paths

    def backtrack(self, n: int, path: List[str], paths: List[List[str]], curr_ix: int):
        # if we have reached the end of the board, we have found a valid path, add it to the paths list and return
        if curr_ix == n:
            paths.append(path.copy())
            return

        # iterate through the columns of the current row and check if we can place a queen in the current column,
        # if we can, we will add it to the path and continue backtracking with the next row as the current index,
        # after backtracking we will pop the queen from the path and continue checking for other columns
        for i in range(n):
            if self.isValid(path, curr_ix, i, n):
                row = ['.'] * n
                row[i] = 'Q'
                path.append(''.join(r for r in row))
                self.backtrack(n, path, paths, curr_ix + 1)
                path.pop()

        # we are backtracking, pop the queen from the path and continue checking for other columns
        return

    def isValid(self, path: List[str], row: int, col: int, n: int) -> bool:
        # check if we can place a queen in the current column by checking if there is a queen in the same column or in the same diagonal
        for i in range(row):
            if path[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and path[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < n and path[i][col + (row - i)] == 'Q':
                return False

        return True

    def testSolveNQueens(self, n: int, expected: List[List[str]]):
        actual = self.solveNQueens(n)
        if len(actual) == len(expected) and all([a in expected for a in actual]):
            print(f"Test Case Passed for n: {n}")
        else:
            print(f"Test Case Failed! n: {n}, actual: {actual}, expected: {expected}")


Solution().testSolveNQueens(
    4,
    [
        [
            ".Q..",
            "...Q",
            "Q...",
            "..Q."
        ],
        [
            "..Q.",
            "Q...",
            "...Q",
            ".Q.."
        ]
    ]
)
Solution().testSolveNQueens(
    1,
    [
        [
            "Q"
        ]
    ]
)
