# 64 最小路径和
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n) for _ in range(m)]
        for i in range(m):
            dp[i][0] = dp[i - 1][0] + grid[i][0] if i > 0 else grid[i][0]
        for j in range(n):
            dp[0][j] = dp[0][j - 1] + grid[0][j] if j > 0 else grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().minPathSum(grid))
