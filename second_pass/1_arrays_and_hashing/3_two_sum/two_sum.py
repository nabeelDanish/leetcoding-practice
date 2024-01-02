from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            map[num] = [i]

        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in map:
                index = map[to_find]
                return [index, i]

        return None

    def testTwoSum(self, nums: List[int], target: int, expected: int):
        actual = self.twoSum(nums, target)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed. nums: {nums} target: {target} actual: {actual} expected:{expected}")
