# 34 在排序数组中查找元素的第一个和最后一个位置
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def get_bound(is_left):
            re = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    re = mid
                    if is_left:
                        r = mid - 1
                    else:
                        l = mid + 1
            return re

        return [get_bound(True), get_bound(False)]


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(Solution().searchRange(nums, target))
