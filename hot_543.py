# 543 二叉树的直径

from tools import *
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l + r)
            return max(l, r) + 1

        dfs(root)
        return self.ans


root = [1, 2, 3, 4, 5]
root = build_tree(root)
print(Solution().diameterOfBinaryTree(root))
