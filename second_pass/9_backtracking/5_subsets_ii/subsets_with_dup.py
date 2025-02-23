from copy import deepcopy
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.all_subsets = []
        nums.sort()
        self.backtrack([], nums, 0)
        return self.all_subsets

    def backtrack(self, current: List[int], nums: List[int], start: int):
        self.all_subsets.append(current[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            self.backtrack(current, nums, i + 1)
            current.pop()

    def testSubsetsWithDup(self, nums: List[int], expected: List[List[int]]):
        actual = self.subsetsWithDup(nums)
        if len(actual) != len(expected):
            print(f"Test Case Failed!: nums: {nums}\nactual: {actual}\nexpected: {expected}\n")
            return

        for find in expected:
            if find not in actual:
                print(f"Test Case Failed!: nums: {nums}\nactual: {actual}\nexpected: {expected}\n")
                return

        print(f"Test Case Passed!")


Solution().testSubsetsWithDup(
    [1, 2, 2],
    [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
)
Solution().testSubsetsWithDup(
    [4, 4, 4, 1, 4],
    [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4], [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]]
)
