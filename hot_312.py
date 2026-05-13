# 312 戳气球
from typing import List


# //Hard 难以理解ToS
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        val = [1] + nums + [1]
        n, nv = len(nums), len(val)

        dp = [[0] * nv for _ in range(nv)]

        for i in range(nv - 3, -1, -1):
            for j in range(i + 2, nv):
                for k in range(i + 1, j):
                    tmp = val[i] * val[j] * val[k]
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + tmp)

        return dp[0][nv - 1]


nums = [3, 1, 5, 8]
print(Solution().maxCoins(nums))
