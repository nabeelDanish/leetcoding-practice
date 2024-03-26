from typing import List


class DequeueSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque()
        max_window = []

        n = len(nums)
        left = right = 0

        while right < n:
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)
            if left > q[0]:
                q.popleft()

            if right + 1 >= k:
                max_window.append(nums[q[0]])
                left += 1

            right += 1

        return max_window

    def testMaxSlidingWindow(self, nums, k, expected):
        actual = self.maxSlidingWindow(nums, k)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! nums: {nums}, k: {k}, actual: {actual}, expected: {expected}")


class DynamicProgrammingSolution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        left_max = [0] * n
        left_max[0] = nums[0]

        right_max = [0] * n
        right_max[n - 1] = nums[n - 1]

        # Building the left max array
        # For each bucket of size k
        for i in range(1, n):
            if i % k == 0:
                left_max[i] = nums[i]
            else:
                left_max[i] = max(nums[i], left_max[i - 1])

        # Building the right max array
        # For each bucket of size k
        for i in range(n - 2, -1, -1):
            if i % k == k - 1:
                right_max[i] = nums[i]
            else:
                right_max[i] = max(nums[i], right_max[i + 1])

        output_size = n - k + 1
        max_array = [0] * output_size
        for i in range(output_size):
            max_array[i] = max(left_max[i + k - 1], right_max[i])

        return max_array

    def testMaxSlidingWindow(self, nums, k, expected):
        actual = self.maxSlidingWindow(nums, k)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! nums: {nums}, k: {k}, actual: {actual}, expected: {expected}")


DynamicProgrammingSolution().testMaxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])
