from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.k = k
        self.heap = []

        for num in nums:
            heapq.heappush(self.heap, num)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        import heapq
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
instructions = ["KthLargest", "add", "add", "add", "add", "add"]
inputs = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
outputs = [None, 4, 5, 5, 8, 8]

obj = None
for i, instruction in enumerate(instructions):
    if instruction == "KthLargest":
        obj = KthLargest(inputs[i][0], inputs[i][1])
    elif instruction == "add":
        actual = obj.add(inputs[i][0])
        assert actual == outputs[i]
