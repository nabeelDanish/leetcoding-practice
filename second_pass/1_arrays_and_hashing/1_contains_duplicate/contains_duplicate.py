from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(list(set(nums))) != len(nums)

    def testContainsDuplicate(self, nums, expected) -> bool:
        actual = self.containsDuplicate(nums)
        
        if actual == expected:
            print ('Test Case Passed!')
        else:
            print (f'Test Case Failed! nums: {nums} expected: {expected} actual: {actual}')

solution = Solution()

solution.testContainsDuplicate([1,2,3,1], True)
solution.testContainsDuplicate([1,2,3,4], False)
solution.testContainsDuplicate([1,1,1,3,3,4,3,2,4,2], True)