# 406 根据身高重建队列
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        n = len(people)
        ans = list()
        for person in people:
            # ans[person[1] : person[1]] = [person]
            ans.insert(person[1], person)  # 等同于上一行
        return ans


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(people))
