# 338 比特位计数
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        re = [0, 1] + [0] * (n - 1)
        for idx in range(2, n + 1):
            i = idx
            while i > 0:
                re[idx] += re[i & 1]
                i = i // 2
        return re


# 官方解法 O(n) O(1)
class Solution2:
    def countBits(self, n: int) -> List[int]:
        re = [0]
        highBit = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                highBit = i
            re.append(1 + re[i - highBit])
        return re


print(Solution2().countBits(6))
