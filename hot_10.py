# 10 正则表达式匹配


# //Hard 难以理解边界 Tos
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        def match(i, j):
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]

        for i in range(m + 1):  # 第0行必须要更新
            for j in range(1, n + 1):  # 第0列无需更新
                if p[j - 1] == "*":
                    dp[i][j] |= dp[i][j - 2]  # 0*
                    if match(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]  # n*
                elif match(i, j):
                    dp[i][j] |= dp[i - 1][j - 1]
            print(dp)
        return dp[m][n]


s = "aa"
p = "*"
print(Solution().isMatch(s, p))
