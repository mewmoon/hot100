# 101 对称二叉树
from typing import Optional
from tools import *


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return check(p.left, q.right) and check(p.right, q.left)

        return check(root.left, root.right)


root = [1, 2, 2, 3, 4, 3]
root = build_tree(root)
print(Solution().isSymmetric(root))
