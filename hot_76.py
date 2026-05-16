# 76 最小覆盖子串
from collections import Counter


# 滑动窗口
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        cnt = Counter()

        done_count = 0  # 达标字符种类:  >=
        required_count = len(freq)

        l = 0
        min_len = float("inf")
        ans_l, ans_r = -1, -1

        for r in range(len(s)):
            print(cnt)
            ch = s[r]
            if ch in freq:
                cnt[ch] += 1
                if cnt[ch] == freq[ch]:
                    done_count += 1

            while done_count == required_count and l <= r:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans_l, ans_r = l, r

                out_ch = s[l]
                if out_ch in freq:
                    if cnt[out_ch] == freq[out_ch]:
                        done_count -= 1
                    cnt[out_ch] -= 1

                l += 1

        return "" if ans_l == -1 else s[ans_l : ans_r + 1]


# 测试代码
s = "ADOBECODEBANC"
t = "ABC"
print(Solution().minWindow(s, t))  # 输出: "BANC"
print(Solution().minWindow(s, t))
