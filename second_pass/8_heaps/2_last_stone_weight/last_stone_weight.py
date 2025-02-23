from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        heap = []
        for stone in stones:
            heapq.heappush(heap, (stone * -1))

        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)

            if x == y:
                continue
            else:
                new_stone = y - x
                heapq.heappush(heap, (new_stone))

        if heap:
            return heap[0] * -1
        return 0

    def testLastStoneWeight(self, stones: List[int], expected: int):
        actual = self.lastStoneWeight(stones)
        if actual == expected:
            print(f"Test Case Passed!")
        else:
            print(f"Test Case Failed!: stones: {stones}, actual: {actual}, expected: {expected}")


Solution().testLastStoneWeight([2, 7, 4, 1, 8, 1], 1)
