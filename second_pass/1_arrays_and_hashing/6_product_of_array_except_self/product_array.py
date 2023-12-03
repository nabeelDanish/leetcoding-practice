from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = nums[0]
        n = len(nums)
        products = [1] * n
        for i in range(1, n):
            products[i] = left
            left = left * nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            products[i] = products[i] * right
            right = right * nums[i]

        return products

    def testProductExceptSelf(self, nums, expected):
        actual = self.productExceptSelf(nums)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! nums:{nums} actual:{actual} expected: {expected}")


solution = Solution()
solution.testProductExceptSelf([1, 2, 3, 4], [24, 12, 8, 6])
solution.testProductExceptSelf([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])
