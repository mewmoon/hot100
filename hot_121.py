# 121 买卖股票的最佳时机
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(0, max_profit, price - min_price)

        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(0, max_profit, price - min_price)
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(Solution2().maxProfit(prices))
