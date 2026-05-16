# 20 有效的括号


class Solution:
    def isValid(self, s: str) -> bool:
        di = {"}": "{", "]": "[", ")": "("}
        stack = []
        for ch in s:
            if ch not in di:
                stack.append(ch)
            else:
                if not stack or di[ch] != stack.pop():
                    return False
        return len(stack) == 0


s = "([])"

print(Solution().isValid(s))
