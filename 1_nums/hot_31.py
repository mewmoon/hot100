# 31 下一个排列
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        l, r = i + 1, len(nums) - 1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums


nums = [2, 2, 7, 5, 4, 3, 2, 2, 1]
# nums = [3, 2, 1]
print(Solution().nextPermutation(nums))
