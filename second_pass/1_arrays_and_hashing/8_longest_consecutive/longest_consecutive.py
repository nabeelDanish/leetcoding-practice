from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        longest = 0

        for num in hashmap:
            if num - 1 not in hashmap:
                current_num = num
                n = 1

                while current_num + 1 in hashmap:
                    current_num += 1
                    n += 1

                longest = max(longest, n)

        return longest

    def testLongestConsecutive(self, nums, output):
        actual = self.longestConsecutive(nums)
        if output == actual:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed. nums = {nums} output = {output} actual = {actual}")


Solution().testLongestConsecutive([100, 4, 200, 1, 3, 2], 4)
Solution().testLongestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
