# 75 颜色分类
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                nums[idx], nums[l] = nums[l], nums[idx]
                l += 1
        for idx in range(0, len(nums)):
            if nums[idx] == 1:
                nums[idx], nums[l] = nums[l], nums[idx]
                l += 1
        return nums


# 双指针法
class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l0, l1 = 0, 0
        for idx in range(0, len(nums)):
            if nums[idx] == 0:
                nums[idx], nums[l0] = nums[l0], nums[idx]
                if l0 < l1:
                    nums[idx], nums[l1] = nums[l1], nums[idx]
                l0 += 1
                l1 += 1
            elif nums[idx] == 1:
                nums[idx], nums[l1] = nums[l1], nums[idx]
                l1 += 1
        return nums


nums = [1, 0, 0]
print(Solution().sortColors(nums))
