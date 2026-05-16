# 739 每日温度
# O(n) O(n)
class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        re = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                re[prev] = i - prev
            stack.append(i)
        return re


# temperatures = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
out = Solution().dailyTemperatures(temperatures)
print(out)
