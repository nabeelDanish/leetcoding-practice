from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if not num.isdigit():
                    continue

                if num in rows[i]:
                    return False
                if num in columns[j]:
                    return False
                if num in boxes[(i // 3) * 3 + (j // 3)]:
                    return False

                rows[i][num] = True
                columns[j][num] = True
                boxes[(i // 3) * 3 + (j // 3)][num] = True

        return True
