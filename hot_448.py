# 448 找到所有数组中消失的数字
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        ns = len(num_set)
        disapp = []
        for num in range(1, n + 1):
            if num not in num_set:
                disapp.append(num)
                if len(disapp) + ns == n:
                    break

        return disapp


# 原地哈希
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n
        re = [i + 1 for i, num in enumerate(nums) if num <= n]
        return re


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution2().findDisappearedNumbers(nums))
