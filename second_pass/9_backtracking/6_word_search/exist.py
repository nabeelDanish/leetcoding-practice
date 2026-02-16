from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        used = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.backtrack(board, word, 0, used, i, j):
                    return True
        return False

    def backtrack(self, board: List[List[str]], word: str, path_ix: int, used: List[List[bool]], curr_x: int, curr_y: int):
        m = len(board)
        n = len(board[0])

        # we are at the edge
        if curr_x == m or curr_y == n:
            return False

        # check if the board piece is already used in the path
        if used[curr_x][curr_y]:
            return False
        
            

        # add the current board piece and check if we reached the word
        if board[curr_x][curr_y] == word[path_ix]:
            path_ix += 1
        else:
            used[curr_x][curr_y] = False
            return False
            return True

        if not word.startswith(word_so_far):
            path.pop()
            used[curr_x][curr_y] = False
            return False

        # move in all possible directions, extending the path
        if curr_x + 1 <= m:
            ans = self.backtrack(board, word, path, used, curr_x + 1, curr_y)
            if ans:
                return True
        if curr_x - 1 >= 0:
            ans = self.backtrack(board, word, path, used, curr_x - 1, curr_y)
            if ans:
                return True
        if curr_y + 1 <= n:
            ans = self.backtrack(board, word, path, used, curr_x, curr_y + 1)
            if ans:
                return True
        if curr_y - 1 >= 0:
            ans = self.backtrack(board, word, path, used, curr_x, curr_y - 1)
            if ans:
                return True

        # pop this from the path
        path.pop()
        used[curr_x][curr_y] = False
        return False

    def testExist(self, board: List[List[str]], word: str, expected: bool):
        actual = self.exist(board, word)
        if actual == expected:
            print(f"Test Case Passed for word: {word}")
        else:
            print(f"Test Case Failed! board: {board}, word: {word}, actual: {actual}, expected: {expected}")


Solution().testExist(
    [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    "ABCCED",
    True
)
Solution().testExist(
    [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    "SEE",
    True
)
Solution().testExist(
    [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
    "ABCB",
    False
)
