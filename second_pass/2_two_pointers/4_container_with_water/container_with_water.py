from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0
        n = len(height)
        left = 0
        right = n - 1

        while (left < right):
            water = min(height[left], height[right]) * abs(right - left)
            most_water = max(water, most_water)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return most_water

    def testMaxArea(self, height, expected):
        actual = self.maxArea(height)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! height: {height} expected: {expected} actual: {actual}")


Solution().testMaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
Solution().testMaxArea([1, 1], 1)
