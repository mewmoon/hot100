# 55 跳跃游戏

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for idx, num in enumerate(nums):
            if idx > max_reach:  # 跳不到这里
                return False
            max_reach = max(max_reach, idx + num)
            if max_reach >= len(nums) - 1:
                return True

        return False


nums = [3, 2, 1, 0, 4]
print(Solution().canJump(nums))
