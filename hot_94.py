# 94 二叉树中序遍历
from tools import *
from typing import Optional, List
from collections import deque


# 递归 + 全局/闭包列表（简单高效）
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res


# 迭代法（使用显式栈，避免递归溢出）
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res


root = [1, None, 2, 3]
root = build_tree(root)
print(Solution().inorderTraversal(root))
