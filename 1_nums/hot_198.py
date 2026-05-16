# 198 打家劫舍


# O(m) O(m)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        if n == 1:
            return nums[0]

        # dp = [0] * (n)
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            # dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            first, second = second, max(first + nums[i], second)
        # return dp[-1]
        return second


nums = [2, 7, 9, 3, 1]
print(Solution().rob(nums))
