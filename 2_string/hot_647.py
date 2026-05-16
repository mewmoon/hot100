# 647 回文子串


# 暴力求解
class Solution:
    def countSubstrings(self, s: str) -> int:
        return sum(
            s[j:i] == s[j:i][::-1] for i in range(1, len(s) + 1) for j in range(i)
        )


# 中心扩展 O(n^2) O(1)
class Solution2:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.re = 0

        def extend(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                self.re += 1
                l -= 1
                r += 1

        for i in range(n):
            extend(i, i)
            extend(i, i + 1)

        return self.re


# Manacher 算法
class Solution3:
    def countSubstrings(self, s: str) -> int:
        pass


s = "abcbe"
print(Solution().countSubstrings(s))
