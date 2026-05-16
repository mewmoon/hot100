# 297 二叉树的序列化与反序列化
from tools import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        li = []

        def dfs(node):
            if not node:
                li.append("None")
                return
            li.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(li)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_iter = iter(data.split(","))

        def dfs_re():
            val = next(data_iter)
            if val == "None":
                return None
            node = TreeNode(int(val))
            node.left = dfs_re()
            node.right = dfs_re()
            return node

        return dfs_re()


root = [1, 2, 5, 3, 4, None, None]
root = build_tree(root)


data = Codec().serialize(root)
root = Codec().deserialize(data)
print(data)
print(Codec().serialize(root))
