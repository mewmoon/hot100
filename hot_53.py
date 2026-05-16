# 53 最大子数组和
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ma, cumm = float("-inf"), 0
        for num in nums:
            cumm = max(num, cumm + num)
            ma = max(cumm, ma)
        return ma


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        def get_max(l: int, r: int) -> tuple:
            # 返回四个值: (lSum, rSum, mSum, iSum)
            # lSum: 以左边界为起点的最大子段和
            # rSum: 以右边界为终点的最大子段和
            # mSum: 区间内的最大子段和（我们最终要的答案）
            # iSum: 区间所有元素的总和
            if l == r:
                return nums[l], nums[l], nums[l], nums[l]

            mid = (l + r) // 2
            # 递归解决左半边和右半边
            l_lSum, l_rSum, l_mSum, l_iSum = get_max(l, mid)
            r_lSum, r_rSum, r_mSum, r_iSum = get_max(mid + 1, r)

            # 组合左右两半边的信息（类似线段树的 PushUp 操作）
            iSum = l_iSum + r_iSum
            lSum = max(l_lSum, l_iSum + r_lSum)
            rSum = max(r_rSum, r_iSum + l_rSum)
            # 核心：最大子段和可能在左边、右边，或者跨越中间（左rSum + 右lSum）
            mSum = max(l_mSum, r_mSum, l_rSum + r_lSum)

            return lSum, rSum, mSum, iSum

        return get_max(0, len(nums) - 1)[2]


nums = [5, 4, -1, 7, 8]
print(Solution().maxSubArray(nums))
