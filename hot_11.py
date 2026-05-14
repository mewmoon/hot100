# 11 盛水最多的容器

# hot_42 接雨水
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(area, ans)
            if height[l] <= height[r]:  # //Hard 难以理解双指针的移动 Tos
                l += 1
            else:
                r -= 1
        return ans


nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(nums))
