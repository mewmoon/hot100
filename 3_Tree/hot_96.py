# 96 不同的二叉搜索树


# O(n^2)
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):  # 以j作为根结点
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


# 上述dp公式即 卡特兰数 (Catalan Number)
# O(n)
class Solution2:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(n):
            C = C * 2 * (2 * i + 1) // (i + 2)
        return C


n = 3
print(Solution().numTrees(n))
