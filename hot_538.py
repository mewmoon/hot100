# 538 把二叉搜索树转化为累加树
from tools import *
from typing import Optional


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.total += node.val
            node.val = self.total
            dfs(node.left)

        self.total = 0
        dfs(root)
        return root


#  Morris 遍历 //Hard Tos
#  https://www.youtube.com/watch?v=wGXB9OWhPTg

root = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
root = build_tree(root)
print(print_tree(Solution().convertBST(root)))
