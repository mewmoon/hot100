# 239 滑动窗口最大值
from typing import List
import collections


# 超出时间限制
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return 0
        dp = nums.copy()
        for win_size in range(2, k + 1):
            for end in range(len(nums) - 1, win_size - 2, -1):
                dp[end] = max(dp[end - 1], nums[end])
        return dp[k - 1 :]


# 双端队列deque
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:  # 保证队列递减
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans


# nums = [1, 3, -1, -3, 5, 3, 6, 7]
nums = [7, 2, 4]
k = 2
print(Solution2().maxSlidingWindow(nums, k))
