from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        nums = sorted(nums)
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = n - 1
            target = 0 - nums[i]

            while (start < end):
                sum = nums[start] + nums[end]

                if sum == target:
                    output.append([nums[i], nums[start], nums[end]])

                    while (start < n - 1 and nums[start] == nums[start + 1] and start < end):
                        start += 1

                    while (end > 1 and nums[end] == nums[end - 1] and start < end):
                        end -= 1

                    start += 1
                    end -= 1

                elif sum < target:
                    start += 1

                else:
                    end -= 1

        return output

    def testThreeSum(self, nums, expected):
        actual = self.threeSum(nums)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed nums: {nums} actual: {actual} expected: {expected}")


Solution().testThreeSum([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
Solution().testThreeSum([0, 1, 1], [])
Solution().testThreeSum([0, 0, 0], [[0, 0, 0]])
