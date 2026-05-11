# 155 最小栈


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # or [math.inf]

    def push(self, val: int) -> None:
        self.min = val if not self.stack else min(val, self.min_stack[-1])
        self.stack.append(val)
        self.min_stack.append(self.min)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-4)
