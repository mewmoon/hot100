# 621 任务调度器
from typing import List
import collections


class Solution:
    def leastInterval(self, tasks: List[str], count: int) -> int:
        freq = collections.Counter(tasks)

        maxExec = max(freq.values())
        maxCount = sum(1 for v in freq.values() if v == maxExec)

        return max((maxExec - 1) * (count + 1) + maxCount, len(tasks))


tasks = ["A", "A", "A", "B", "B", "B"]
n = 3
print(Solution().leastInterval(tasks, n))
