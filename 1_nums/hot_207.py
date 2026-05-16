# 207 课程表
import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        valid = [True]

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u):
            # nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid[0]:
                        return
                if visited[v] == 1:
                    valid[0] = False
                    return
            visited[u] = 2

        for i in range(numCourses):
            if valid[0] and visited[i] == 0:
                dfs(i)

        return valid[0]


numCourses = 6
prerequisites = [[1, 3], [1, 2], [3, 0], [1, 4], [4, 2]]
# prerequisites = [[1, 0], [0, 1]]
print(Solution().canFinish(numCourses, prerequisites))
