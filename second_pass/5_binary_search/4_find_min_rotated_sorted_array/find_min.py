from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        import math
        n = len(nums)
        left = 0
        right = n - 1
        x = nums[0]
        z = nums[n - 1]
        min_found = x

        while left < right:
            mid = (left + right) // 2
            y = nums[mid]

            if y < z and y < x:
                if mid > left:
                    min_found = min(min_found, nums[mid])
                    right = mid - 1
                else:
                    return min(min_found, nums[mid])
            elif y >= z and y >= x:
                left = mid + 1
            else:
                right = mid - 1

        return min(min_found, nums[left])

    def testFindMin(self, nums: List[int], expected: int):
        actual = self.findMin(nums)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! nums: {nums} actual: {actual} expected: {expected}")


Solution().testFindMin([3, 4, 5, 1, 2], 1)
Solution().testFindMin([4, 5, 6, 7, 0, 1, 2], 0)
Solution().testFindMin([11, 13, 15, 17], 11)
Solution().testFindMin([1], 1)
Solution().testFindMin([2, 1], 1)
Solution().testFindMin([2, 3, 4, 5, 1], 1)
Solution().testFindMin([3, 1, 2], 1)
