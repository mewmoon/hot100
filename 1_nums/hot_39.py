# 39 组合总和
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        re = []
        candidates.sort()

        def dfs(remain, start):
            if remain == 0:
                res.append(re[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if remain - num < 0:
                    break
                re.append(num)
                dfs(remain - num, i)
                re.pop()

        dfs(target, 0)
        return res


candidates = [2, 3, 6, 7]
target = 7

print(Solution().combinationSum(candidates, target))
