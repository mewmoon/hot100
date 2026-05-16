# 337 打家劫舍Ⅲ
from tools import *
from typing import Optional


#
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        selected = {None: 0}
        no_selected = {None: 0}

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)

            selected[node] = node.val + no_selected[node.left] + no_selected[node.right]
            no_selected[node] = max(selected[node.left], no_selected[node.left]) + max(
                selected[node.right], no_selected[node.right]
            )

        dfs(root)
        return max(selected[root], no_selected[root])


#
class Solution2:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            sl, nl = dfs(node.left)
            sr, nr = dfs(node.right)
            return node.val + nl + nr, max(sl, nl) + max(sr, nr)

        return max(dfs(root))


root = [3, 2, 3, None, 3, None, 1]
root = build_tree(root)
print(Solution2().rob(root))
