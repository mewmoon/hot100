# 128 最长连续序列
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_re = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_re = 1
                current_num = num

                while current_num + 1 in num_set:
                    current_re += 1
                    current_num = current_num + 1
                longest_re = max(longest_re, current_re)

        return longest_re


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Solution().longestConsecutive(nums))
