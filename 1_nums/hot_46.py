# 46 全排列
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        unused = set(nums)
        res = []

        def dfs(path):
            if not unused:
                res.append(path[:])  # ??
                return
            for num in list(unused):  # 集合不可直接遍历
                unused.remove(num)
                path.append(num)
                dfs(path)
                path.pop()
                unused.add(num)

        dfs([])
        return res


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(start):
            if start == n:
                res.append(nums[:])
                return
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        dfs(0)
        return res


nums = [1, 2, 3]
print(Solution().permute(nums))
