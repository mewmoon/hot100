# 84 柱状图中最大矩形

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        n = len(heights)
        left = [0] * n
        right = [n] * n

        stk = []
        for i in range(n):
            while stk and heights[stk[-1]] >= heights[i]:
                right[stk[-1]] = i  # 右边界同时得到,默认值n
                stk.pop()
            left[i] = stk[-1] if stk else -1
            stk.append(i)

        ans = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            ans = max(ans, width * heights[i])
        return ans


heights = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(heights))
