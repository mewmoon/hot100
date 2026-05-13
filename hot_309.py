# 309 买卖股票最佳时期（含冷冻期）
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or n == 1:
            return 0
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][1] - prices[i], dp[i - 1][0])  # 买入 or 继续持有
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][2])  # 上一时刻没有持有
            dp[i][2] = dp[i - 1][0] + prices[i]  # 卖出
        print(dp)
        return max(dp[-1])


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        m0, m1, m2 = -prices[0], 0, 0
        for i in range(1, len(prices)):
            i0 = max(m0, m1 - prices[i])
            i1 = max(m1, m2)
            i2 = m0 + prices[i]
            m0, m1, m2 = i0, i1, i2
        return max(m1, m2)


# prices = [2, 5, 0, 1, 7]
prices = [2, 1]
print(Solution().maxProfit(prices))
