from typing import List
from copy import deepcopy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.backtrack(nums, [], [], permutations)
        return permutations

    def backtrack(self, nums: List[int], path: List[int], used: List[int], permutations: List[List[int]]):
        if len(used) == len(nums):
            return

        for num in nums:
            if num in used:
                continue

            path.append(num)
            used.append(num)

            self.backtrack(nums, path, used, permutations)

            if len(path) == len(nums):
                permutations.append(deepcopy(path))

            path.pop()
            used.pop()

    def testPermute(self, nums: List[int], expected: List[List[int]]) -> None:
        result = self.permute(nums)
        if sorted(result) == sorted(expected):
            print(f"Test passed for nums={nums}")
        else:
            print(f"Test failed for nums={nums}. Expected {expected}, but got {result}")


Solution().testPermute(
    [1, 2, 3],
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
)
Solution().testPermute(
    [0, 1],
    [[0, 1], [1, 0]]
)
Solution().testPermute(
    [1],
    [[1]]
)
