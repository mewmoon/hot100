# 104 二叉树的最大深度
from typing import Optional
from tools import *


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, re):
            if not node:
                self.ans = max(self.ans, re)
                return
            dfs(node.left, re + 1)
            dfs(node.right, re + 1)

        dfs(root, 0)
        return self.ans


root = [3, 9, 20, None, None, 15, 7]
root = build_tree(root)
print(Solution().maxDepth(root))
