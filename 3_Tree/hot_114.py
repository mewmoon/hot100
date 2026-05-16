# 114 二叉树展开为链表
from typing import Optional
from tools import *


# 需要额外空间
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        tmp_left, tmp_right = root.left, root.right

        root.left = None
        root.right = tmp_left

        curr = root
        while curr.right:
            curr = curr.right

        curr.right = tmp_right
        return curr


# Good
class Solution2:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right

                predecessor.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

        return root


root = [1, 2, 5, 3, 4, None, 6]
root = build_tree(root)
print(Solution().flatten(root))
