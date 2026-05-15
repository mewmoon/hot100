# 4 寻找两个正序数组的中位数
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):  # 保证 nums1 更短 --》num_i-1 <nums_j判断才有用
            return self.findMedianSortedArrays(nums2, nums1)

        inf = 2**40
        m, n = len(nums1), len(nums2)
        median1, median2 = 0, 0

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i  # 注意+1，保证左边>右边

            nums_i_1 = -inf if i == 0 else nums1[i - 1]
            nums_i = inf if i == m else nums1[i]
            nums_j_1 = -inf if j == 0 else nums2[j - 1]
            nums_j = inf if j == n else nums2[j]

            if nums_i_1 <= nums_j:
                left = i + 1
                median1, median2 = max(nums_i_1, nums_j_1), min(nums_i, nums_j)
            else:
                right = i - 1

        return (median1 + median2) / 2.0 if (m + n) % 2 == 0 else median1


nums1 = [1, 2, 8]

nums2 = [3, 4]
print(Solution().findMedianSortedArrays(nums1, nums2))
