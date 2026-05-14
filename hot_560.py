# 560 和为K的子数组
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = {0: 1}
        ans = 0
        total = 0

        for num in nums:
            total += num
            if total - k in cnt:
                ans += cnt[total - k]
            cnt[total] = cnt.get(total, 0) + 1

        return ans


nums = [1, 1, 1]
k = 2
print(Solution().subarraySum(nums, k))
