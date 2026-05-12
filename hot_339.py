# 339 除法求值
from typing import List
import collections


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:

        # 1. 构造双向图
        # graph[A][B] = k 表示 A / B = k
        graph = collections.defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        print(graph)

        # 2. 定义 DFS 搜索路径
        def dfs(start, end, visited):
            # 如果起点或终点不在图中，直接返回 -1
            if start not in graph or end not in graph:
                return -1.0
            # 找到终点
            if start == end:
                return 1.0

            visited.add(start)

            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    # 递归寻找路径：(start -> neighbor) * (neighbor -> end)
                    res = dfs(neighbor, end, visited)
                    if res != -1.0:
                        return value * res
            return -1.0

        # 3. 处理每个查询
        ans = []
        for x, y in queries:
            ans.append(dfs(x, y, set()))

        return ans


# --- 测试用例 ---
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(Solution().calcEquation(equations, values, queries))
# 输出: [6.0, 0.5, -1.0, 1.0, -1.0]

equations2 = [["a", "b"], ["c", "b"], ["bc", "cd"]]
values2 = [1.5, 2.5, 5.0]
queries2 = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
print(Solution().calcEquation(equations2, values2, queries2))
# 输出: [0.6, 2.5, 5.0, 0.2]
