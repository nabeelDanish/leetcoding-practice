from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = max(piles)

        left = 1
        right = min_k

        while left <= right:
            mid_k = (left + right) // 2

            # Compute the eating and the delta hours that took relative to h
            hours_taken = 0
            for pile in piles:
                hours_taken += ceil(pile / mid_k)

            delta = h - hours_taken

            # We still have hours left to use so we can decrease the speed of eating
            if delta >= 0:
                right = mid_k - 1
                # We finished eating all bananas so this speed is a candidate for min_k
                min_k = min(min_k, mid_k)
            else:
                # We used more hours than we had so we need to increase the speed of eating
                left = mid_k + 1

        return min_k
    
    def testMinEatingSpeed(self, piles: List[int], h: int, expected: int):
        actual = self.minEatingSpeed(piles, h)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! piles: {piles} h: {h} actual: {actual} expected: {expected}")


Solution().testMinEatingSpeed([3, 6, 7, 11], 8, 4)
Solution().testMinEatingSpeed([30, 11, 23, 4, 20], 5, 30)
Solution().testMinEatingSpeed([30, 11, 23, 4, 20], 6, 23)
