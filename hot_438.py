# 438 找到字符串中所有字母异位词
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len:
            return []

        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - ord("a")] += 1
            p_count[ord(p[i]) - ord("a")] += 1

        pos = []
        if s_count == p_count:
            pos.append(0)

        for i in range(p_len, s_len):
            s_count[ord(s[i]) - ord("a")] += 1
            s_count[ord(s[i - p_len]) - ord("a")] -= 1
            if s_count == p_count:
                pos.append(i - p_len + 1)
        return pos


s, p = "cbaebabacd", "abc"
print(Solution().findAnagrams(s, p))
