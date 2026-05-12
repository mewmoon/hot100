# 124 二叉树中最大路径和
from platform import node

from tools import *
from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_sum = [root.val]

        def maxNodeSum(root):
            if root is None:
                return 0
            l = max(maxNodeSum(root.left), 0)
            r = max(maxNodeSum(root.right), 0)
            max_sum[0] = max(max_sum[0], l + r + root.val)
            return max(l, r) + root.val

        maxNodeSum(root)
        return max_sum[0]


# 示例数组
null = None
nums = [-2, -1]
nums = [-10, 9, 20, null, null, 15, 7]
nums = [1, -2, 3]

root = build_tree(nums)

print(Solution().maxPathSum(root))
