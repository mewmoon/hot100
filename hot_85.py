# 85 最大矩形
from typing import List

# see hot 221 最大正方形
# see hot 84 柱状图中最大矩形


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        left = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    left[i][j] = (0 if j == 0 else left[i][j - 1]) + 1

        ans = 0
        for j in range(n):
            up = [0] * m
            down = [0] * m

            stk = []
            for i in range(m):
                while stk and left[stk[-1]][j] >= left[i][j]:
                    stk.pop()
                up[i] = stk[-1] if stk else -1
                stk.append(i)

            stk = []
            for i in range(m - 1, -1, -1):
                while stk and left[stk[-1]][j] >= left[i][j]:
                    stk.pop()
                down[i] = stk[-1] if stk else m
                stk.append(i)

            for i in range(m):
                height = down[i] - up[i] - 1
                ans = max(ans, height * left[i][j])

        return ans


# 优化版 单次循环，左右边界同时更新
class Solution2:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        # 逐行处理，每一行都看作是一个“柱状图求最大矩形”的问题
        for i in range(m):
            # 1. 更新当前行的柱子高度
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0

            # 2. 复用第 84 题的单调栈优化：一次遍历求出当前行的最大矩形
            # 初始化左右边界：left 默认为 -1，right 默认为 n
            left = [-1] * n
            right = [n] * n
            stk = []

            for j in range(n):
                while stk and heights[stk[-1]] >= heights[j]:
                    right[stk[-1]] = j
                    stk.pop()
                left[j] = stk[-1] if stk else -1
                stk.append(j)

            for j in range(n):
                width = right[j] - left[j] - 1
                max_area = max(max_area, width * heights[j])

        return max_area


matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]

print(Solution().maximalRectangle(matrix))
