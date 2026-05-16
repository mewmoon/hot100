# 42 接雨水
from typing import List


# 双指针 O(n) O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = 0, 0
        l, r = 0, len(height) - 1
        re = 0
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax < rightMax:
                re += leftMax - height[l]
                l += 1
            else:
                re += rightMax - height[r]
                r -= 1
        return re


# 单调栈 O(n) O(n)
class Solution2:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans


height = [5, 4, 3, 2, 1, 4]
print(Solution2().trap(height))
