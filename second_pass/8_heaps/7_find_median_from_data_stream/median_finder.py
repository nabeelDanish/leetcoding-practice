from typing import List


# class MedianFinder:

#     def __init__(self):
#         from collections import defaultdict
#         self.counter = defaultdict(int)
#         self.total = 0

#     def addNum(self, num: int) -> None:
#         self.counter[num] += 1
#         self.total += 1

#     def findMedian(self) -> float:
#         all_numbers = sorted(list(self.counter.keys()))
#         is_even = self.total % 2 == 0
#         n = (self.total // 2)

#         if is_even:
#             left_idx = self.total // 2 - 1
#             right_idx = self.total // 2
#         else:
#             median_idx = self.total // 2

#         count_seen = 0
#         median1 = None
#         median2 = None

#         for number in all_numbers:
#             count = self.counter[number]
#             count_seen += count

#             if not is_even:
#                 if median1 is None and count_seen > median_idx:
#                     median1 = number
#                     break
#             else:
#                 if median1 is None and count_seen > left_idx:
#                     median1 = number
#                 if median2 is None and count_seen > right_idx:
#                     median2 = number
#                     break

#         if not is_even:
#             return float(median1)
#         return (median1 + median2) / 2

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        import heapq

        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # balancing the heaps
        while abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap) + 1:
                largest_of_max = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, largest_of_max)
            else:
                smallest_of_min = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -smallest_of_min)

    def findMedian(self) -> float:
        len_min_heap = len(self.min_heap)
        len_max_heap = len(self.max_heap)

        if len_min_heap == len_max_heap:
            median1 = self.min_heap[0] if len_min_heap > 0 else 0
            median2 = -self.max_heap[0] if len_max_heap > 0 else 0
            return (median1 + median2) / 2
        elif len_min_heap > len_max_heap:
            return float(self.min_heap[0])
        else:
            return float(-self.max_heap[0])


def testMedianFinder(actions: List[str], inputs: List, expected: List[float]):
    median_finder = None
    for i, action in enumerate(actions):
        if action == "MedianFinder":
            median_finder = MedianFinder()
        elif action == "addNum":
            median_finder.addNum(inputs[i][0])
        elif action == "findMedian":
            median = median_finder.findMedian()
            assert expected[i] == median, f"Test Case Failed! action: {action}, inputs: {inputs[i]}, expected: {expected[i]}, actual: {median}"

    print("Test Case Passed!")


testMedianFinder(
    ["MedianFinder", "addNum", "addNum", "addNum", "addNum", "addNum", "addNum", "addNum", "addNum", "findMedian"],
    [[], [1], [1], [2], [3], [4], [4], [5], [6], []],
    [None, None, None, None, None, None, None, None, None, 3.5]
)
testMedianFinder(
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
    [[], [1], [2], [], [3], []],
    [None, None, None, 1.5, None, 2.0]
)
