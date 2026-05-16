# 105 从前序与中序遍历序列构造二叉树
from typing import List, Optional
from tools import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: i for i, val in enumerate(inorder)}

        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            mid = index_map[root_val]
            left_size = mid - in_left

            root.left = helper(pre_left + 1, pre_left + left_size, in_left, mid - 1)
            root.right = helper(pre_left + left_size + 1, pre_right, mid + 1, in_right)
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print_tree(Solution().buildTree(preorder, inorder))
