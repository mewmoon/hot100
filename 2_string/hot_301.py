# 301删除无效的括号
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        for ch in s:
            if ch == "(":
                l += 1
            if ch == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1

        def isValid(str):
            cnt = 0
            for c in str:
                if c == "(":
                    cnt += 1
                elif c == ")":
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if isValid(s):
                    res.append(s)
                return

            # 还不太懂为啥
            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue
                if lremove + rremove > len(s) - i:
                    break

                if lremove > 0 and s[i] == "(":
                    helper(s[:i] + s[i + 1 :], i, lremove - 1, rremove)
                if rremove > 0 and s[i] == ")":
                    helper(s[:i] + s[i + 1 :], i, lremove, rremove - 1)

        helper(s, 0, l, r)
        return res


s = "()())()"
print(Solution().removeInvalidParentheses(s))
