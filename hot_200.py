# 200 岛屿数量
class Solution1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        re = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    re += 1
                    self.dfs_renew_grid(grid, i, j)
        return re

    def dfs_renew_grid(self, grid, i, j):
        grid[i][j] = "0"
        nr, nc = len(grid), len(grid[0])
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                self.dfs_renew_grid(grid, x, y)


class Solution2(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        re = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    re += 1
                    self.bfs_renew_grid(grid, i, j)
        return re

    def bfs_renew_grid(self, grid, r, c):
        nr, nc = len(grid), len(grid[0])
        stack = [(r, c)]
        while stack:
            i, j = stack.pop()
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                    stack.append((x, y))
                    grid[x][y] == "0"
            grid[i][j] = "0"


# 并查集 Union
class Solution3(object):
    pass


grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(Solution2().numIslands(grid))
