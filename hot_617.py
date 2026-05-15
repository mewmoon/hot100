# 617 合并二叉树
from typing import Optional
from tools import *


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        if not root1 or not root2:
            return root1 or root2
        node = TreeNode(root1.val + root2.val)
        left = self.mergeTrees(root1.left, root2.left)
        right = self.mergeTrees(root1.right, root2.right)
        node.left = left
        node.right = right
        return node


root1 = [1, 3, 2, 5]
root2 = [2, 1, 3, None, 4, None, 7]
root1 = build_tree(root1)
root2 = build_tree(root2)
print_tree(Solution().mergeTrees(root1, root2))
