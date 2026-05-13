# 279 完全平方数
import math


class Solution:
    def numSquares(self, n: int) -> int:
        coins = []
        for i in range(1, n + 1):
            if i**2 > n:
                break
            coins.append(i**2)
        dp = [0] + [float("inf")] * n
        for coin in coins:
            for j in range(coin, n + 1):  # 注意从coin开始，否则j-coin<0
                dp[j] = min(dp[j - coin] + 1, dp[j])
        return dp[-1]


# 四平方数定理 O(n^1/2) O(1)
class Solution2:
    def numSquares(self, n: int) -> int:
        def isOne(n):
            return int(math.sqrt(n)) ** 2 == n  # 注意平方不是 ^

        def isFour(n):
            while n % 4 == 0:
                n = n // 4
            return n % 8 == 7

        if isOne(n):
            return 1
        if isFour(n):
            return 4

        for i in range(1, int(math.sqrt(n)) + 1):
            if isOne(n - i**2):
                return 2

        return 3


print(Solution2().numSquares(5))
