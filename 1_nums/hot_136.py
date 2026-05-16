# 136 只出现一次的数字
from typing import List


# O(n) O(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        vo = set()
        for num in nums:
            if num not in vo:
                vo.add(num)
            else:
                vo.remove(num)
        return vo.pop() if vo else None


# O(n) O(1)   异或
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


nums = [2, 2, 1]
print(Solution2().singleNumber(nums))
