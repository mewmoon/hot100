# 3 无重复字符的最长子串


# ❌ 空间消耗大
class Solution0:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        dp = [0] + [1] * len(s)
        ma = 0
        for i, ch in enumerate(s):
            idx = i + 1
            if ch not in last_seen:
                dp[idx] = dp[idx - 1] + 1
                last_seen[ch] = i
            else:
                old = last_seen[ch]
                if old < i - dp[idx - 1]:
                    dp[idx] = dp[idx - 1] + 1
                else:
                    dp[idx] = i - old
                last_seen[ch] = i
            ma = max(ma, dp[idx])
        print(dp)
        return ma


# 双指针更优
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        max_len = 0
        start = 0

        for end, ch in enumerate(s):
            if ch in last_seen:
                start = max(start, last_seen[ch] + 1)

            last_seen[ch] = end
            max_len = max(max_len, end - start + 1)

        return max_len


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
