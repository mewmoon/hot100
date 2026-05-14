# 22 括号生成
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []

        def dfs(prefix, l, r):
            if l == 0:
                res.append(prefix + ")" * r)
                return
            if l > r:
                return

            if l > 0:
                dfs(prefix + "(", l - 1, r)
            if r > 0:
                dfs(prefix + ")", l, r - 1)

        dfs("(", n - 1, n)
        return res


print(Solution().generateParenthesis(3))
