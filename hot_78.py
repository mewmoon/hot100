# 78 子集
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        re = []

        def dfs(cur):
            if cur == len(nums):
                ans.append(re[:])
                return
            re.append(nums[cur])
            dfs(cur + 1)
            re.pop()
            dfs(cur + 1)

        dfs(0)
        return ans


nums = [1, 2, 3]
print(Solution().subsets(nums))
