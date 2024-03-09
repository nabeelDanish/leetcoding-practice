from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while (left <= right and left < n and right > 0):
            while left > 0 and numbers[left] == numbers[left - 1]:
                left += 1

            while right < n - 1 and numbers[right] == numbers[right + 1]:
                right -= 1

            calc = numbers[left] + numbers[right]

            if calc == target:
                return [left + 1, right + 1]

            if calc < target:
                left += 1

            if calc > target:
                right -= 1

    def testTwoSum(self, numbers, target, expected):
        actual = self.twoSum(numbers, target)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed. numbers: {numbers} target: {target} actual: {actual} expected: {expected}")


Solution().testTwoSum([2, 7, 11, 15], 9, [1, 2])
Solution().testTwoSum([2, 3, 4], 6, [1, 3])
Solution().testTwoSum([-1, 0], -1, [1, 2])
