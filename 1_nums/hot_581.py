# 581 最短无序连续子数组
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans_l, ans_r = n, -1

        stack = []
        ma = float("-inf")

        for idx, num in enumerate(nums):
            # 注意是while不是if, <第一次出现, ≤ 最新一次出现
            while stack and num < nums[stack[-1]]:
                ans_l = min(stack[-1], ans_l)
                stack.pop()
            stack.append(idx)

            ma = max(ma, num)
            if num < ma:
                ans_r = idx

        return ans_r - ans_l + 1 if ans_l <= ans_r else 0


# O(n) O(1)  没看懂
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]

            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]

        return 0 if right == -1 else right - left + 1


nums = [1, 2, 4, 5, 3]
print(Solution().findUnsortedSubarray(nums))
