# 1 两数之和
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for idx, num in enumerate(nums):
            if target - num in di:
                return [di[target - num], idx]
            di[num] = idx
        return [-1, -1]


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
