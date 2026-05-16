# 416 分割等和子集

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum % 2 == 1:
            return False
        P = num_sum // 2
        dp = [1] + [0] * P
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]  # 用 |= 代替+=也可以
            if dp[P] >= 1:
                return True
        return False


nums = [1, 5, 11, 5]
print(Solution().canPartition(nums))
