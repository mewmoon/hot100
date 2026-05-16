# 461 汉明距离


from itertools import count


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        s = x ^ y
        dis = 0
        while s != 0:
            if s % 2 == 1:
                dis += 1
                s = s - 1
            s = s // 2
        return dis


class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        s = x ^ y
        dis = 0
        while s != 0:
            dis += s & 1
            s = s >> 1
        return dis


class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()


print(Solution().hammingDistance(1, 4))
