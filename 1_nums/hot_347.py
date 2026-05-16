# 347 前K个高频元素
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        # l = sorted([(n, c) for n, c in count.items()], key=lambda x: x[1], reverse=True)
        # re = [n for n, c in l][:k]
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq, num))
        return [item[1] for item in heap]


nums, k = [2, 1, 1, 2, 1, 2, 3, 1, 3, 2], 2
print(Solution().topKFrequent(nums, k))
