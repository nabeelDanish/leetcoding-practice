from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_pointer = nums[0]
        fast_pointer = nums[0]

        # Since we know there is a loop we keep the while loop running
        # Until we find the duplicate
        while True:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]
            if slow_pointer == fast_pointer:
                break

        # Now that we have the meeting point we can find the duplicate
        # by starting the slow pointer from the start and fast pointer from the meeting point
        slow_pointer = nums[0]
        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]

        # Where the slow pointer and fast pointer meet is the duplicate
        return slow_pointer

    def testFindDuplicate(self, nums: List[int], expected: int):
        actual = self.findDuplicate(nums)
        if actual != expected:
            print(f"Expected {expected} but got {actual}")
        else:
            print("Test Case Passed")


Solution().testFindDuplicate([1, 3, 4, 2, 2], 2)
Solution().testFindDuplicate([3, 1, 3, 4, 2], 3)
Solution().testFindDuplicate([3, 3, 3, 3, 3], 3)
Solution().testFindDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1], 9)
