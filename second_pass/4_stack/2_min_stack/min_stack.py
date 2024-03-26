class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.min_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
def main():
    obj = MinStack()
    obj.push(2)
    obj.push(3)
    obj.push(-1)
    obj.push(-5)
    obj.push(-2)
    obj.push(-6)

    for i in range(6):
        print(f"top: {obj.top()}, min: {obj.getMin()}")
        obj.pop()


if __name__ == '__main__':
    main()
