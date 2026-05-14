# 48 旋转图像
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        n = len(matrix)
        for i in range(0, n // 2):
            l = n - 2 * i - 1
            for j in range(0, l):
                tmp = matrix[i][i + j]
                matrix[i][i + j] = matrix[i + l - j][i]
                matrix[i + l - j][i] = matrix[i + l][i + l - j]
                matrix[i + l][i + l - j] = matrix[i + j][i + l]
                matrix[i + j][i + l] = tmp
        return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().rotate(matrix))
