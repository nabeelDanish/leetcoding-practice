from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        total_len = m * n

        left = 0
        right = total_len - 1

        while left <= right:
            mid = (left + right) // 2
            i = mid // n
            j = mid % n

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def testSearchMatrix(self, matrix: List[List[int]], target: int, expected: bool):
        actual = self.searchMatrix(matrix, target)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! matrix: {matrix} target: {target} actual: {actual} expected: {expected}")


Solution().testSearchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True)
Solution().testSearchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False)
