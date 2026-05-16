# 494 目标和
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        tmp = total_sum + target
        if abs(target) > total_sum or tmp % 2 == 1:
            return 0
        P = tmp // 2

        dp = [1] + [0] * P
        for num in nums:
            for j in range(P, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[P]


nums, target = [
    35,
    16,
    11,
    38,
    44,
    5,
    17,
    20,
    23,
    0,
    27,
    46,
    38,
    29,
    22,
    18,
    27,
    34,
    12,
    10,
], 22
nums, target = [1, 1, 1, 1, 1], 3
print(Solution().findTargetSumWays(nums, target))
