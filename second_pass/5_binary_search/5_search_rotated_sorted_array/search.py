from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[left] <= nums[mid]:
                    # Inflection point is to the right
                    # Check if the target is in the non-rotated side of the midpoint (left)
                    if target < nums[mid] and target >= nums[left]:
                        right = mid - 1 # Search left
                    else:
                        left = mid + 1 # Search right
                else:
                    # Inflection point is to the left
                    # Check if the target is in the non-rotated side of the midpoint (right)
                    if target > nums[mid] and target <= nums[right]:
                        left = mid + 1 # Search right
                    else:
                        right = mid - 1 # Search left

        return -1

    def testSearch(self, nums: List[int], target: int, expected: int):
        actual = self.search(nums, target)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! nums: {nums} target: {target} actual: {actual} expected: {expected}")


Solution().testSearch([4, 5, 6, 7, 0, 1, 2], 0, 4)
Solution().testSearch([4, 5, 6, 7, 0, 1, 2], 3, -1)
Solution().testSearch([1], 0, -1)
Solution().testSearch([3, 1], 1, 1)
Solution().testSearch([1, 3], 3, 1)
