from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            if num in map:
                map[num].append(i)
            else:
                map[num] = [i]

        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in map:
                index = next((x for x in map[to_find] if x != i), None)
                if index is not None:
                    return [index, i]

        return None
