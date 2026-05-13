# 283 移动零
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for num in nums:
            if num != 0:
                nums[l] = num
                l += 1
        for i in range(l, len(nums)):
            nums[i] = 0
        return nums


# 双指针 避免第二次遍历nums进行赋值
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
