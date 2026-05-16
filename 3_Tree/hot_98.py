# 98 搜索二叉树
from typing import Optional
from tools import *


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False

            return check(node.left, lower, node.val) and check(
                node.right, node.val, upper
            )

        return check(root, float("-inf"), float("inf"))


root = [5, 1, 4, None, None, 3, 6]
root = build_tree(root)
print(Solution().isValidBST(root))
