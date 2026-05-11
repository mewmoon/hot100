# 238 除自身以外数组的乘积

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = set()
        product = 1
        for idx, num in enumerate(nums):
            if num == 0:
                count.add(idx)
            else:
                product *= num

        re = [0] * len(nums)
        if len(count) == 0:
            re = [product // num for num in nums]
        elif len(count) == 1:
            re[count.pop()] = product
        return re


nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))
