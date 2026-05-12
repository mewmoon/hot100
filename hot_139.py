# 139 单词拆分
from enum import Flag
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s is None:
            return True
        if wordDict is None:
            return False

        n = len(s)
        word_set = set(wordDict)
        max_len = max([len(w) for w in word_set])
        dp = [True] + [False] * n

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - 1 - max_len, -1), -1):
                if s[j:i] in word_set and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]


s, wordDict = "leetcode", ["leet", "code"]
s, wordDict = "catsandog", ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))
