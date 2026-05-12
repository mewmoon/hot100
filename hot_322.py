# 322 零钱兑换
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):  # 注意+1
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


# coins = [1, 2, 5]
coins = [288, 160, 10, 249, 40, 77, 314, 429]
# coins = [2]
print(Solution().coinChange(coins, 9208))
