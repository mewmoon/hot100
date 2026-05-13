# 最长递增子序列
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ma = 1
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for k in range(0, i):
                if nums[i] > nums[k]:
                    dp[i] = max(dp[i], dp[k] + 1)
            ma = max(ma, dp[i])

        return ma


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for num in nums:
            i = 0
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                l, r = 0, len(dp) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if num <= dp[mid]:  # 找第一个大于等于num的dp，所以loc的更新放在这里
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                dp[loc] = num
        return len(dp)


# nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
nums = [0, 1, 0, 3, 2, 3]
print(Solution2().lengthOfLIS(nums))
