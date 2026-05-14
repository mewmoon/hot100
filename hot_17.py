# 17 电话号码的字母组合
from typing import List
from collections import deque


# 双端队列 = bfs
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        queue = deque()
        di = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        for i, ch in enumerate(digits):
            if not queue:
                queue.extend(di[ch])
            while len(queue[0]) <= i:
                prefix = queue.popleft()
                for c in di[ch]:
                    queue.append(prefix + c)
        return list(queue)


# 回溯法 = dfs
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        di = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        re = []
        res = []

        def backtrack(idx):
            if idx == len(digits):
                res.append("".join(re))
                return
            for ch in di[digits[idx]]:
                re.append(ch)
                backtrack(idx + 1)
                re.pop()

        backtrack(0)
        return res


digits = "23"
print(Solution().letterCombinations(digits))
