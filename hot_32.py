# 32 最长有效括号


# //Hard 难以理解Tos
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)  # 重置
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_ans = 0

        # 1. 从左向右遍历
        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1

            if left == right:
                max_ans = max(max_ans, 2 * right)
            elif right > left:
                left = right = 0

        # 重置计数器，进行反向遍历
        left = right = 0

        for char in reversed(s):
            if char == "(":
                left += 1
            else:
                right += 1

            if left == right:
                max_ans = max(max_ans, 2 * left)
            elif left > right:
                left = right = 0

        return max_ans


s = "()((())()"
print(Solution().longestValidParentheses(s))
