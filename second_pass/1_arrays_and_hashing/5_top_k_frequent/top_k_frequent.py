from curses import start_color
from typing import List
from collections import Counter
import random


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     map = {}
    #     top_k = [0] * k
    #     n = len(nums)

    #     for i in range(n):
    #         num = nums[i]
    #         if num in map:
    #             map[num][0] += 1
    #         else:
    #             map[num] = [1, -1]

    #         j = k - 1 if map[num][1] == -1 else map[num][1]
    #         count = map[num][0]

    #         # TODO: Nabeel - Complete this function
    #         while top_k[j] < count and j >= 0:
    #             j -= 1

    #         if top_k[j] < count:
    #             top_k[j] = count

    #     print(map)
    #     print(top_k)
    def partition(self, nums, counts, pivot_index, start_index, end_index):
        n = len(nums)

        print(start_index, end_index, pivot_index)
        temp = nums[pivot_index]
        nums[pivot_index] = nums[end_index]
        nums[end_index] = temp

        store_index = start_index
        for i in range(start_index, end_index):
            if counts[nums[i]] < counts[nums[pivot_index]]:
                temp = nums[i]
                nums[i] = nums[store_index]
                nums[store_index] = temp

                store_index += 1

        nums[store_index], nums[n - 1] = nums[n - 1], nums[store_index]
        return nums, store_index

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        unique = list(counts.keys())
        n = len(unique)
        start_index = 0
        end_index = n - 1

        while True:
            pivot_index = random.randint(start_index, end_index)
            parted_list, pivot_now = self.partition(unique, counts, pivot_index, start_index, end_index)

            print(unique[pivot_index], parted_list)

            if pivot_now == n - k:
                return unique[pivot_now + 1:n - 1]
            elif pivot_now > n - k:
                end_index = pivot_now - 1
            else:
                start_index = pivot_now + 1


solution = Solution()
solution.topKFrequent([7, 7, 10, 10, 10, 10, 10, 3, 3, 3, 3, 3, 3, 9, 9, 4, 2, 2, 2, 2], 3)

# TODO: Nabeel - Revise QuickSort
# TODO: Nabeel - Read the editorial for this problem
