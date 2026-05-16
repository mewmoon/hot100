# 5 最长回文子串


# dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        left, right = 0, 0
        for i in range(n):
            dp[i][i] = True
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                left, right = i, i + 1

        # 右上三角，对角线遍历
        for k in range(2, n):
            for l in range(n - k):
                i, j = l, k + l
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i > right - left:
                        right, left = j, i
                else:
                    dp[i][j] = False
        print(*dp, sep="\n")
        return s[left : right + 1]


# 中心扩展
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        def expend(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        start, end = 0, 0
        for i in range(len(s)):
            ml = max(expend(i, i), expend(i, i + 1))
            if ml > end - start + 1:
                start = i - (ml - 1) // 2
                end = i + ml // 2

        return s[start : end + 1]


s = "abbcccba"
print(Solution().longestPalindrome(s))
