# 226 翻转结点


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left

        return root
