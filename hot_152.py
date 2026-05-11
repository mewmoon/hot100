# 152 乘积最大子数组
from typing import List
from math import inf


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        ma = dp1 = dp2 = nums[0]

        for num in nums[1:]:
            dp1, dp2 = min(dp2 * num, dp1 * num, num), max(dp2 * num, dp1 * num, num)
            ma = max(dp2, ma)
        return ma


nums = [2, 3, -2, 4]
print(Solution().maxProduct(nums))
