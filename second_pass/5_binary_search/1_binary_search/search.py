from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def testSearch(self, nums: List[int], target: int, expected: int):
        actual = self.search(nums, target)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! nums: {nums} target: {target} actual: {actual} expected: {expected}")


Solution().testSearch([-1, 0, 3, 5, 9, 12], 9, 4)
Solution().testSearch([-1, 0, 3, 5, 9, 12], 2, -1)
