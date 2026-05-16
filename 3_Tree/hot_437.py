# 437 路径总和Ⅲ

from tools import *
from typing import Optional
import collections


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.path = []
        self.end_sum = []
        self.count = 0

        def dfs(root):
            if root is None:
                return

            self.path.append(root.val)
            print(self.path)
            current_sum = 0
            for val in reversed(self.path):
                current_sum += val
                if current_sum == targetSum:
                    self.count += 1
                    print("good:", self.path)

            dfs(root.left)
            dfs(root.right)
            self.path.pop()

        dfs(root)
        return self.count


# O(N) O(N)
class Solution2:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]  # 先更新net再prefix[curr]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1
            return ret

        return dfs(root, 0)


# nums = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
# nums = [1, -2, -3, 1, 3, -2, None, -1
nums = [1]
root = build_tree(nums)
print(Solution2().pathSum(root, 0))
