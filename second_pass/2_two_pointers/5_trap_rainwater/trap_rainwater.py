from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        total = 0
        n = len(height)

        left_max_height = [0] * n
        right_max_height = [0] * n

        for i in range(n):
            if i == 0:
                left_max_height[i] = height[i]
            else:
                left_max_height[i] = max(height[i], left_max_height[i - 1])

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                right_max_height[i] = height[i]
            else:
                right_max_height[i] = max(height[i], right_max_height[i + 1])

        for i in range(1, n):
            total += min(left_max_height[i], right_max_height[i]) - height[i]

        return total

    def testTrap(self, height, expected):
        actual = self.trap(height)
        if actual == expected:
            print("Test Case Passed")
        else:
            print(f"Test Case Failed! height: {height} actual: {actual} expected: {expected}")


Solution().testTrap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
Solution().testTrap([4, 2, 0, 3, 2, 5], 9)
