from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap = []

        for point in points:
            x, y = point
            distance = (x ** 2 + y ** 2) ** 0.5
            heapq.heappush(heap, (distance, point))

        results = []
        for _ in range(k):
            results.append(heapq.heappop(heap)[1])

        return results

    def testKClosest(self, points: List[List[int]], k: int, expected: List[List[int]]):
        actual = self.kClosest(points, k)
        if actual == expected:
            print(f"Test Case Passed!")
        else:
            print(f"Test Case Failed!: points: {points}, k: {k}, actual: {actual}, expected: {expected}")


Solution().testKClosest(
    [[1, 3], [-2, 2]],
    1,
    [[-2, 2]]
)
Solution().testKClosest(
    [[3, 3], [5, -1], [-2, 4]],
    2,
    [[3, 3], [-2, 4]]
)
