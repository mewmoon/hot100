# 394 字符串解码


# 暴力扫描，复杂度高
class Solution:
    def decodeString(self, s: str) -> str:
        while "]" in s:
            r = s.find("]")
            l = s.rfind("[", 0, r)

            for num_start in range(l - 1, -1, -1):
                if not s[num_start].isnumeric():
                    num_start += 1
                    break

            repeat = int(s[num_start:l])
            content = s[l + 1 : r]

            s = s[:num_start] + content * repeat + s[r + 1 :]
        return s


# 栈
class Solution2:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""  # 当前正在构建的字符串
        multi = 0  # 当前正在构建的数字

        for c in s:
            if "0" <= c <= "9":
                multi = multi * 10 + int(c)
            elif c == "[":
                stack.append([multi, res])
                res, multi = "", 0
            elif c == "]":
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            else:
                res += c

        return res


s = "13[a]2[bc]"
s = "3[a]2[bc]"
print(Solution2().decodeString(s))
