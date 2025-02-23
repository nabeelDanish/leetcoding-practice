from typing import List
from copy import deepcopy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.all_subsets = [[]]
        self.backtrack([], nums)
        return self.all_subsets

    def backtrack(self, previous: List[int], inputs: List[int]):
        if not inputs:
            return

        n = len(inputs)
        for i in range(n):
            previous.append(inputs[i])
            to_insert = deepcopy(previous)
            self.all_subsets.append(to_insert)

            self.backtrack(previous, inputs[i + 1:])

            previous.pop()

    def testSubsets(self, nums: List[int], expected: List[List[int]]):
        actual = self.subsets(nums)
        if len(actual) != len(expected):
            print(f"Test Case Failed!: stones: {nums}, actual: {actual}, expected: {expected}")
            return

        for i in range(len(actual)):
            find = expected[i]
            if find not in actual:
                print(f"Test Case Failed!: stones: {nums}, actual: {actual}, expected: {expected}")
                return

        print(f"Test Case Passed!")


Solution().testSubsets([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
