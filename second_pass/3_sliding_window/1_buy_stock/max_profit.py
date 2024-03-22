from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        n = len(prices)
        brought_for = prices[0]
        max_profit = 0

        for i in range(1, n):
            if prices[i] < brought_for:
                brought_for = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - brought_for)

        return max_profit

    def testMaxProfit(self, prices, expected):
        actual = self.maxProfit(prices)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed!")


Solution().testMaxProfit([7, 1, 5, 3, 6, 4], 5)
Solution().testMaxProfit([7, 6, 4, 3, 1], 0)
