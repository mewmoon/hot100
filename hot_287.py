# 287 寻找重复数
from typing import List


# O(nlogn) O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums) - 1
        ans = r
        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            print(mid, cnt)
            if cnt > mid:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


# O(n) O(1) 快慢指针
class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        loc = 0
        while loc != slow:
            loc = nums[loc]
            slow = nums[slow]
        return loc


nums = [1, 3, 4, 2, 2]

print(Solution2().findDuplicate(nums))
