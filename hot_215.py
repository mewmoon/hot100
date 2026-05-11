# 215 数组中的第k个最大元素

import heapq
from operator import le
import random


# 堆 O(n+klogn)=O(nlogn) O(logn)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        return heap[0]


# 快速选择 O(n) O(logn)
class Solution2(object):
    def findKthLargest(self, nums, k):
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

    def quickSelect(self, nums, l, r, k):
        if l == r:
            return nums[l]
        pivot_idx = random.randint(l, r)
        nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]

        i, j = l - 1, r + 1
        key = nums[l]
        while i < j:
            while True:
                i += 1
                if nums[i] >= key:
                    break
            while True:
                j -= 1
                if nums[j] <= key:
                    break
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        if k <= j:
            return self.quickSelect(nums, l, j, k)
        return self.quickSelect(nums, j + 1, r, k)


nums = [3, 1, 2, 5, 6, 4]
k = 2
print(nums, k)
print(Solution2().findKthLargest(nums, k))
