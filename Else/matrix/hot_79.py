# 79 单词搜索
from typing import Counter, List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # --- 词频剪枝 ---
        word_dict = Counter(word)
        board_dict = Counter(char for row in board for char in row)
        for char, count in word_dict.items():
            if board_dict[char] < count:
                return False

        # --- 反转剪枝 ---
        if board_dict[word[0]] > board_dict[word[-1]]:
            word = word[::-1]
        # visited = [[0] * n for _ in range(m)]  # board原地标记 #

        def dfs(i, j, start):
            if start == len(word):
                return True
            tmp = board[i][j]
            board[i][j] = "#"  # visited
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (
                    0 <= x < m and 0 <= y < n and board[x][y] == word[start]
                ):  # 不需要判断visited
                    if dfs(x, y, start + 1):
                        return True
            board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True
        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
print(Solution().exist(board, word))
