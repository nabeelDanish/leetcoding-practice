from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

    def testFindKthLargest(self, nums: List[int], k: int, expected: int):
        actual = self.findKthLargest(nums, k)
        if actual == expected:
            print(f"Test Case Passed!")
        else:
            print(f"Test Case Failed!: nums: {nums}, k: {k}, actual: {actual}, expected: {expected}")


Solution().testFindKthLargest(
    [3, 2, 1, 5, 6, 4],
    2,
    5
)
Solution().testFindKthLargest(
    [3, 2, 3, 1, 2, 4, 5, 5, 6],
    4,
    4
)
