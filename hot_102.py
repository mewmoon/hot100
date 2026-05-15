# 102 二叉树的层序遍历
from typing import Optional, List
from tools import *
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            re = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                re.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(re)
        return res


root = [3, 9, 20, None, None, 15, 7]
root = build_tree(root)
print(Solution().levelOrder(root))
